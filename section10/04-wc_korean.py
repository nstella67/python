# /section10/04-wc_korean.py
# Word Cloud 한글처리

from matplotlib import pyplot
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from collections import Counter         #빈도수 계산(파이선 기본)
from konlpy.tag import Okt              #한글 형태소 분석기
from PIL import Image
import numpy

text = ""
with open("section10/res/대한민국헌법.txt", "r", encoding="utf-8") as f:
    text = f.read()

#print(text)
#------------------------------------------------------------------------------------------------------------
#text 변수가 가지고 있는 내용을 기반으로 형태소 분석
#형태소 분석 클래스 객체 생성
nlp=Okt()
#명사들만 추출 → 리스트형식으로 반환
nouns=nlp.nouns(text)
#print(nouns)

#명사형태의 단어들만 뽑아서 리스트를 만들고 한 글자로 된 단어는 잘라냄 → 개인이 판단
words=[]
for n in nouns:
    if(len(n))>1:
        words.append(n)
#print(words)

#빈도수 계산
#Counter 객체를 통해 리스트 원소들의 빈도수 계산해서 딕셔너리값으로 반환
count=Counter(words)
#print(count)

#가장 많이 등장한 상위 100개 단어 추출
most=count.most_common(100)
#print(most)

#WordCloud 객체가 요구하는 형식으로 딕셔너리를 직접 구성
tags={}
for n, c in most:
    tags[n]=c
#print(tags)

#수집결과를 활용하여 워드클라우드 생성
#한글 워드클라우드를 작성하는 경우 글꼴 이름 확인할 것
wc=WordCloud(font_path="NanumGothic", width=1200, height=800, scale=2.0, max_font_size=250)

gen=wc.generate_from_frequencies(tags)
pyplot.figure()
pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("korean.png")
pyplot.close()

