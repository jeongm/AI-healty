# database 관련
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
#db = SQLAlchemy(Base) # SQLALchemy를 사용해 데이터베이스 저장

class User(Base) : # user 테이블
    __tablename__ = 'user' # table 이름
    user_seq = Column(Integer, primary_key=True)
    userid = Column(String(200), unique=True, nullable=True) # id는 email형식으로 받자
    password = Column(String(200), nullable=False)
    username = Column(String(150), nullable = False)
    phone = Column(String(150), unique=True, nullable = False)
    age = Column(Integer, nullable = False)
    sex = Column(String(2), nullable = False)
    height = Column(Float(150), nullable = False)
    weight = Column(Float(150),  nullable = False)
    field1 = Column(Float(150),  nullable = False)
    field2 = Column(Float(150),  nullable = False)
    field3 = Column(Float(150),  nullable = False)
    field4 = Column(Float(150),  nullable = False)
    field5 = Column(Float(150),  nullable = False)
    field6 = Column(Float(150),  nullable = False)
    field7 = Column(Float(150),  nullable = False)
    field8 = Column(Float(150),  nullable = False)
    field9 = Column(Float(150),  nullable = False)
    field10 = Column(Float(150),  nullable = False)
    field11 = Column(Float(150),  nullable = False)
    field12 = Column(Float(150),  nullable = False)
    field13 = Column(Float(150),  nullable = False)
    field14 = Column(Float(150),  nullable = False)
    field15 = Column(Float(150),  nullable = False)
    field16 = Column(Float(150),  nullable = False)
    
    menu_user = relationship("Menu", order_by="Menu.user_id", backref="user") # 외래키 관계 선언
    rate_user = relationship("AttainmentRate", order_by="AttainmentRate.user_id", backref="user")

    
class Nutrition(Base) : # 음식 정보 테이블
    __tablename__ = 'nutrition' # table 이름
    food_seq = Column(Integer, primary_key=True) # food index와 같음
    foodname = Column(String(200), unique=True, nullable=True)
    category = Column(Float(150), nullable=False)
    gram = Column(Float(150), unique=True, nullable = False)
    kcal = Column(Float(150), unique=True, nullable = False)
    protein = Column(Float(150), nullable = False)
    fat = Column(Float(150), nullable = False)
    carbohydrate = Column(Float(150), nullable = False)
    sodium = Column(Float(150),  nullable = False)

    diet_Table1 = relationship("DietTable", order_by="DietTable.food_index1", backref="food_1") # 외래키 관계 선언
    diet_Table2 = relationship("DietTable", order_by="DietTable.food_index2", backref="food_2")
    diet_Table3 = relationship("DietTable", order_by="DietTable.food_index3", backref="food_3")
    menu_Table = relationship("Menu", order_by="Menu.food_id", backref="menu_nut")
    
    
class DietTable(Base) : # 음식 조합 테이블
    __tablename__ = 'dietTable' # table 이름
    diet_seq = Column(Integer, primary_key=True)# food index와 같음
    food_index1 = Column(Integer, ForeignKey('nutrition.food_seq')) # 음식 정보 테이블의 인덱스와 관계설정 / 외래키
    food_index2 = Column(Integer, ForeignKey('nutrition.food_seq'))
    food_index3 = Column(Integer, ForeignKey('nutrition.food_seq'))
    field1 = Column(Float(150),  nullable = False)
    field2 = Column(Float(150),  nullable = False)
    field3 = Column(Float(150),  nullable = False)
    field4 = Column(Float(150),  nullable = False)
    field5 = Column(Float(150),  nullable = False)
    field6 = Column(Float(150),  nullable = False)
    field7 = Column(Float(150),  nullable = False)
    field8 = Column(Float(150),  nullable = False)
    field9 = Column(Float(150),  nullable = False)
    field10 = Column(Float(150),  nullable = False)
    field11 = Column(Float(150),  nullable = False)
    field12 = Column(Float(150),  nullable = False)
    field13 = Column(Float(150),  nullable = False)
    field14 = Column(Float(150),  nullable = False)
    field15 = Column(Float(150),  nullable = False)
    field16 = Column(Float(150),  nullable = False)
    
    food_1 = relationship("Nutrition", backref=backref('diet_Table1', order_by=food_index1))
    food_2 = relationship("Nutrition", backref=backref('diet_Table2', order_by=food_index2))
    food_3 = relationship("Nutrition", backref=backref('diet_Table3', order_by=food_index3))


class Menu(Base) : # 식단 정보 테이블
    __tablename__ = 'menu' # table 이름
    menu_seq = Column(Integer, primary_key=True) 
    user_id = Column(String(200), ForeignKey('user.userid'))
    food_id = Column(Integer, ForeignKey('nutrition.food_seq'))
    date = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", backref=backref('menu_user', order_by=user_id))
    menu_nut = relationship("Nutrition", backref=backref('menu_Table', order_by=food_id))

    
class AttainmentRate(Base) : # 달성률 테이블
    __tablename__ = 'rate' # table 이름
    rate_seq = Column(Integer, primary_key=True) 
    user_id = Column(String(200), ForeignKey('user.userid'))
    date = Column(DateTime, default=datetime.utcnow)
    A_rate = Column(Float(150),  nullable = False)
    kcal = Column(Float(150), unique=True, nullable = False)
    protein = Column(Float(150), nullable = False)
    fat = Column(Float(150), nullable = False)
    carbohydrate = Column(Float(150), nullable = False)
    sodium = Column(Float(150),  nullable = False)
    
    user = relationship("User", backref=backref('rate_user', order_by=user_id))
