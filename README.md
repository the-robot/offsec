# HackTheBox writeups

![](https://geps.dev/progress/56)  
**49/87** done. 

**Active boxes are password protected.**

<br/>

## Useful Links

- [ippsec.rocks](https://ippsec.rocks/)
- [kashz-jewel](https://kashz.gitbook.io/kashz-jewels/) - like Hacktricks
- [revshells](https://www.revshells.com/) - generate reverse shells easily
- [OSCP preperation notes](https://oscpnotes.infosecsanyam.in/My_OSCP_Preparation_Notes.html) - super useful list of commands in case you forgot how to run
- [Windows cheetsheet](https://0xsp.com/offensive/red-team-cheatsheet/)
- [Windows file transfer methods](https://academy.hackthebox.com/course/preview/file-transfers/windows-file-transfer-methods)
- [PowerView tips and tricks](https://gist.github.com/the-robot/c0396e87dd2bab8c4ca0ac80e70c95b4)
- [Exploitdb Bin Sploits](https://gitlab.com/exploit-database/exploitdb-bin-sploits) - pre-compiled list of exploitdb binaries

### Active Directory

- [WADComs - GTFOBin for AD](https://wadcoms.github.io/)
- [Active Directory cheetsheet](https://medium.com/@kuwaitison/active-directory-cheat-sheet-94e0bb9bed2)

### Some good articles to read for OSCP preperation

- [OSCP — CRACKING THE NEW PATTERN](https://jaiguptanick.github.io/Blog/blog/OSCP_Cracking_New_Pattern_Walkthrough/)
- [OSCP 2022 — Tips To Help You Pass: K.I.S.S.](https://medium.com/@0xP/oscp-2022-tips-to-help-you-pass-dddd3563967e)

## tjnull Linux boxes

- [x] Lame
- [x] brainfuck
- [x] shocker
- [x] bashed
- [x] nibbles
- [x] beep
- [x] cronos
- [x] nineveh
- [x] sense
- [x] solidstate
- [x] node
- [x] valentine
- [x] poison
- [x] sunday
- [x] tartarsauce
- [ ] lrked
- [x] Friendzone
- [x] Swagshop
- [x] Networked
- [x] jarvis
- [ ] Mirai
- [ ] Popcorn
- [x] Haircut
- [x] Blocky
- [x] Frolic
- [x] Postman
- [x] Mango
- [x] Traverxec
- [x] OpenAdmin
- [x] Magic
- [x] Admirer
- [x] Blunder
- [x] Tabby
- [x] Doctor
- [ ] SneakyMailer
- [ ] Passage
- [ ] Luanne
- [ ] Time
- [x] Ready
- [x] Delivery
- [x] Ophiuchi
- [x] ScriptKiddie
- [x] Armageddon
- [x] Knife
- [x] Pit
- [x] Seal
- [x] Previse
- [x] Forge
- [x] Horizontall
- [x] Shibboleth

## tjnull Window boxes

- [x] legacy
- [x] Blue
- [x] Devel
- [x] Optimum
- [x] Bastard
- [x] granny
- [x] Arctic
- [x] grandpa
- [x] silo
- [x] bounty
- [x] jerry
- [x] conceal
- [x] chatterbox
- [x] Forest (Active Directory)
- [ ] BankRobber
- [x] secnotes
- [ ] Suana (Active Directory)
- [ ] Bastion
- [ ] Buff
- [ ] Servmon
- [ ] Active (Active Directory)
- [ ] Remote
- [ ] Fuse
- [ ] Omni
- [x] Worker
- [ ] Love
- [ ] Intelligence (Active Directory)
- [ ] APT
- [ ] Object (Active Directory)
- [ ] Support
- [ ] Acute (Active Directory)
- [x] Timelapse (Active Directory)
- [x] StreamIO (Active Directory)
- [x] Scrambled (Active Directory)


## Other boxes

- [x] Ambassador
- [x] MetaTwo
- [x] Photobomb
- [x] RedPanda
- [x] Shoppy
- [x] UpDown

<br/>

## Active Directory practice

- [x] [THM: Attacktive Directory](https://tryhackme.com/room/attacktivedirectory)
- [x] [THM: Hacking Active Directory](https://tryhackme.com/module/hacking-active-directory)
    - [draw.io diagram to understand the AD attack easier](https://github.com/the-robot/hackthebox/blob/master/THM/compromising-active-directory/THM%20-%20Hacking%20AD.pdf)

![AD attack diagram](https://raw.githubusercontent.com/the-robot/hackthebox/master/THM/compromising-active-directory/AD%20Privesc.svg)

<br/>

## Scripts

#### Privilege escalation

- [jailbreak-rbash](https://github.com/the-robot/hackthebox/blob/master/scripts/pe/jailbreak-rbash.sh) - command to find out what commands are available that has a potential of spawning a proper shell, commands are taken from [GTFOBins with +Shell](https://gtfobins.github.io/#+Shell) 
