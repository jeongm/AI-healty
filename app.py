# -*- coding: utf-8 -*-
from tkinter import N
from flask import Flask, session, render_template, redirect, request, url_for, flash
from pandas import to_datetime
from werkzeug.utils import secure_filename
from db_models import db
import os
from db_models import User, Nutrition, DietTable, Menu, AttainmentRate, Image_file # db_models.py에 있는 User 클래스
import rec 
from datetime import date, datetime

#import argparse
import io
import os
from PIL import Image

import torch


app = Flask(__name__)
app.secret_key = "abcdef"

cls_dic = {'0': '와플', '1': '케이크', '2': '핫도그', '3': '시리얼바', '4': '바나나', '5': '사과', '6': '수박', '7': '아보카도', '8': '오렌지', '9': '참외', '10': '파인애플', '11': '포도', '12': '키위', '13': '고구마', '14': '시리얼', '15': '팝콘', '16': '두부', '17': '방울토마토', '18': '상추', '19': '오이', '20': '파프리카', '21': '풋고추', '22': '조미김', '23': '삶은달걀', '24': '닭가슴살', '25': '훈제오리', '26': '훈제치킨', '27': '모듬회', '28': '생선회', '29': '전복', '30': '새우', '31': '베이컨', '32': '소시지', '33': '햄', '34': '소시지', '35': '소시지', '36': '밥', '37': '비빔밥', '38': '알밥', '39': '육회비빔밥', '40': '김치볶음밥', '41': '달걀볶음밥', '42': '볶음밥', '43': '새우볶음밥', '44': '카레라이스', '45': '햄볶음밥', '46': '김밥', '47': '주먹밥', '48': '초밥', '49': '연어롤', '50': '장어초밥', '51': '초밥', '52': '순대국밥', '53': '오므라이스', '54': '리조또', '55': '피자', '56': '피자', '57': '피자', '58': '피자', '59': '피자', '60': '피자', '61': '샌드위치', '62': '샌드위치', '63': '샌드위치', '64': '샌드위치', '65': '국수', '66': '비빔국수', '67': '쌀국수', '68': '냉면', '69': '비빔냉면', '70': '라면', '71': '컵라면', '72': '까르보나라', '73': '봉골레파스타', '74': '스파게티', '75': '크림파스타', '76': '파스타', '77': '우동', '78': '나가사끼짬뽕', '79': '라멘', '80': '짜장면', '81': '짬뽕', '82': '만두', '83': '떡만두국,고기만두', '84': '만두', '85': '만두', '86': '미소장국', '87': '갈비탕', '88': '삼계탕', '89': '어묵국', '90': '해장국', '91': '미역국', '92': '김치찌개', '93': '된장찌개', '94': '어묵국', '95': '추어탕', '96': '해물탕', '97': '부대찌개', '98': '순두부찌개', '99': '아귀찜', '100': '갈비찜', '101': '닭찜(찜닭)', '102': '돼지갈비찜', '103': '보쌈', '104': '순대', '105': '순살찜닭', '106': '달걀찜', '107': '고구마', '108': '고등어구이', '109': '고등어구이', '110': '새우구이', '111': '생선구이', '112': '연어구이', '113': '장어구이', '114': '갈비구이', '115': '닭가슴살', '116': '돼지고기고추장불고기', '117': '삼겹살', '118': '스테이크', '119': '오리구이', '120': '치킨스테이크', '121': '함박스테이크', '122': '고구마', '123': '타코야키', '124': '떡갈비', '125': '달걀말이', '126': '달걀후라이', '127': '부침개', '128': '스크램블드에그', '129': '파전', '130': '떡볶이', '131': '잡채', '132': '감자채볶음', '133': '쭈꾸미볶음', '134': '닭갈비', '135': '제육볶음', '136': '쇠고기볶음', '137': '족발', '138': '새우튀김', '139': '닭강정', '140': '순살치킨', '141': '양념치킨', '142': '왕돈가스', '143': '치킨', '144': '치킨너겟', '145': '치킨', '146': '파닭', '147': '핫윙', '148': '후라이드치킨', '149': '후라이드치킨,날개', '150': '후라이드치킨,다리', '151': '감자튀김', '152': '회오리감자', '153': '치즈스틱', '154': '모듬튀김', '155': '치즈볼', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '156': '샐러드', '157': '무김치', '158': '육회', '159': '참치통조림'}
checkbox_dic = {'0':'15', '1':'8','2':'1','3':'10','4':'8','5':'5','6':'12','7':'6','8':'6','9':'3','10':'13','11':'11','12':'10','13':'11','14':'7','15':'4','16':'12','17':'0','18':'9','19':'7','20':'14','21':'6','22':'2','23':'5','24':'0','25':'14','26':'13','27':'0','28':'3','29':'6','30':'12','31':'9','32':'1'}

@app.route('/')  # main페이지 -logout 상태
def index():
    if "userid" in session: # 로그인 여부 확인
        return render_template('indexout.html')
    return render_template('index2_copy.html')

