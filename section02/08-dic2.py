#/section02/08-dic2.py
#딕셔너리의 계층 구조
#딕셔너리는 리스트나 다른 딕셔너리를 포함할 수 있다

addr   = ["서울", "종로구", "관철동"]
grade  = {"kor":10, "mat":20, "eng":30}
member = {"userid":"python",
          "age"   :20,
          "addr"  :addr,
          "grade" :grade }

print(member)

#계층화된 값에 접근하기
print(member["addr"][0])
print(member["grade"]["kor"])

#딕셔너리의 계층화 직접 표현
mydic = { "total"      :1962,
          "city"       :["서울", "제주", "부산"],
          "population" :[100, 200, 300],
          "date"       :{'yy':2019, 'mm':3, 'dd':5}
         }

print(mydic)
print(mydic["city"][0])
print(mydic["population"][0])
print(mydic["date"]["yy"])


#리스트의 원소가 딕셔너리가 되는 경우 -> 표 자료형
grade = [
         {"name":"홍길동", "kor":10, "eng":40},
         {"name":"무궁화", "kor":20, "eng":60},
         {"name":"라일락", "kor":30, "eng":90}
        ]

tpl = "{0}의 국어점수:{1}, 영어점수:{2}"
print(tpl.format(grade[0]["name"],grade[0]["kor"],grade[0]["eng"]))
print(tpl.format(grade[1]["name"],grade[1]["kor"],grade[1]["eng"]))
print(tpl.format(grade[2]["name"],grade[2]["kor"],grade[2]["eng"]))















