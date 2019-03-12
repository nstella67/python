#/section11/13-graph.py
#데이터프레임 시각화

from matplotlib import pyplot
from print_df import print_df
from pandas import DataFrame
from sklearn.impute import SimpleImputer
from sample import traffic
import numpy

df=DataFrame(traffic)
print_df(df)
"""
+----+-------+-------+-------+--------+-------+
|    | seoul | busan | daegu | inchun | month |
+----+-------+-------+-------+--------+-------+
| 0  |  3166 |  927  |  933  |  655   |  1월  |
| 1  |  2728 |  857  |  982  |  586   |  2월  |
| 2  |  3098 |  988  |  1049 |  629   |  3월  |
| 3  |  3172 |  955  |  1032 |  669   |  4월  |
| 4  |  3284 |  1014 |  1083 |  643   |  5월  |
| 5  |  3247 |  974  |  1117 |  627   |  6월  |
| 6  |  3268 |  1029 |  1076 |  681   |  7월  |
| 7  |  3308 |  1040 |  1080 |  657   |  8월  |
| 8  |  3488 |  1058 |  1174 |  662   |  9월  |
| 9  |  3312 |  971  |  1163 |  606   |  10월 |
| 10 |  3375 |  958  |  1146 |  641   |  11월 |
| 11 |  3179 |  982  |  1135 |  663   |  12월 |
+----+-------+-------+-------+--------+-------+
"""

#데이터 전처리
month=list(df["month"])   #"월"에 대한 칼럼만 리스트로 추출
new_name={}     #빈 딕셔너리 생성
print_df(month)     #['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']

#"월" 리스트에 대해 반복
for i, v in enumerate(month):
    #딕셔너리에 {인덱스번호:값} 형식으로 채워넣음
    new_name[i]=v

#데이터프레임의 인덱스 변경
df.rename(index=new_name, inplace=True)
#기존의 "월" 칼럼은 삭제
df.drop("month", axis=1, inplace=True)
print_df(df)
"""
+------+-------+-------+-------+--------+
|      | seoul | busan | daegu | inchun |
+------+-------+-------+-------+--------+
| 1월  |  3166 |  927  |  933  |  655   |
| 2월  |  2728 |  857  |  982  |  586   |
| 3월  |  3098 |  988  |  1049 |  629   |
| 4월  |  3172 |  955  |  1032 |  669   |
| 5월  |  3284 |  1014 |  1083 |  643   |
| 6월  |  3247 |  974  |  1117 |  627   |
| 7월  |  3268 |  1029 |  1076 |  681   |
| 8월  |  3308 |  1040 |  1080 |  657   |
| 9월  |  3488 |  1058 |  1174 |  662   |
| 10월 |  3312 |  971  |  1163 |  606   |
| 11월 |  3375 |  958  |  1146 |  641   |
| 12월 |  3179 |  982  |  1135 |  663   |
+------+-------+-------+-------+--------+
"""


#다양한 그래프 시각화

#한글폰트, 그래픽 크기 설정
pyplot.rcParams["font.family"]="NanumGothic"
pyplot.rcParams["font.size"]=13
pyplot.rcParams["figure.figsize"]=(10, 6)


#1) 상자그림
pyplot.grid()
df.boxplot()
pyplot.title("2017년 교통사고 변화")
# pyplot.savefig("boxplot3.png", dpi=200)
pyplot.show()
pyplot.close()


#2) 선그래프
x=numpy.arange(len(month))
df.plot()
pyplot.grid()
pyplot.title("2017년 월별 교통사고 변화")
pyplot.ylabel("교통사고 수")
pyplot.xticks(x, month)
pyplot.xlim(0, 11)
# pyplot.savefig("plot.png", dpi=200)
pyplot.show()
pyplot.close()


