# /section10/02-wc_option.py
# Word Cloud 모듈옵션

from matplotlib import pyplot  # 그래프모듈
from wordcloud import WordCloud  # 워드클라우드모듈
#금지어 설정 모듈 참조하기
from wordcloud import STOPWORDS

text = ""
with open("section10/res/이상한나라의앨리스.txt", "r", encoding="utf-8") as f:      #기본 root 'python'
    text = f.read()

print(text)

#금지어 설정 → 필요한 만큼 add() 함수 호출해서 추가
#금지어 → Alice, said
ignore=set(STOPWORDS)
ignore.add("Alice")
ignore.add("said")

#WordCloud 클래스의 객체 생성
wc=WordCloud(width=1200, height=800, scale=2.0, 
                     stopwords=ignore,      #금지어
                     max_font_size=150,     #최대 글자 크기
                     max_words=100        #최대 표시 단어 수
                    )

gen=wc.generate(text)
print(gen.words_)

pyplot.figure()

pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("simple2.png")

pyplot.close()

