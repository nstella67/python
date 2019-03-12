#/section12/02-simple_http.py
#웹상의 데이터 가져오기
#모듈 설치
# pip install requests

import requests

#온라인 상의 text 파일 URL
simple_text_url="http://itpaper.co.kr/demo/python/simple_text.txt"

#특정 웹 페이지에 접속
r=requests.get(simple_text_url)

r.encoding="utf-8"      #인코딩 형식 지정
print(r.text)       #텍스트 출력

