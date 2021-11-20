This(P3) is a **web application** showing information of Korean companies.

P3 has 3 web pages.   
**The first page** has searching bar which searches given company name from database   
and also has Dude button for who don't know his/her company name.   
Dude button shows categories of company.   
Any dude clicking a category is sent to third page.   
and there is another dude button for who don't know her/his company category.   
The second dude button shows a disappointed face.   
**Second page** shows information of searched company, that includes trends, features compared with mean value of similar companies.   
**Third page** shows a list of companies which is similar to searched company.

![Alt text](/blueprint.png)


used tools   
python   
flask : micro web framework(python library)   
API : dart API   
database :    
beautiful soup : web scrapping(python library)

[dart API](https://opendart.fss.or.kr/guide/main.do?apiGrpCd=DS001)   

database

유저에게 기업명을 받으면
검색어 정리 후

데이터베이스 존재하지 않으면 고유번호 데이터베이스를 api로 전부 받고 기업개황데이터베이스에 전부 검색하여 업종코드얻기
데이터베이스에 기업명을 검색 후 없으면 api로 고유번호, 업종코드 받아서 데이터베이스에 추가

1 공시검색 api로 검색회사 고유번호로 정보 가져오기
2 업종코드로 데이터베이스 검색 후 고유번호로 동종업계회사들 정보 가져오기
3 회사정보에 필요한 정보 : 인증키 고유번호 사업연도 보고서코드
단일회사정보로는 최근5년 가져오고(유사시 최우선 삭제)
업종회사정보로는 가장 최근 것으로

가져온 정보를 데이터베이스에 만들어둠. 이것은 용량 부족시 필요없는것 삭제(API요청, 웹스크래핑을 최소화하자)
(현재 작업중인 업종이 아닌 업종 중에서 삭제)

즉 만들어둘 데이터베이스는

1 고유번호+업종코드+회사명 데이터베이스
2 업종별기업정보 데이터베이스
3 단일기업정보 데이터베이스

feature
1 성장성 : 매출그래프, 업계평균비교
1.1 비유동자산의 유형자산 그래프, 업계평균비교
2 재무건전성
부채비율 = 부채/자본, 업계평균 비교, 보통 100%이하 건전
2.1 유동비율=유동자산/유동부채, 업계평균비교, 보통 200%이상 건전
3 수익성
ROE = 당기순이익/자기자본, 업계평균비교, 높을수록 좋음
3.1 매출액순이익률=당기순이익/매출액, 업계평균비교, 높을수록 좋음
4 업계트렌드, 타업계트렌드와 비교
	
크레딧잡 : 신입,경력 연봉정보 가져오기

CRUD
Create : 유저가 회사명 검색 시 같은 업종회사 모아서 db생성
Read : 어디에나있다
Update : 검색한 회사가 데이터베이스에 없는데 검색해서 있을 경우 데이터베이스에 추가
Delete : 유저가 회사명 검색 시 딜리트 올 하고 시작

해석
같은 업종 회사로 머신러닝 vs 모든 회사 머신러닝

전자는 데이터수가 적은 경우가 생김 -> 그래도 간단한 머신러닝은 가능함
입력값에 따른 결과를 줘야함 -> 4번째 페이지 생성
binary값 feature를 정해야함 -> 가공된 feature 4개? 시간변수있음
선형회귀는? 성장성 체크 가능 -> 최후의수단(공시정보가 별로 없는 경우가 많음)
회사를 입력 -> 

모든 회사 머신러닝 -> '회사'의 성격 도출 인원이 많아질수록~ 이라던가
그런데 유저정보를 받아 결론을 만드는거랑 관련없음
만들 수 있는것 -> 업종별로 최근 트렌드

어떤 회사 검색했을 때 같은업종의 더 좋은회사 추천?
추천알고리즘
사용자의 행동 로그(behavior log) 데이터가 필요하며, 그 분석을 통해 사용자의 호감도를 조사한다. 
머신러닝을 하면 이렇겠지만
타유저데이터를 기반으로 해야하고
내가하려는건 기업데이터고
내유저데이터도 고작 회사 한두개임 이직을 한달에 한번하는게 아니니까
그냥 적당히 넣고 추천


-----------------------------------------------------
Open DART 홈페이지 오픈API 서비스의 일일한도는 다음과 같습니다.   

1. 개인 : 일 10,000건 (서비스별 한도가 아닌 오픈API 23종 전체 서비스 기준)   

2. 기업(사업자등록증 및 IP 등록)   
1) 공시목록, 기업개황 2종 : 한도 없음(기존 DART홈페이지 오픈API와 동일)   
2) 공시원문, 사업보고서 주요정보 등 신규서비스 21종 : 일 10,000(서비스별 한도가 아닌 21종 서비스 전체 기준)   

* 일일한도를 준수하더라도 서비스의 안정적인 운영을 위하여 과도한 네트워크 접속(분당 1000회 이상)은 서비스 이용이 제한될 수 있으니 이용에 참고하시기 바랍니다.
