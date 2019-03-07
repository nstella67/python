#/section09/02-line2.py
#pyplot의 옵션 설정

#모듈 참조
from matplotlib import pyplot

#데이터 참조(sample.py)
from sample import newborn
from sample import year

pyplot.figure()

#1)
pyplot.plot(newborn, label="baby count", linestyle="--", marker=".", color="#0b1c7c")
pyplot.savefig("line1.png")

pyplot.close()




