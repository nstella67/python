#/section10/05-bigdata.py
#년도별 국내특허 통계

from matplotlib import pyplot
import numpy

from sample import Australia
from sample import Canada
from sample import Germany
from sample import Korea
from sample import Japan
from sample import label

#한글폰트 설정
pyplot.rcParams["font.family"]='NanumGothic'
pyplot.rcParams["font.size"]=12

#그래프 설정 시작
pyplot.figure()

x=numpy.arange(len(label))

#기본적으로 pyplot은 clear()를 호출하기 전까지 모든 출력 내역이 누적됨
pyplot.bar(x-0.1, Australia, label="호주", width=0.1, color="#addada")
pyplot.bar(x-0.05, Canada, label="캐나다", width=0.1, color="#8080ff")
pyplot.bar(x, Germany, label="독일", width=0.1, color="#e0edad")
pyplot.bar(x+0.05, Korea, label="한국", width=0.1, color="#ff9b9b")
pyplot.bar(x+0.1, Japan, label="일본", width=0.1, color="#efcbb6")

pyplot.title('나라별 2007~2016년 국제특허 통계')
pyplot.xlabel('년도')
pyplot.ylabel('특허수')
pyplot.xticks(x, label)
pyplot.ylim(200, 20000)
pyplot.legend(title='국가', loc='center left', shadow=True)

pyplot.show()

# pyplot.savefig('patent2.png', dpi=200)
pyplot.close()

