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
	
