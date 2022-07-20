# database 관련

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from sqlalchemy import ForeignKey
db = SQLAlchemy() # SQLALchemy를 사용해 데이터베이스 저장

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
    acti = db.Column(db.Integer,  nullable = False)

    field1 = db.Column(db.Float(150),  nullable = False)
    field2 = db.Column(db.Float(150),  nullable = False)
    field3 = db.Column(db.Float(150),  nullable = False)
    field4 = db.Column(db.Float(150),  nullable = False)
    field5 = db.Column(db.Float(150),  nullable = False)
    field6 = db.Column(db.Float(150),  nullable = False)
    field7 = db.Column(db.Float(150),  nullable = False)
    field8 = db.Column(db.Float(150),  nullable = False)
    field9 = db.Column(db.Float(150),  nullable = False)
    field10 = db.Column(db.Float(150),  nullable = False)
    field11 = db.Column(db.Float(150),  nullable = False)
    field12 = db.Column(db.Float(150),  nullable = False)
    field13 = db.Column(db.Float(150),  nullable = False)
    field14 = db.Column(db.Float(150),  nullable = False)
    field15 = db.Column(db.Float(150),  nullable = False)
    field16 = db.Column(db.Float(150),  nullable = False)
    
    # menu_user = db.relationship("Menu", order_by="Menu.user_id", backref="user") # 외래키 관계 선언
    # rate_user = db.relationship("AttainmentRate", order_by="AttainmentRate.user_id", backref="user")

    
class Nutrition(db.Model) : # 음식 정보 테이블
    __tablename__ = 'nutrition' # table 이름
    food_seq = db.Column(db.Integer, primary_key=True) # food index와 같음
    foodname = db.Column(db.String(200), unique=True, nullable=True)
    category = db.Column(db.Float(150), nullable=False)
    gram = db.Column(db.Float(150), nullable = False)
    kcal = db.Column(db.Float(150), nullable = False)
    protein = db.Column(db.Float(150), nullable = False)
    fat = db.Column(db.Float(150), nullable = False)
    carbohydrate = db.Column(db.Float(150), nullable = False) # 탄수화물
    sodium = db.Column(db.Float(150),  nullable = False)

    # diet_Table1 = db.relationship("DietTable", order_by="DietTable.food_index1", backref="food_1") # 외래키 관계 선언
    # diet_Table2 = db.relationship("DietTable", order_by="DietTable.food_index2", backref="food_2")
    # diet_Table3 = db.relationship("DietTable", order_by="DietTable.food_index3", backref="food_3")
    # menu_Table = db.relationship("Menu", order_by="Menu.food_id", backref="menu_nut")
    

    
class DietTable(db.Model) : # 음식 조합 테이블
    __tablename__ = 'dietTable' # table 이름
    diet_seq = db.Column(db.Integer, primary_key=True)# food index와 같음
    food_index1 = db.Column(db.Integer, db.ForeignKey('nutrition.food_seq')) # 음식 정보 테이블의 인덱스와 관계설정 / 외래키
    food_index2 = db.Column(db.Integer, db.ForeignKey('nutrition.food_seq'))
    food_index3 = db.Column(db.Integer, db.ForeignKey('nutrition.food_seq'))
    kcal = db.Column(db.Float(150), nullable = False)
    protein = db.Column(db.Float(150), nullable = False)
    fat = db.Column(db.Float(150), nullable = False)
    carbohydrate = db.Column(db.Float(150), nullable = False) # 탄수화물
    sodium = db.Column(db.Float(150),  nullable = False)
    field1 = db.Column(db.Float(150),  nullable = False)
    field2 = db.Column(db.Float(150),  nullable = False)
    field3 = db.Column(db.Float(150),  nullable = False)
    field4 = db.Column(db.Float(150),  nullable = False)
    field5 = db.Column(db.Float(150),  nullable = False)
    field6 = db.Column(db.Float(150),  nullable = False)
    field7 = db.Column(db.Float(150),  nullable = False)
    field8 = db.Column(db.Float(150),  nullable = False)
    field9 = db.Column(db.Float(150),  nullable = False)
    field10 = db.Column(db.Float(150),  nullable = False)
    field11 = db.Column(db.Float(150),  nullable = False)
    field12 = db.Column(db.Float(150),  nullable = False)
    field13 = db.Column(db.Float(150),  nullable = False)
    field14 = db.Column(db.Float(150),  nullable = False)
    field15 = db.Column(db.Float(150),  nullable = False)
    field16 = db.Column(db.Float(150),  nullable = False)
    
    # food_1 = db.relationship("Nutrition", backref=db.backref('diet_Table1', order_by=food_index1))
    # food_2 = db.relationship("Nutrition", backref=db.backref('diet_Table2', order_by=food_index2))
    # food_3 = db.relationship("Nutrition", backref=db.backref('diet_Table3', order_by=food_index3))


class Menu(db.Model) : # 식단 정보 테이블
    __tablename__ = 'menu' # table 이름
    menu_seq = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.String(200), db.ForeignKey('user.userid'))
    food_id = db.Column(db.Integer, db.ForeignKey('nutrition.food_seq'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    meal_time = db.Column(db.Integer)
    image = db.Column(db.BLOB)
    
    # user = db.relationship("User", backref=db.backref('menu_user', order_by=user_id))
    # menu_nut = db.relationship("Nutrition", backref=db.backref('menu_Table', order_by=food_id))

    
class AttainmentRate(db.Model) : # 달성률 테이블
    __tablename__ = 'rate' # table 이름
    rate_seq = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.String(200), db.ForeignKey('user.userid'))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    A_rate = db.Column(db.Float(150),  nullable = False)
    kcal = db.Column(db.Float(150), unique=True, nullable = False)
    protein = db.Column(db.Float(150), nullable = False)
    fat = db.Column(db.Float(150), nullable = False)
    carbohydrate = db.Column(db.Float(150), nullable = False)
    sodium = db.Column(db.Float(150),  nullable = False)
    
    # user = db.relationship("User", backref=db.backref('rate_user', order_by=user_id))
    
class Image_file(db.Model) : # 달성률 테이블
    __tablename__ = 'image_file' # table 이름
    image_index = db.Column(db.Integer, primary_key=True) 
    image_binary = db.Column(db.BLOB)
