#/section03/03-if1.py
#조건문
#형식) if 조건식:
#자바에서의 {}기능은 탭(tab)이 한다

"""-----------------------------------------------
have_money = False
if have_money:
    print("서울")
    print("종로구")
    print("관철동")

print("인사동")

#빈문자열은 False로 간주
name = "Python"
#name = ""
if name:
    print(name)

print("프로그래밍")

#리스트, 튜플, 딕셔너리에 대한 조건 
#grade = [] -> 원소가 없으면 False로 간주
grade = [100, 80, 70]
if grade:
    msg = "국어:{0}, 영어:{1}, 수학:{2}"
    print(msg.format(grade[0], grade[1], grade[2]))


#숫자형 변수는 0이면 False
money = 12000 
if money: print("돈이 있다")


if money>=5000:
    print("선물을 사고 %d원 남았다" % (money-5000))


if money and money<15000:
    print("돈이 있지만 %d원 부족했다" % (15000-money))
#----------------------------------------------------
#is 연산자

a = 123
b = 123
c = 234

if a is b:
    print("a와 b는 같다")

if b is c:
    print("b와 c는 같다")


#== 값만 비교
#is 변수의 타입까지 비교    
x = 123.0
y = 123
z = 123

if x == z :
    print("x와 z는 같다")

if y is z :
    print("y와 z는 같다")


두값이 서로 다르면 : 참
if x is not y:
    print("x와 y는 다르다")

if y is not z:
    print("y와 z는 다르다")
#--------------------------------------------

#in 연산자 : 포함 여부를 검사

user1 = "hello"
user2 = "world"
member_list = ["hello", "python", "life"]

a = user1 in member_list
print(a)

b = user2 in member_list
print(b)


if user1 in member_list:
    print(user1 + " 이미 가입되어 있다")

if user2 in member_list:
    print(user2 + " 이미 가입되어 있다")


#not in 연산자 : 포함되지 않았음을 조사
if user1 not in member_list:
    print(user1 + " 이미 가입되어 있지 않다")

if user2 not in member_list:
    print(user2 + " 이미 가입되어 있지 않다")
--------------------------------------------"""
#if ~ else문
age = 19
if age>19:
    print("성인입니다")
else:
    print("성인이 아닙니다")


user1 = "hello"
user2 = "world"
member_list = ["hello", "python", "life"]
if user1 in member_list:
    print("%s는 가입되어 있다" % user1)
else:
    print("%s는 가입되어 있지 않다" % user1)


point = 72
if point>90:
    print("A학점")
elif point>80:
    print("B학점")
elif point>70:
    print("C학점")
elif point>60:
    print("D학점")
else:
    print("F학점")



















