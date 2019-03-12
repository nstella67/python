#/section12/05-news_crawler.py
#네이버 뉴스 크롤러


from Crawler import crawler
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from matplotlib import pyplot
from pandas import ExcelFile
from pandas import DataFrame
from collections import Counter
from konlpy.tag import Okt
from print_df import print_df

#1) 접속 조건 설정하기
URL="http://news.naver.com"
url_list=[]     #뉴스기사의 본문 URL을 저장할리스트

#2) 수집할 뉴스기사의 URL조사하기
#가져온 URL에서 링크에 대한 셀렉터를 크롤링. 반환결과는 list 형태
#   → 여러 형식의 셀렉터를 동시에 처리해야 할 경우 콤마(,)로 구분하여 지정한다
link_list=crawler.select(URL, encoding="euc-kr", selector=".newsnow_tx_inner>a, .newsnow_imgarea>a, .mtype_img>dt>a, mlist2>li>a")

#가져온 결과 확인하기
for item in link_list:
    print(item)
    print("-"*30)

#리스트의 원소들에 대한 반복 처리
for item in link_list:
    print(type(item.attrs))
    #각 원소(링크)에 속성들(attrs) 중에 href 속성이 있다면 그 속성값을 별도로 준비한 리스트에 추가
    if "href" in item.attrs:
        #href 속성은 링크를 클릭했을 때의 URL을 의미
        #URL에 뉴스 상세 페이지의 파일명인 "read.nhn"이 포함되어 있다면 해당 주소를 url_list에 추가
        if "read.nhn" in item["href"]:
            url_list.append(item["href"])

#집계된 리스트의 주소들 확인하기
for v in url_list:
    print(v)


#3) 뉴스기사에 접속하여 본문 크롤링 하기
print("="*50)
print("뉴스기사 크롤링 시작>>총 %d개의 기사를 수집합니다." %len(url_list))
print("="*50)

#기사의 본문을 누적해서 저장할 문자열 변수
news_content=""

#URL 목록만큼 반복
for i, url in enumerate(url_list):
    print("%d번째 뉴스기사 수집중...>>%s" %(i+1, url))

    #URL에 접근하여 뉴스 컨텐츠를 가져온다
    news_html=crawler.select(url, selector="#articleBodyContents", encoding="euc-kr")

    if not news_html:       #가져올 내용이 없다면?
        print("%d번째 뉴스기사 크롤링 실패" %(i+1))
    else:       #가져올 내용이 있다면
        print("%d번째 뉴스기사 크롤링 성공" %(i+1))
        #수집결과에서 불필요한 HTML 태그 제거
        for item in news_html:
            crawler.remove(item, "script")
            crawler.remove(item, "a")
            crawler.remove(item, "br")
            crawler.remove(item, "span", {"class":"end_photo_org"})

            #공백을 제거한 텍스트만 미리 준비한 변수에 누적
            news_content += item.text.strip()

#4) 수집결과를 기반으로 형태소 분석
#형태소 분석 객체를 통해 수집된 뉴스 본문에서 명사만 추출
nlp=Okt()
nouns=nlp.nouns(news_content)

#명사들에 대한 빈도수 검사
count=Counter(nouns)

#가장 많이 사용된 단어 100개 추출
most=count.most_common(100)

#추출 결과를 워드클라우드에서 요구하는 형식으로 재구성
#   → {"단어":빈도수, "단어":빈도수, ...}
tags={}
lists=[]
for n, c in most:
    if len(n)>1:
        tags[n]=c
        lists.append([n, c])
df=DataFrame(lists, columns=["단어", "빈도수"])
print_df(df)
df.to_excel("helloworld.xlsx", encoding="utf-8", sheet_name="단어빈도수", index=False)


#5) 수집결과를 활용하여 워드클라우드 생성
#워드클라우드 객체 만들기
wc=WordCloud(font_path="NanumGothic", max_font_size=200, width=1200, height=800, scale=2.0, background_color="#d8d8d8")

#미리 준비한 딕셔너리를 통해 생성
gen=wc.generate_from_frequencies(tags)

#워드 클라우드 이미지 저장
pyplot.figure()
pyplot.imshow(gen, interpolation="bilinear")
pyplot.axis("off")
# wc.to_file("section12/news.png")
pyplot.show()
pyplot.close()




