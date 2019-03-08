# /dualipa/DuaLipa_DuaLipa.py
# Word Cloud 배경이미지

from matplotlib import pyplot
from wordcloud import WordCloud
from wordcloud import STOPWORDS

# from PIL import Image
# import numpy

text = ""
with open("dualipa/music/DuaLipa_DuaLipa.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text)

#금지어 설정 → 필요한 만큼 add() 함수 호출해서 추가
#금지어 → Alice, said
ignore=set(STOPWORDS)
ignore.add("-")
ignore.add("Dua Lipa")

#꾸밈기능 : 앨리스 이미지 파일 위에 출력
#배경이미지 가져오기
# img=Image.open("section10/res/앨리스배경.png")
#배경이미지 데이터를 numpy 리스트로 변환
# img_array=numpy.array(img)

#WordCloud 클래스의 객체 생성
wc=WordCloud(width=1200, height=800, scale=2.0, stopwords=ignore, 
                     max_font_size=150, max_words=100, 
                    # mask=img_array,                    #배경이미지
                     background_color="#fce8d1"    #배경색
                    )

gen=wc.generate(text)
print(gen.words_)

pyplot.figure()

pyplot.imshow(gen, interpolation="bilinear")
wc.to_file("dualipa_dualipa.png")

pyplot.close()

