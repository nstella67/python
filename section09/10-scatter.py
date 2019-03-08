# /section09/10-scatter.py
# 산점도 그래프
#   → 두 변수 간의 영향력을 보여주기 위해 가로축과 세로축에 데이터 포인트를 그리는 그래프
#   → 두 가지 수치에 대한 관계를 추론하기 위한 근거

from matplotlib import pyplot
from sample import tmp  # 온도
from sample import qty  # 아이스크림 판매량

pyplot.rcParams["font.family"] = "Malgun Gothic"
pyplot.rcParams["font.size"] = 12
pyplot.rcParams["figure.figsize"] = (10, 10)

pyplot.figure()

pyplot.scatter(tmp, qty, color="#de7688", label="판매수량")
pyplot.legend()
pyplot.grid()
pyplot.title("기온과 아이스크림 판매수량의 관계")
pyplot.ylabel("아이스크림 판매수량")
pyplot.xlabel("기온")

pyplot.show()
pyplot.close()
