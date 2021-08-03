from flask import Blueprint, render_template
#from p3_app import CSV_FILEPATH
import csv
from p3_app.models import Key_model, Corp_model, Ind_model
import os
from p3_app import db

import requests
import json
from io import BytesIO
from zipfile import ZipFile
from xml.etree.ElementTree import parse
import pandas as pd


main_bp = Blueprint('main', __name__)
CSV_FILEPATH='./p3_app/static/industrytable.csv'
@main_bp.route('/', methods=['GET','POST'])
def index():

    if Ind_model.query.limit(1).all() ==False:
        iList=[]
        with open(CSV_FILEPATH, encoding='UTF8') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                iList.append(row)
        for i in range(len(iList)):
            ind_add = Ind_model(ind_code=iList[i][0],iClass1=iList[i][1],iClass2=iList[i][2],iClass3=iList[i][3],iClass4=iList[i][4],iClass5=iList[i][5])
            db.session.add(ind_add)
            db.session.commit()
        for i in range(len(iList)):
            iList[i][0]=int(iList[i][0]/10)#세세분류 제거
            iList[i][5]=0
        iList = list(dict.fromkeys(iList))
        for i in range(len(iList)):
            ind_add = Ind_model(ind_code=iList[i][0],iClass1=iList[i][1],iClass2=iList[i][2],iClass3=iList[i][3],iClass4=iList[i][4])
            db.session.add(ind_add)
            db.session.commit()
        for i in range(len(iList)):
            iList[i][0]=int(iList[i][0]/10)#세분류제거
            iList[i][4]=0
        iList = list(dict.fromkeys(iList))
        for i in range(len(iList)):
            ind_add = Ind_model(ind_code=iList[i][0],iClass1=iList[i][1],iClass2=iList[i][2],iClass3=iList[i][3])
            db.session.add(ind_add)
            db.session.commit()
        for i in range(len(iList)):
            iList[i][0]=int(iList[i][0]/10)#소분류제거
            iList[i][3]=0
        iList = list(dict.fromkeys(iList))
        for i in range(len(iList)):
            ind_add = Ind_model(ind_code=iList[i][0],iClass1=iList[i][1],iClass2=iList[i][2])
            db.session.add(ind_add)
            db.session.commit()

    #db에서 고유번호 유무확인
    if Key_model.query.limit(1).all() ==False:
        #API,입력 : API키, 출력 : 고유번호,회사명
        url='https://opendart.fss.or.kr/api/corpCode.xml'
        param={'crtfc_key':'60683bf2eba171b346f957c54dfa5d0c6defdacb'}
        res= requests.get(url,param)
        with ZipFile(BytesIO(res.content)) as zipfile:
            zipfile.extractall('./p3_app/static/')
        xmlTree = parse('./p3_app/static/CORPCODE.xml')
        root = xmlTree.getroot()
        kList = root.findall('list')
        for i in range(len(kList)):
            key_add = Key_model(corp_code=kList[i].findtext('corp_code'), corp_name=kList[i].findtext('corp_name'))
            db.session.add(key_add)
            db.session.commit()

    #if corp_model.query.limit(1).all() ==False:
    #    keys=key_model.query.all()
#
    #    url='https://opendart.fss.or.kr/api/company.json'
    #    param={'crtfc_key':'60683bf2eba171b346f957c54dfa5d0c6defdacb', 'corp_code':code}
    #    res= requests.get(url,param)
    #    parsed_data = json.loads(res.text)
    #    a=int(parsed_data['induty_code'])
    #    b=parsed_data['corp_name']
    #    c=parsed_data['corp_name_eng']
    #    print(a)





    return render_template('main.html')