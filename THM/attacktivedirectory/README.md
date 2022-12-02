# Scan

```bash
khant@Khants-MacBook-Pro [17:32:02] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.11.13:53
Open 10.10.11.13:88
Open 10.10.11.13:80
Open 10.10.11.13:139
Open 10.10.11.13:135
Open 10.10.11.13:389
Open 10.10.11.13:445
Open 10.10.11.13:464
Open 10.10.11.13:593
Open 10.10.11.13:636
Open 10.10.11.13:3269
Open 10.10.11.13:3268
Open 10.10.11.13:3389
Open 10.10.11.13:5985
Open 10.10.11.13:9389
Open 10.10.11.13:47001
Open 10.10.11.13:49667
Open 10.10.11.13:49676
Open 10.10.11.13:49674
Open 10.10.11.13:49669
Open 10.10.11.13:49675
Open 10.10.11.13:49679
Open 10.10.11.13:49665
Open 10.10.11.13:49664
Open 10.10.11.13:49684
Open 10.10.11.13:49694
Open 10.10.11.13:49811

PORT      STATE SERVICE       REASON  VERSION
53/tcp    open  domain        syn-ack Simple DNS Plus
80/tcp    open  http          syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-methods:
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
88/tcp    open  kerberos-sec  syn-ack Microsoft Windows Kerberos (server time: 2022-12-02 09:34:13Z)
135/tcp   open  msrpc         syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn   syn-ack Microsoft Windows netbios-ssn
389/tcp   open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp   open  microsoft-ds? syn-ack
464/tcp   open  kpasswd5?     syn-ack
593/tcp   open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped    syn-ack
3268/tcp  open  ldap          syn-ack Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped    syn-ack
3389/tcp  open  ms-wbt-server syn-ack Microsoft Terminal Services
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Issuer: commonName=AttacktiveDirectory.spookysec.local
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-12-01T09:14:16
| Not valid after:  2023-06-02T09:14:16
| MD5:   27e1f2280abb01d89dc3967541f0afbf
| SHA-1: 470b720b819ece6e718a4ff6041d837dc71400f1
| -----BEGIN CERTIFICATE-----
| MIIDCjCCAfKgAwIBAgIQQEtv0HC9LqhAYh7H6g0QJTANBgkqhkiG9w0BAQsFADAu
| MSwwKgYDVQQDEyNBdHRhY2t0aXZlRGlyZWN0b3J5LnNwb29reXNlYy5sb2NhbDAe
| Fw0yMjEyMDEwOTE0MTZaFw0yMzA2MDIwOTE0MTZaMC4xLDAqBgNVBAMTI0F0dGFj
| a3RpdmVEaXJlY3Rvcnkuc3Bvb2t5c2VjLmxvY2FsMIIBIjANBgkqhkiG9w0BAQEF
| AAOCAQ8AMIIBCgKCAQEAoCCnyRN4mPyDPZVBLh8OleZbDkufC9hgVz73Eg9tTlJf
| 4airTh58LDVvd51bmQMqIkn5DjWgeDbTjgFyEupe/Sq/CcchQlwG70/lrAeRmvOv
| rcKYDQ/ld1T89giG8fQkXxzaDhreqJmR9A3p8e1vQTPaLdptbZu8jsHVkdIAI9Bc
| 7ruqgT8MoHBkSMA8zRvo0hGgQL4ovH6ipM6gN+hT0uhzvEPNFSBUcqAvHM6124Iy
| 1p95rDOSQS2FNUgQCbre2Nc6war3S5AYBqluPAhE9wGi907Rm88/KXxc1lOqxjL2
| pXsn3GyOjkR1BFuaXXelY5i8NAvcTYboDqdbryc2tQIDAQABoyQwIjATBgNVHSUE
| DDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBDAwDQYJKoZIhvcNAQELBQADggEBADau
| P44nTtKHe/e/lDzsrAWO37ofGgGrWUwpH7dqq2Nbi2Sgc47F79e+2d1F7jjQtDI2
| fzqhvWxUjP0yziSabK4Vkb1MJr/SYosB4SGkzghU5VXSX7YF3Ci8GYnya2WgMi2D
| of9UPUhrZmeoAp311EsTpvdQKt4tzvyiSaH4B/JrpGBA66l4XLJufQW9CcYHhQPf
| u+A1Xs8AJ4fHDmqmrfNHXZoJazsn0tspIwbwJSicIpwzW+NYZRcL2Mz8HLwEey4m
| uyPi615WQTk/YH4nn6QmxS3xQoRPxgf9gJjvo1JLd18E1l5apdMay+ZQheRRPK7a
| C7BYmiItdT3iyT4V8i8=
|_-----END CERTIFICATE-----
| rdp-ntlm-info:
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2022-12-02T09:35:13+00:00
|_ssl-date: 2022-12-02T09:35:23+00:00; +1s from scanner time.
5985/tcp  open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp  open  mc-nmf        syn-ack .NET Message Framing
47001/tcp open  http          syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open  msrpc         syn-ack Microsoft Windows RPC
49665/tcp open  msrpc         syn-ack Microsoft Windows RPC
49667/tcp open  msrpc         syn-ack Microsoft Windows RPC
49669/tcp open  msrpc         syn-ack Microsoft Windows RPC
49674/tcp open  msrpc         syn-ack Microsoft Windows RPC
49675/tcp open  ncacn_http    syn-ack Microsoft Windows RPC over HTTP 1.0
49676/tcp open  msrpc         syn-ack Microsoft Windows RPC
49679/tcp open  msrpc         syn-ack Microsoft Windows RPC
49684/tcp open  msrpc         syn-ack Microsoft Windows RPC
49694/tcp open  msrpc         syn-ack Microsoft Windows RPC
49811/tcp open  msrpc         syn-ack Microsoft Windows RPC
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-security-mode:
|   311:
|_    Message signing enabled and required
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 14398/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 38431/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 24772/udp): CLEAN (Timeout)
|   Check 4 (port 45275/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time:
|   date: 2022-12-02T09:35:13
|_  start_date: N/A
```


