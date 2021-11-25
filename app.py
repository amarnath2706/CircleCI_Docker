from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return 'Flask app is running from app.py'


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

#circleci-docker-deployment
#cda36648-276f-4d7a-8ddc-2f1a640e5bca