#/section12/01-xlsx.py
#엑셀 파일을 통한 데이터 수집
#모듈 설치
# pip install xlrd
#pip install openpyxl

from print_df import print_df
from pandas import ExcelFile
from pandas import DataFrame
from matplotlib import pyplot
import datetime as dt

#엑셀파일 읽기
xls_file=ExcelFile("section12/children_house.xlsx")

#엑셀의 sheet 이름들 표시
sheet_names=xls_file.sheet_names
print_df(sheet_names)       #<class 'list'>  ['데이터', '메타정보']

#첫 번째 sheet를 dataframe으로 변환
df=xls_file.parse(sheet_names[0])
print_df(df)
"""
+----+----------+-------+-------+-------+
|    |   지역   |  2014 |  2015 |  2016 |
+----+----------+-------+-------+-------+
| 0  | 전국(계) | 43742 | 42517 | 41084 |
| 1  |   서울   |  6787 |  6598 |  6368 |
| 2  |   부산   |  1957 |  1971 |  1937 |
| 3  |   대구   |  1588 |  1539 |  1483 |
| 4  |   인천   |  2308 |  2278 |  2231 |
| 5  |   광주   |  1260 |  1264 |  1238 |
| 6  |   대전   |  1698 |  1669 |  1584 |
| 7  |   울산   |  946  |  934  |  895  |
| 8  |   세종   |  160  |  216  |  250  |
| 9  |   경기   | 13259 | 12689 | 12120 |
| 10 |   강원   |  1257 |  1227 |  1180 |
| 11 |   충북   |  1229 |  1230 |  1208 |
| 12 |   충남   |  2053 |  1988 |  1974 |
| 13 |   전북   |  1654 |  1623 |  1562 |
| 14 |   전남   |  1242 |  1238 |  1251 |
| 15 |   경북   |  2212 |  2130 |  2102 |
| 16 |   경남   |  3533 |  3349 |  3158 |
| 17 |   제주   |  599  |  574  |  543  |
+----+----------+-------+-------+-------+
"""

#데이터 전처리
#이름에 대한 열을 리스트로 추출
city_list=list(df["지역"])
print_df(city_list)     #['전국(계)', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

#새로 적용할 인덱스 이름에 대한 딕셔너리 구조 생성
index_dict={}
for i, v in enumerate(city_list):
    index_dict[i]=v
print_df(index_dict)    #{0: '전국(계)', 1: '서울', 2: '부산', 3: '대구', 4: '인천', 5: '광주', 6: '대전', 7: '울산', 8: '세종', 9: '경기', 10: '강원', 11: '충북', 12: '충남', 13: '전북', 14: '전남', 15: '경북', 16: '경남', 17: '제주'}

#원본에서는 이름에 대한 열을 제거하고 인덱스 이름 변경
df.drop("지역", axis=1, inplace=True)
df.rename(index=index_dict, inplace=True)

#전국에 대한 데이터는 필요 없으므로 행 삭제
df.drop(["전국(계)"], inplace=True)

#결과확인
print_df(df)
"""
+------+-------+-------+-------+
| 서울 |  6787 |  6598 |  6368 |
| 부산 |  1957 |  1971 |  1937 |
| 대구 |  1588 |  1539 |  1483 |
| 인천 |  2308 |  2278 |  2231 |
| 광주 |  1260 |  1264 |  1238 |
| 대전 |  1698 |  1669 |  1584 |
| 울산 |  946  |  934  |  895  |
| 세종 |  160  |  216  |  250  |
| 경기 | 13259 | 12689 | 12120 |
| 강원 |  1257 |  1227 |  1180 |
| 충북 |  1229 |  1230 |  1208 |
| 충남 |  2053 |  1988 |  1974 |
| 전북 |  1654 |  1623 |  1562 |
| 전남 |  1242 |  1238 |  1251 |
| 경북 |  2212 |  2130 |  2102 |
| 경남 |  3533 |  3349 |  3158 |
| 제주 |  599  |  574  |  543  |
+------+-------+-------+-------+
"""

#생성된 정보를 엑셀파일로 저장하기
#파일이름
#sheet_name → 시트이름
#na_rep → 결측치를 표시할 문자열(기본값=빈문자열)
#index → False로 지정할 경우 index는 저장안함(여기서는 사용하지 않음)
#index_label → 인덱스에표시될 제목(기본값=빈문자열)
#header → 각 칼럼의 제목으로 사용될 문자열 리스트(기본값=데이터프레임의 칼럼명)
#encoding → 파일 인코딩(default=utf-8)
df.to_excel("전국어린이집.xlsx", sheet_name="어린이집", na_rep="Nan", index=True, index_label="지역", header=["15년", "16년", "17년"])


#데이터 시각화
#그래프 만들기
pyplot.rcParams["font.family"]="NanumGothic"
pyplot.rcParams["font.size"]=13
pyplot.rcParams["figure.figsize"]=(10, 6)

#전체 갈럼에 대한 시각화
df.plot.bar()
pyplot.grid()
pyplot.title("2014~2016년 전국 어린이집 분포")
pyplot.legend()
pyplot.ylabel("어린이집 수")
pyplot.show()
pyplot.close()