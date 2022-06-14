from flask import Flask, render_template, request
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate(app, db)

@app.route('/')
def main_user():
    return render_template('index2.html')

@app.route('/signin') # 로그인 - 원래 join이었는데 파일이름 임의로 바꿨음 헷갈려서
def signin():
    return render_template('signin.html')

@app.route('/join',methods = ['GET','POST']) # 회원가입 - 원래 sign이었음
def join():
    if request.method == 'POST' :
        return render_template('write.html')
    return render_template('join.html')

@app.route('/write') 
def write():
    return render_template('write.html')

@app.route('/main')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)