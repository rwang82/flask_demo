from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World! (THIS IS ROM HERE!!!)'

@app.route('/chilema/')
def chilema():
    return 'hai meiyou chi ne, dao ni jia chi qu.'

#if __name__ == '__main__':
#    app.run()
