#/section09/04-line3.py
#다중 선 그래프

#모듈 참조
from matplotlib import pyplot
import numpy

#데이터 참조
from sample import seoul
from sample import busan
from sample import daegu
from sample import inchun
from sample import label

#한글폰트 설정
pyplot.rcParams["font.family"]='Malgun Gothic'
pyplot.rcParams["font.size"]=12

#그래프 설정 시작
pyplot.figure()

#배경에 그리드 표시하기
pyplot.grid()

#그래프 제목, x, y축 라벨 설정
pyplot.title('2017년 주요도시 교통사고')
pyplot.xlabel('월')
pyplot.ylabel('교통사고')

#기본적으로 pyplot은 clear()를 호출하기 전까지 모든 출력 내역이 누적됨
pyplot.plot(seoul, label='서울')
pyplot.plot(busan, label='부산')
pyplot.plot(daegu, label='대구')
pyplot.plot(inchun, label='인천')

#해상도 dpi=100 기본값
pyplot.savefig('traffic1.png', dpi=200)

#x, y축의 범위 설정
pyplot.xlim(0, 11)
pyplot.ylim(0, 4000)

#범주를 표시하도록 설정
pyplot.legend(title='도시', loc='center left', shadow=True)

#중간결과 확인
pyplot.savefig('traffic2.png', dpi=200)

#x축의 각 지점에 적용될 라벨 설정
#   → 0부터 1씩 증가하는 label 리스트 만큼의 크기를 갖는 리스트
x=list(range(0, len(label)))

#   → x 리스트의 각 좌표에 지정될 라벨 설정
pyplot.xticks(x, label)

#그래프 저장하기
pyplot.savefig('section09/test.png', dpi=200)


pyplot.show()

# 그래프 관련 설정 해제
pyplot.close()

