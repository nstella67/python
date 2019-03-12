#/section11/10-refine1.py
#데이터 정제(1)

#결측치(Missing value) : 누락된 값, 비어있는 값
#이상치(Outlier) : 정상 범주에서 크게 벗어난 값

from print_df import print_df
from pandas import DataFrame
from sample import grade_dic

df=DataFrame(grade_dic, index=["철수", "영희", "민철", "수현", "호영"])
print_df(df)



#결측치 여부 확인 : isnull(), isna() 둘 중 아무거나 사용
#   → 각 열에 대해 결측치가 아닐 경우 False, 결측치는 True로 표시
empty=df.isnull()
empry=df.isna()
print_df(empty)

empty_sum=empty.sum()
print_df(empty_sum)



#결측치가 있는 모든 행 삭제
# → 원본은 변화 없음, 삭제 결과 리턴됨
na1=df.dropna()

#결측치가 삭데된 데이터 프레임 확인
print_df(na1)
"""
<class 'pandas.core.series.Series'>
                        국어    0
                        영어    0
                        수학    0
                        과학    0
"""

#결측치 값 갯수 확인
print_df(na1.isnull().sum())        #dtype: int64



#결측치가 있는 모든 열삭제
na2=df.dropna(axis=1)

#결측치가 삭데된 데이터 프레임 확인
print_df(na2)
"""
                            <class 'pandas.core.frame.DataFrame'>
                            (5, 1)
                            +------+------+
                            |      | 국어 |
                            +------+------+
                            | 철수 |  98  |
                            | 영희 |  88  |
                            | 민철 |  92  |
                            | 수현 |  63  |
                            | 호영 | 120  |
                            +------+------+
"""
#결측치 값 갯수 확인
print_df(na2.isnull().sum())        #dtype: int64



#행의 모든 값이 결측치면 행을 삭제
na3=df.dropna(how="all")
print_df(na3)

#열의 모든 값이 결측치면 열을 삭제
na4=df.dropna(how="all", axis=1)
print_df(na4)
