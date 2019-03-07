#/section09/02-line2.py
#pyplot의 옵션 설정

#모듈 참조
from matplotlib import pyplot

#데이터 참조(sample.py)
from sample import newborn
from sample import year

pyplot.figure()

pyplot.plot(newborn, label="baby count", linestyle="--", marker=".", color="#0b1c7c")
#1)
pyplot.savefig("line1.png")

#2) label속성 적용
pyplot.legend()
pyplot.savefig("line2.png")

#3) 배경에 그리드 표시
pyplot.grid()
pyplot.savefig("line3.png")

#4) 그래프 제목, x축, y축 라벨 설정
pyplot.title("NewBorn baby of Year")
pyplot.xlabel("year")
pyplot.ylabel("newborn")
pyplot.savefig("line4.png")

#5) x축의 각 위치에 year 리스트의 값을 라벨로 적용
pyplot.xticks([0, 1, 2, 3, 4], year)
pyplot.savefig("line5.png")

pyplot.show()

pyplot.close()




