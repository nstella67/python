#/section07/01-moduse1.py
#모듈(module)의 활용
# 모듈 : 다른 프로그램에서 활용하기 위한 프로그램 조각
#import 파일이름
#.jar 라이브러리 ???
"""-------------------------------------------------------------------------
#1)
import my_mod1

#파일이름.기능명
print(my_mod1.NAME)         #Hello Python
print(my_mod1.plus(5, 3))     #8
print(my_mod1.minus(5, 3))  #2

-----------------------------------------------------------------------------------
#2) 모듈에 별칭 적용
#   → import 파일이름 as 별칭
import my_mod1 as hello
print(hello.NAME)           #Hello Python
print(hello.plus(5, 3))       #8
print(hello.minus(5, 3))    #2

-----------------------------------------------------------------------------------
#3) 모듈 안에 포함된 특정 기능만 골라서 가져오기
#   → from 모듈이름 import 기능명
from my_mod1 import NAME
from my_mod1 import plus

print(NAME)         #Python
print(plus(5, 3))     #8
#print(minus(5, 3))  #에러. minus함수 import 안함

-------------------------------------------------------------------------"""

