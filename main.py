import os
from wsgiref import simple_server
from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    return "Flask app is running locally - done some changesgit "

port = int(os.getenv("PORT",5000))

if __name__ == "__main__":
    host = '127.0.0.1'
    #app.run
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()