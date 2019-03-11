#/section11/04-datainfo.py
#기초통계 산출하기

from pandas import DataFrame
from sample import grade_dic

#데이터 구성하기
df=DataFrame(grade_dic, index=["철수","영희", "민철", "수현", "호영"])

print(df)

print(df.head())    #(파라미터 없을 경우 기본 5줄)
# 전체에 대한 처음 2줄만 추출
print(df.head(2))
print(df["영어"].head(2))   #특정 열에 대한 처음 2줄

#마지막 2줄만 보기
#   → 파라미터가 없을 경우 5줄이 기본
print(df.tail(2))
print(df["영어"].tail(2))   #특정열에 대한 마지막 2줄

#전체 요약 정보 가져오기
des=df.describe()
print(type(des))    #요약정보의 타입은 DataFrame
print(des)              #요약정보 출력하기

#요약정보의 개별 조회
# 각 열, 혹은 특정 열에 대해 Nan를 제외한 값의 수를 반환
print(df.count())
print(df["영어"].count())

print(df.min())
print(df["영어"].min())

print(df.max())
print(df["영어"].max())

print(df.sum())
print(df["영어"].sum())

print(df.mean())                #평균
print(df["영어"].mean())

print(df.std())
print(df["영어"].std())     #표준편차

print(df.median())              #중앙값(2사분위수)
print(df["영어"].median())

print(df.quantile(q=0.5))          #사분위 수(중앙값:50%위치의 값)
print(df["영어"].quantile(q=0.5))

print(df.quantile(q=0.25))               #1사분위 수(25%위치의 값)
print(df["영어"].quantile(q=0.25))

print(df.quantile(q=0.75))  #3사분위 수 (75%위치의 값)

#사분위 수 이외의 위치 추출
#   → 0에서부터 출발해서 90%위치의 값. 즉 상위 10%
print(df.quantile(q=0.9))



