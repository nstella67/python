#/section09/06-box2.py
#다중 막대그래프

import numpy
from matplotlib import pyplot
from sample import seoul
from sample import busan
from sample import label

#
pyplot.rcParams["font.family"]='Malgun Gothic'
pyplot.rcParams["font.size"]=12
pyplot.rcParams["figure.figsize"]=(12, 8)


pyplot.figure()
#막대그래프 기준축에 대한 좌표를 표현한 배열 생성(0~11)
x=numpy.arange(len(label))
#print(x)            #[ 0  1  2  3  4  5  6  7  8  9 10 11]

# pyplot.bar(x, seoul, label="서울", width=0.4, color="#6ad0d0")
# pyplot.bar(x, busan, label="부산", width=0.4, color="#8080ff")


#2)
pyplot.bar(x-0.2, seoul, label="서울", width=0.4, color="#6ad0d0")
pyplot.bar(x+0.2, busan, label="부산", width=0.4, color="#8080ff")

pyplot.xticks(x, label)
pyplot.legend()
pyplot.xlabel('월')
pyplot.ylabel('교통사고 수')
pyplot.ylim(0, 4000)
pyplot.title('2017년 서울, 부산 교통사고 현황')

pyplot.show()
pyplot.close()