#/section04/02-func2.py
"""---------------------------------------------------------
#리턴값이 있는 함수
def plus(x, y):
	z=x+y
	return z

a=plus(1, 3)
print(a)			#4

print(plus(5, 6))	#11

b=plus(2, 4)+100
print(b)			#106
---------------------------------------------------------"""


"""---------------------------------------------------------
def foo(x, y):
	if x<10 or y<10:
		return 0
	z=x+y
	return z

print(foo(3, 5))	#0
print(foo(30, 50))	#80
---------------------------------------------------------"""


"""---------------------------------------------------------
def id_check(user_id):
	member_list=["user1", "user2", "user3"]

	#user_id가 없다면 처리 중단
	if not user_id: return

	if user_id in member_list:
		print("사용할 수 없는 아이디입니다")
	else:
		print("사용 가능한 아이디입니다")

id_check("")
id_check("user1")	#사용할 수 없는 아이디입니다
id_check("python")	#사용 가능한 아이디입니다
---------------------------------------------------------"""


#함수와 변수의 유표범위
a=100
b=100

def test():
	c=a+b
	print(c)

test()
#print(c) 에러

