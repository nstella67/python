#/section12/04-use_mod.py
#크롤러 모듈(Crawler.py) 사용하기
#   → 03-html_parser.py와 결과값 동일

#Crawler.py에 있는 75행 crawler 객체
from Crawler import crawler
from sample import naver_news_url

#가져올 페이지의 URL과 추출할 영역의 CSS 셀렉터를 지정한다
html=crawler.select(naver_news_url, encoding="euc-kr", selector="#articleBodyContents")

#크롤링 결과의 원소 수 만큼 반복하면서 불필요한 태그를 제거한다
for item in html:
    crawler.remove(item, "script")
    crawler.remove(item, "a")
    crawler.remove(item, "br")
    crawler.remove(item, "span")

#크롤링 처리된 최종 결과
print(item.text.strip())