# GET => 페이지가 나오도록 요청. POST = 버튼을 눌렀을 때 데이터를 가지고오는 요청, 요청정보를 확인하기 위해 request 모듈 사용
@app.route('/join',methods = ['GET','POST']) # 회원가입
def join():
    if request.method == 'GET':
        return render_template('join_copy.html')
    else : # form 데이터 가져옴, POST, post는 http요청 메시지에서 body에 데이터를 담아 보냄
        # db전송
        user = User()
        user.userid = request.form.get('id') # get으로 전달된 데이터?? get은 url에 query string로 데이터가 넘어옴
        user.password = request.form.get('password')
        user.username = request.form.get('user_name')
        user.phone = request.form.get('phone_num')
        user.age = request.form.get('age')
        user.sex = request.form.get('SEX1')
        user.height = request.form.get('height')
        user.weight = request.form.get('weight')
        user.acti = request.form.get('activity')
        field = request.form.getlist('circle_txt') # 음식값을 한글로 가져오고 싶으면 value를 한글로주면 됨
        
        field_list = [1.0]*16
        for i in field:
            field_list[int(checkbox_dic[i])] = field_list[int(checkbox_dic[i])] * 1.5
        user.field1 = field_list[0]
        user.field2 = field_list[1]
        user.field3 = field_list[2]
        user.field4 = field_list[3]
        user.field5 = field_list[4]
        user.field6 = field_list[5]
        user.field7 = field_list[6]
        user.field8 = field_list[7]
        user.field9 = field_list[8]
        user.field10 = field_list[9]
        user.field11 = field_list[10]
        user.field12 = field_list[11]
        user.field13 = field_list[12]
        user.field14 = field_list[13]
        user.field15 = field_list[14]
        user.field16 = field_list[15]

        db.session.add(user)
        db.session.commit()
        flash("회원가입이 완료되었습니다.")
        return redirect(url_for('index')) 

@app.route('/signin', methods=['GET', 'POST']) # 로그인
def signin():
    if request.method == 'GET':
        return render_template('signin.html')
    else : # POST
        userid = request.form['id'] 
        password = request.form['pw']
        data = User.query.filter_by(userid=userid, password=password).first() # ID/PW조회 Query 실행
        
        if data is not None: # 쿼리 데이터 존재시
            session['userid'] = userid # userid를 session에 저장
            return redirect(url_for('diary'))
        else:
            flash("로그인 실패.")
            return render_template('signin.html')
        

@app.route('/signout', methods=['GET']) # 로그아웃
def signout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/mypage') # 회원정보
def mypage():
    userinfo = User.query.filter_by(userid=session['userid']).first()
    return render_template("mypage.html",userInfo = userinfo)

@app.route('/diary', methods = ['GET', 'POST']) # 오늘 먹은 음식 확인, 로그인하면 
def diary(): # db 불러오자
    if request.method == "POST":
        
        m_dict = request.form
        data_key = list(m_dict.keys())
        action = request.form["current"]

        if action == "확인":
            diarydate = m_dict['date']
            Mealtime = m_dict['name']
            menu = rec.getMealtime(session['userid'], diarydate, m_dict['name'])
            if len(menu) <1:
                return render_template('diary_copy.html')
            data = User.query.filter_by(userid=session['userid']).first()
            uRDI = rec.getRDI(data.age, data.height, data.weight, data.sex, data.acti)
            nut = rec.getNut(uRDI)
            rate = rec.getRate(session['userid'], nut, uRDI, diarydate)
            img_path = Menu.query.filter_by(user_id=session['userid'], date=diarydate, meal_time=Mealtime).first().image_path
            
            return render_template('diary_chart.html', day = diarydate, Meal=Mealtime, rate=rate, nut=nut, menu= menu, img_path=img_path)
        
    return render_template('diary_copy.html')

@app.route('/write', methods = ['GET', 'POST']) 
def write(): # db식단 기록
    if request.method == "POST":
        m_dict = request.form
        data_key = list(m_dict.keys())
        action = request.form['write']
        if action == "SUBMIT":
            dict = m_dict.to_dict(flat=False)
            writedate = m_dict['date/']
            
            if 'name' not in dict:
                flash('아침, 점심, 저녁을 선택해주세요')
                return render_template("write_copy.html")
            if 'chck' in dict : # 메뉴만 따로 기록
                menu_list = dict['chck']
            elif 'foodname' in dict:
                menu_list = dict['foodname']
            
            for foodname in menu_list:
                menu = Menu()
                img = Image_file.query.order_by(Image_file.image_index.desc()).first()
                menu_id = Nutrition.query.filter_by(foodname=foodname).first()
                menu.user_id = session['userid']
                menu.food_id = menu_id.food_seq
                menu.date = writedate
                menu.meal_time = m_dict['name']
                menu.image_path = img.image_path
                db.session.add(menu)
                db.session.delete(img)
            db.session.commit()   
            flash("저장되었습니다.")
            
        else: 
            if action == "search":
                predict_data= predict()
                return render_template("write_copy.html", predict_data = predict_data)
            if "text-search" in data_key and m_dict['text-search'] != '':
                data = request.form["text-search"]
            elif "chck" in data_key:
                data = request.form['chck']
            food = Nutrition.query.filter_by(foodname=data).first()
            return render_template("write_copy.html", food = food)
    return render_template("write_copy.html")






