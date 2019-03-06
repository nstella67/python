#/section02/06-tuple.py
#리스트와 기본적으로 동일하지만,
#처음 할당한 원소의 값을 수정할 수 없다
#리스트를 더 많이 사용

grade = (12, 13, 14, 15, 16)
print(grade)
print(grade[0])
#grade[0] = 100  에러
#print(grade(0)) 에러

names = ("홍길동", "무궁화", "진달래", "개나리", "라일락")
print(names)

stud1 = ("봉선화", 90) #자료형에 대한 혼합 사용도 가능함
print(stud1)
print(stud1[0])       #대괄호로 원소 접근
print(stud1[1])







