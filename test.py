import requests
import json
from io import BytesIO
from zipfile import ZipFile
from xml.etree.ElementTree import parse
import pandas as pd

#API,출력 고유번호,회사명
url='https://opendart.fss.or.kr/api/corpCode.xml'
param={'crtfc_key':'60683bf2eba171b346f957c54dfa5d0c6defdacb'}
res= requests.get(url,param)
with ZipFile(BytesIO(res.content)) as zipfile:
    zipfile.extractall('./p3_app/static/')
xmlTree = parse('./p3_app/static/CORPCODE.xml')
root = xmlTree.getroot()
list = root.findall('list')
#print(list[0].findtext('corp_code'))
#print(list[0].findtext('corp_name'))
for i in range(len(list)):
    if list[i].findtext('corp_name')=='삼성전자':
        print(i)
        code=list[i].findtext('corp_code')


#API,출력 업종코드, 정식명칭, 영문명칭
url='https://opendart.fss.or.kr/api/company.json'
param={'crtfc_key':'60683bf2eba171b346f957c54dfa5d0c6defdacb', 'corp_code':code}
res= requests.get(url,param)
parsed_data = json.loads(res.text)
a=int(parsed_data['induty_code'])
b=parsed_data['corp_name']
c=parsed_data['corp_name_eng']
print(a)

#저장해둔 산업분류csv파일
csv = pd.read_csv('./p3_app/static/industrytable.csv')
print(csv.loc[csv['표준산업분류']==a])

#API,공시검색 출력 고유번호 접수번호
url='https://opendart.fss.or.kr/api/list.json'
param={'crtfc_key':'60683bf2eba171b346f957c54dfa5d0c6defdacb', 'corp_code':code, 'bgn_de':'20150101', 'page_count':'100'}
res= requests.get(url,param)
parsed_data = json.loads(res.text)

print(parsed_data)
#API, 재무재표