@app.route('/recommend', methods = ['GET','POST']) # 식단추천페이지- 경민
def recommend():
    data = User.query.filter_by(userid=session['userid']).first()
    uRDI = rec.getRDI(data.age, data.height, data.weight, data.sex, data.acti)
    nut = rec.getNut(uRDI)
    mode='off'
    if request.method == 'POST':
        mode = request.form['mode']

    menu_list = rec.getMenu(uRDI, session['userid'],mode)
    
    menu1 = Nutrition.query.filter_by(food_seq=menu_list[0]).first()
    menu2 = Nutrition.query.filter_by(food_seq=menu_list[1]).first()
    menu3 = Nutrition.query.filter_by(food_seq=menu_list[2]).first()
    
    t_rate = rec.getTotalRate(session['userid'], nut, uRDI)
    rate = rec.getRate(session['userid'], nut, uRDI, str(date.today()))

    return render_template('recommend.html', uRDI = round(uRDI, 3), nut = nut , menu_list=len(menu_list), menu1 = menu1, menu2 = menu2, menu3 = menu3, t_rate=t_rate, rate= rate)


@app.route('/search', methods = ['GET','POST']) # search 기본페이지
def search_info():
    if "userid" in session: # 로그인 여부 확인
        se = session['userid']
    else :
        se = None
    if request.method == "POST":
        key_dict = request.form
        if not key_dict :
            return render_template("search_copy.html",se= se)
        data_key = list(key_dict.keys())
        # 텍스트 => text-search
        # 이미지 => ['text-search', 'file']
        # return render_template("test.html",data = key_dict)
        
        if "file" in data_key :
            predict_data = predict()
            return render_template("search_copy.html", predict_data = predict_data)
        if "chck" in data_key:
            data = request.form['chck']
        else:
            data = request.form["text-search"]
        
        food = Nutrition.query.filter(Nutrition.foodname.like("%"+data+"%")).first()
        # food = Nutrition.query.filter_by(foodname=data).first()
        
        return render_template("search_copy.html",se=se, food = food)
    return render_template("search_copy.html",se= se)
    

@app.route("/predict", methods=['GET','POST']) # 이미지 detection
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        image_file = Image_file()
        img_bytes = file.read() # yolo detction
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=640)
        #dataframe으로 가져옴
        now = datetime.now()
        save_to = 'static/images/menu_img/'+str(now.microsecond)+".png"
        img.save(save_to)
        image_file.image_path = save_to
        db.session.add(image_file)
        db.session.commit()

        data = results.pandas().xyxy[0]["name"]
        data_list = data.tolist()
        data_value = []
        for key, value in cls_dic.items(): # 한글매칭
            if key in data_list:
                data_value.append(value)
        if not data_value:
            return ""
        return data_value

    return render_template("search_copy.html")


if __name__ == '__main__':
    basedir = os.path.abspath(os.path.dirname(__file__)) # database 경로를 절대경로로 설정
    dbfile = os.path.join(basedir, 'test3.db') # 데이터베이스 이름과 경로
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 사용자에게 원하는 정보를 전달완료했을 떄가 TEARDOWN, 그 순간마다 COMMIT을 하도록 함=db반영
    # 여러가지 쌓아져있던 동작들을 Commit을 해주어야 데이터베이스에 반영됨. 이러한 단위들을 트렌젝션 이라고 함
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # True하면 warning 메시지 유발, 추가 메모리를 사용하므로 꺼둔다
    
    db.init_app(app) # app설정값 초기화
    db.app = app # Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
    db.create_all() # DB생성
    
    #parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    #parser.add_argument("--port", default=5000, type=int, help="port number")
    #args = parser.parse_args()
    
    # yolo
    '''
    model = torch.hub.load(
        "ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True, autoshape=True
    )  # force_reload = recache latest code
    model.eval()
    '''
    
    model = torch.hub.load(
        'yolov5', 'custom', path='exp8_56epoch.pt', source='local', force_reload=True, autoshape=True
    )  # force_reload = recache latest code
    model.eval()
    
    app.run(host='127.0.0.1', port=5000, debug=True)
    #app.run(host="0.0.0.0", port=args.port, debug=True)  # debug=True causes Restarting with stat









# yolov5 모델 적용
# https://github.com/ultralytics/yolov5/issues/36
# https://github.com/ultralytics/yolov5/issues/36
# https://cdnjs.com/libraries/font-awesome
# query 관련
# https://sejin0134.tistory.com/54