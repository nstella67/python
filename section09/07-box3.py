#/section09/07-box3.py
#가로 막대그래프

from matplotlib import pyplot
from sample import newborn
from sample import year

pyplot.rcParams["font.family"]='Malgun Gothic'
pyplot.rcParams["font.size"]=12
pyplot.rcParams["figure.figsize"]=(12, 8)


pyplot.figure()

#가로 막대 그래프
#   → barh() 함수의 기준축은 y방향
pyplot.barh(year, newborn, label="신생아 수")
pyplot.legend()                      #범주 표시하기
pyplot.xlabel("신생아 수")         #데이터(x축) 라벨
pyplot.xlim(350000, 450000)     #데이터(x축) 범위
pyplot.ylabel("년도")               #기준축(y축) 라벨
pyplot.title("년도별 신생아수")   #그래프 제목
pyplot.grid()                          #격자 선 표시

pyplot.show()
pyplot.close()