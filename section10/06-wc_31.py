# /section10/06-wc_31.py

from matplotlib import pyplot
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy

text = ""
with open("section10/res/기념사.txt", "r", encoding="utf-8") as f:
    text = f.read()

nlp=Okt()
nouns=nlp.nouns(text)

words=[]
for n in nouns:
    if(len(n))>1:
        words.append(n)

count=Counter(words)

most=count.most_common(100)

tags={}
for n, c in most:
    tags[n]=c

wc=WordCloud(font_path="NanumGothic", width=1200, height=800, scale=2.0, max_font_size=250, background_color="#ffcece")

gen=wc.generate_from_frequencies(tags)
pyplot.figure()
pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("speech31.png")
pyplot.close()

