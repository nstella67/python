#/section02/07-dic1.py
#리스트만큼 많이 사용
#HashMap 클래스, JSON문법과 비슷
#{"key":value, "key":value ~}
#key와 value 쌍으로 데이터를 정의하는 구조

#딕셔너리 정의하기
dic = {"name":"무궁화", "phone":"123-4567", "birth":"0305"}
print(dic)
print(dic["name"])
print(dic["phone"])

dic["name"] = "라일락"
print(dic["name"])

#print(dic["weight"]) 존재하지 않는 키값을 사용하면 에러

dic["height"] = 175   #존재하지 않는 키에 값을 할당하면 확정
print(dic["height"])

del(dic["birth"]) #삭제
print(dic)

#키가 중복될 경우 하나를 제외한 나머지는 무시됨
data = {"msg":"HELLO", "msg":"WORLD", "msg":"PYTHON"}
print(data)

#key는 정수형도 가능(권장하지 않음)
rank = {0:"PYTHON", 30:"R", 10:"JAVA"}
print(rank[0])
print(rank[30])
print(rank[10])

