#/section09/01-line1.py
#선그래프 : 한 가지 지표에 대한 특정 기준(주로 시간)에 따른 변화
#모듈설치 pip install matplotlib

#모듈 참조하기
from matplotlib import pyplot

#데이터
data=[0, 1, 2, 3, 4]

#그래프 설정시작 → 모든 그래프 작업 시작시에 호출
pyplot.figure()

#데이터를 선그래프로 표현
#   → 리스트의 각 값은 y축이 되고,
#   → 리스트 값의 인덱스는 x축이 된다
pyplot.plot(data)

#그래프 표시하기
pyplot.show()

#그래프 관련 설정 해제
pyplot.close()





