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
    return "recevie GET login request."

#if __name__ == '__main__':
#    app.run()
