# database 관련

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # SQLALchemy를 사용해 데이터베이스 저장

'''
class Question(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)

class Answer(db.Model) :
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'cascade'))
    question = db.relationship('Question', backref=db.backref('answer_set', ))
    # question = db.relationship('Question', backref=db.backref('answer_set', casecade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)
'''
class User(db.Model) :
    __table_name__ = 'user' # table 이름
    user_seq = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(200), unique=True, nullable=True) # id는 email형식으로 받자
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable = False)
    phone = db.Column(db.String(150), unique=True, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    sex = db.Column(db.String(2), nullable = False)
    height = db.Column(db.Float(150), nullable = False)
    weight = db.Column(db.Float(150),  nullable = False)