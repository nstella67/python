#/section11/01-series.py
# >pip install prettytable
# >pip install pandas

#pandas 모듈에서 Series 클래스 가져오기
from pandas import Series

#리스트, 인덱스 추상적
items=[10, 30, 50, 70, 90]
print(items)

#시리즈, 인덱스가 열로 추가
column=Series(items)
print(column)

#→ 
print(column.values)
print(column.index)

#→ 시리즈값들을 list로 변환
print(list(column.values))
print(list(column.index))

#특정 조건에 맞는 항목들만 추출
#   → 이름[조건식]
in1=column[column>30]
print(in1)

# →and
in2=column[column<70][column>10]
print(in2)

# → or ()필수
in3=column[(column<10)|(column>70)]
print(in3)