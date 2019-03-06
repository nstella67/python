#/section02/09-dic3.py
#딕셔너리 관련 함수

dic = {"name":"무궁화", "phone":"123-4567", "birth":"0305"}
print(dic["name"])
print(dic.get("name"))

#존재하지 않는 key에 접근하는 경우
#print(dic["addr"])     에러
#print(dic.get("addr")) None

#get함수는 전달하는 key가 존재하지 않을 경우
#대신 반환될 값을 함께 설정할 수 있다
print(dic.get("addr","관철동"))

#key만 모아서 객체로 반환
keys = dic.keys()
print(keys)

#list변환
key_list = list(keys)
print(key_list)

#value만 모아서 리스트 변환
value_list = list(dic.values())
print(value_list)

#key-value를 튜플로 묶어서 리스트 변환
lists = list(dic.items())
print(lists)















