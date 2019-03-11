#/section10/05-bigdata.py
#년도별 국내특허 통계

#모듈 참조
from matplotlib import pyplot
import numpy

#데이터 참조
from sample import Australia1
from sample import Canada1
from sample import Germany1
from sample import Korea1
from sample import Japan1
from sample import label

#한글폰트 설정
pyplot.rcParams["font.family"]='NanumGothic'
pyplot.rcParams["font.size"]=12

#그래프 설정 시작
pyplot.figure()

#배경에 그리드 표시하기
pyplot.grid()

#그래프 제목, x, y축 라벨 설정
pyplot.title('나라별 2007~2016년 국제특허 통계')
pyplot.xlabel('년도')
pyplot.ylabel('특허수')

#기본적으로 pyplot은 clear()를 호출하기 전까지 모든 출력 내역이 누적됨
pyplot.plot(Australia1, label='호주')
pyplot.plot(Canada1, label='캐나다')
pyplot.plot(Germany1, label='독일')
pyplot.plot(Korea1, label='한국')
pyplot.plot(Japan1, label='일본')

#x, y축의 범위 설정
pyplot.xlim(0, 9)
pyplot.ylim(0, 20000)

#범주를 표시하도록 설정
pyplot.legend(title='국가', loc='center left', shadow=True)

#x축의 각 지점에 적용될 라벨 설정
x=list(range(0, len(label)))

#   → x 리스트의 각 좌표에 지정될 라벨 설정
pyplot.xticks(x, label)

#그래프 저장하기
pyplot.savefig('patent.png', dpi=200)

pyplot.show()

# 그래프 관련 설정 해제
pyplot.close()

