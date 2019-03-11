#/section11/02-dataframe1.py
# 데이터 프레임 
# → 엑셀 
# → Series의 모음

from pandas import DataFrame
from sample import grade_list
from sample import grade_dic

#2차원 리스트를 데이터 프레임으로 변환
#   → Nan은 값이 없다는 뜻
df=DataFrame(grade_list)
print(df)

print(df[0])    #0열의 데이터

#칼럼(열) 이름을 지정하여 새로 생성
c_names=["국어", "영어", "수학", "과학"]
df=DataFrame(grade_list, columns=c_names)
print(df)
print(df["영어"])

#인덱스(행) 이름을 지정하여 새로 생성
i_names=["철수", "영희", "미철", "수현", "호영"]
df=DataFrame(grade_list, index=i_names)
print(df)

#인덱스와 컬럼이름 모두 지정하기
#index에는 s가 붙지 않는다. 주의
df=DataFrame(grade_list, index=i_names, columns=c_names)
print(df)

#딕셔너리를 통한 데이터 프레임 만들기
#   → 딕셔너리의 key는 DataFrame의 칼럼(열) 이름이 된다
df=DataFrame(grade_dic)
print(df)

#인덱스 이름을 지정한 데이터 프레임 만들기
#가장 흔하게 사용하는 문장
df=DataFrame(grade_dic, index=["철수", "영희", "미철", "수현", "호영"])
print(df)

