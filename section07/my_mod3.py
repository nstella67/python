#/section07/my_mod3.py
#자체적으로 객체를 생성하는 모듈

class Calc:
    def plus(self, x, y):
        return x+y
    
    def minus(self, x, y):
        return x-y

my_calc=Calc()

