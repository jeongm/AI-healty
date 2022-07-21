import pandas as pd
import sqlite3
import datetime
import numpy as np

# 일일 섭취 에너지 권장량 계산 BMR = 기초대사량 // RDI 일일권장섭취량
def getRDI(age,stat,weight,sex,acti):
    bmr = (10*weight) + (6.25*stat) - (5*age)
    if sex=='M':
        bmr = bmr + 5
    else:
        bmr = bmr -161
    
    if acti ==1:
        return bmr * 1.2
    elif acti ==2:
        return bmr * 1.375
    elif acti ==3:
        return bmr * 1.55
    elif acti ==4:
        return bmr * 1.725
    elif acti ==5:
        return bmr * 1.9

def getNut(uRDI):
    result = []
    result.append(round((uRDI*0.4)/4, 3))
    result.append(round((uRDI*0.4)/4, 3))
    result.append(round((uRDI*0.4)/9, 3))
    
    return result

def getMenu(uRDI, user_id):
    con = sqlite3.connect("test3.db" , check_same_thread=False)

    df = pd.read_sql("SELECT * FROM dietTable WHERE kcal BETWEEN "+str(uRDI*0.98)+" AND "+str(uRDI*1.02),con, index_col='diet_seq')
    user_W =  pd.read_sql("SELECT * FROM user WHERE userid="+ user_id,con, index_col='user_seq')
    for i in range(15):
        df[user_W.columns[i+9]]= df[user_W.columns[i+9]]*user_W.iloc[0][i+9]
    df['W'] = df.drop(['food_index1', 'food_index2', 'food_index3', 'kcal', 'protein', 'fat', 'carbohydrate', 'sodium'],axis=1).sum(axis=1)
    choice = df.sample(n=1,weights='W')
    con.close()
    return list(choice.iloc[0][0:3])

def getMealtime(userID, date, Mealtime):
    con = sqlite3.connect("test3.db" , check_same_thread=False)

    df = pd.read_sql("SELECT nutrition.foodname, nutrition.gram, nutrition.kcal, nutrition.protein, nutrition.fat, nutrition.carbohydrate, nutrition.sodium, menu.date FROM nutrition, menu WHERE menu.food_id=nutrition.food_seq AND menu.Meal_time="+str(Mealtime)+" AND menu.user_id="+str(userID), con)
    con.close()
    df = df[df['date']==date]
    result = []
    for i in range(len(df)):
        result.append(list(df.iloc[i].values))

    return result

def getRate(userID, nut, uRDI, date):
    con = sqlite3.connect("test3.db" , check_same_thread=False)
    df = pd.read_sql("SELECT nutrition.foodname, nutrition.gram, nutrition.kcal, nutrition.protein, nutrition.fat, nutrition.carbohydrate, nutrition.sodium, menu.date FROM nutrition, menu WHERE menu.food_id=nutrition.food_seq AND menu.user_id="+str(userID), con)
    con.close()
    result = [0,0,0,0,0]
    df = df[df['date']==date]

    if len(df)<1:
        return result

    for i in range(len(df)):
        if df.iloc[i][2] != '-':
            result[0] = round(result[0] + float(df.iloc[i][2]),3)
        if df.iloc[i][5] != '-':
            result[1] = round(result[1] + float(df.iloc[i][5]),3)
        if df.iloc[i][3] != '-':
            result[2] = round(result[2] + float(df.iloc[i][3]),3)
        if df.iloc[i][4] != '-':
            result[3] = round(result[3] + float(df.iloc[i][4]),3)
        if df.iloc[i][6] != '-':
            result[4] = round(result[4] + float(df.iloc[i][6]),3)
    nut.append(2300)
    nut = [uRDI]+nut
    rate = []
    for i in range(5):
        rate.append(round(result[i]/nut[i]*100,3))
    rate = rate+result
    return rate

def getTotalRate(userID, nut, uRDI):
    con = sqlite3.connect("test3.db" , check_same_thread=False)
    df = pd.read_sql("SELECT nutrition.foodname, nutrition.gram, nutrition.kcal, nutrition.protein, nutrition.fat, nutrition.carbohydrate, nutrition.sodium, menu.date FROM nutrition, menu WHERE menu.food_id=nutrition.food_seq AND menu.user_id="+str(userID),con)
    con.close()
    
    result = [0,0,0,0,0]
    for i in range(len(df)):
        if df.iloc[i][2] != '-':
            result[0] = round(result[0] + float(df.iloc[i][2]),3)
        if df.iloc[i][5] != '-':
            result[1] = round(result[1] + float(df.iloc[i][5]),3)
        if df.iloc[i][3] != '-':
            result[2] = round(result[2] + float(df.iloc[i][3]),3)
        if df.iloc[i][4] != '-':
            result[3] = round(result[3] + float(df.iloc[i][4]),3)
        if df.iloc[i][6] != '-':
            result[4] = round(result[4] + float(df.iloc[i][6]),3)
    nut.append(2300)
    nut = [uRDI]+nut
    rate = []
    for i in range(5):
        rate.append(round(result[i]/nut[i]*100,3))
    rate = np.array(rate)
    rate = rate/len(df['date'].value_counts())
    rate = list(rate)
    rate = rate+result
    return rate