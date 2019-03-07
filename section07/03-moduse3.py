#/section07/02-moduse3.py

#객체가 정의된 모듈 참조

#1) 
import my_mod3
print(my_mod3.my_calc.plus(5, 3))       #8
print(my_mod3.my_calc.minus(5, 3))    #2


#2) 모듈 자체에 별칭 부여
import my_mod3 as hello
print(hello.my_calc.plus(5, 3))      #8
print(hello.my_calc.minus(5, 3))   #2


#3) 모듈에 정의된 특정 기능(여기서는 객체)만 참조
from my_mod3 import my_calc
print(my_calc.plus(5, 3))      #8
print(my_calc.minus(5, 3))   #2
