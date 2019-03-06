#/section06/01-obj1.py
#클래스와 객체
"""---------------------------------------------------------------------------------
#클래스 선언
class Member:
    userid="python"
    email="webmaster@soldesk.com"
    phone="0101234567"

#객체 선언
mem1=Member()
print(mem1.userid)
print(mem1.email)
print(mem1.phone)

mem2=Member()
print(mem2.userid)
print(mem2.email)
print(mem2.phone)
---------------------------------------------------------------------------------"""


"""-------------------------------------------------------------------------------------
#함수를 내장하는 클래스 정의
    # → 클래스에 포함되는 함수들은 반드시 첫번째 파라미터 self를 정의해야 한다
class Calc:
    def plus(self, x, y):
        return x+y

    def minus(self, x, y):
        return x-y
        
    def all(self, x, y):
        a=self.plus(x, y)
        b=self.minus(x, y)
        return (a, b) #튜플로 묶어서 여러 개의 값을 한번에 리턴

#객체 선언
my=Calc()
print(my.plus(5, 3))        #8
print(my.minus(5, 3))       #2

a=my.all(10, 20)
print(a[0])                 #30
print(a[1])                 #-10

p, m=my.all(100, 200)
print(p)                    #300
print(m)                    #-100
-------------------------------------------------------------------------------------"""


#변수와 함수를 모두 내장하는 클래스 정의
class Member:
    username=""
    email=""

    def join(self, username, email):
        self.username=username
        self.email=email

    def view_info(self):
        print(self.username)
        print(self.email)

mem1=Member()
mem1.join("python", "webmaster@soldesk.com")
mem1.view_info()





