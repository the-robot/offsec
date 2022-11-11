#include <stdio.h>
#include <stdlib.h>

// gcc -m32 -no-pie -o rop rop.c

int main(int argc, char *argv[])
{
    setuid(0);
    if (argc < 2)
    {
        printf("[*] Usage: program <message>\n");
        return -1;
    }
    vuln(argv[1]);
    return 0;
}

void vuln(char * arg)
{
    char text[40];
    strcpy(text, arg);
    printf("[+] Message sent: ");
    printf(text);
}
