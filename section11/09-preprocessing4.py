#/section11/09-preprocessing4.py
#조건에 맞는 행 추출하기

from pandas import DataFrame
from sample import grade_dic
from print_df import print_df
import numpy

#데이터 구성하기
df=DataFrame(grade_dic, index=["철수","영희", "민철", "수현", "호영"])
print(df)

#sum, max, min, mean 함수에 'axis=1'을 설정하면 각각의 행에 대해 계산함
#   → 계산 결과를 새로운 열로 추가
df["평균"]=df.mean(axis=1)
print_df(df)

#numpy 모듈을 사용하여 조건부 데이터 추가
# 평균 70점 이상이면 합격, 그렇지 않으면 불합격
df["결과"]=numpy.where(df["평균"]>=70, "합격", "불합격")
print_df(df)

#학점을 부여하기 위한 점수의 구간을 설정하는 조건들을 리스트로 설정
conditions=[(df["평균"]>=90), #A
                     (df["평균"]>=80), #B
                     (df["평균"]>=70), #C
                     (df["평균"]<70), #F
                    ]

#조건에 따라 부여될 학점
grade=["A", "B", "C", "F"]

#조건에 따른 학점열 추가하기
df["학점"]=numpy.select(conditions, grade)

#결과확인
print_df(df)

