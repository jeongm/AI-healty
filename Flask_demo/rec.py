import pandas as pd
import sqlite3

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
    con = sqlite3.connect("C:\\Users\\user\\AI-healty\\Flask_demo\\test3.db")
    df = pd.read_sql("SELECT * FROM dietTable WHERE kcal BETWEEN "+str(uRDI*0.98)+" AND "+str(uRDI*1.02),con, index_col='diet_seq')
    user_W =  pd.read_sql("SELECT * FROM user WHERE userid="+ user_id,con, index_col='user_seq')
    for i in range(15):
        df[user_W.columns[i+9]]= df[user_W.columns[i+9]]*user_W.iloc[0][i+9]
    df['W'] = df.drop(['food_index1', 'food_index2', 'food_index3', 'kcal', 'protein', 'fat', 'carbohydrate', 'sodium'],axis=1).sum(axis=1)
    choice = df.sample(n=1,weights='W')

    return list(choice.iloc[0][0:3])