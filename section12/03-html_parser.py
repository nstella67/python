#/section12/03-html_parser.py
#네이버 뉴스기사 가져오기
#모듈 설치 > pip install bs4

import requests                             #웹 페이지 요청 모듈
from bs4 import BeautifulSoup    #웹 페이지 소스코드 분석 모듈
from print_df import print_df

#sample.py에서 필요한 데이터 참조
from sample import naver_news_url   #가져올 뉴스의 URL
from sample import user_agent           #웹 브라우저 버전 정보

#데이터 수집 - 웹 페이지 HTML 소스코드 가져오기
#접속 세션을 생성
#세션 - 클라이언트(브라우저)와 서버(웹사이트) 간의 연결단위
#   → 이 객체에 접속에 필요한 기본 정보를 설정한다.
session=requests.Session()

#현재 세션의 referer 페이지를 '없음'으로 강제 설정
#   → referer : 이전에 머물렀던 페이지 주소
#   → referer 값이 없으면 웹 서버는 브라우저에서 직접 URL을 입력한 것으로 간주한다
#현재 세션의 웹 브라우저 정보(User-agent)를 구글 크롬으로 설정
session.headers.update({"referer":None, "User-agent":user_agent})

#특정 웹 페이지에 접속
#   → headers 파라미터로 가져올 컨텐츠의 형식을 미리 지정해 놓는다
r=session.get(naver_news_url)

#가져온 HTML 코드 확인
#   → 웹 페이지의 인코딩 형식을 확인하여 설정해야 한다
r.encoding="euc-kr"
print_df(r.text)


#데이터 전처리(1) - HTML을 분석하여 원하는 영역 추출

#웹 페이지의 소스코드 HTML 분석 객체로 생성
soup=BeautifulSoup(r.text, "html.parser")

#CSS 선택자를 활용하여 가져오기를 원하는 부분 지정
selector=soup.select("#articleBodyContents")
print_df(selector)


#데이터 전처리(2) - 추출된 영역 안에서 불필요한 태그 제거
for item in selector:
    for target in item.find_all("script"):
        target.extract()    #찾아낸 태그 삭제

    for target in item.find_all("a"):
        target.extract()
    
    for target in item.find_all("br"):
        target.extract()

    for target in item.find_all("span"):
        target.extract()

print_df(item)

print("-"*50)
#최종 결과값 확인
result_str=item.text.strip()
print(result_str)