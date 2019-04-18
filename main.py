import requests
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    print ('abcdef')
    return 'Hello World! (THIS IS ROM HERE!!!)'

@app.route('/chilema/')
def chilema():
    return 'hai meiyou chi ne, dao ni jia chi qu.'

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return "recevie POST login request."
    code = request.args.get("code","")
    #app.logger.info('recevie login code:' + code)
    print ("[ROM_DEBUG], code:" + code)
    authCode2Session(code)
    return "recevie GET login request."

def authCode2Session(code):
    APPID = "wx0feab39f50fd2674"
    SECRET = "39645c2ec117df4c5b8f8f91b7598623"
    reqUrl = "https://api.weixin.qq.com/sns/jscode2session?appid="+APPID+"&secret="+SECRET+"&js_code="+code+"&grant_type=authorization_code"
    r = requests.get(reqUrl)
    print("[ROM_DEBUG], r:"+r.text)

#if __name__ == '__main__':
#    app.run()
