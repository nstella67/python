#/section03/01-value.py
#변수를 정의하는 파이선만의 다양한 방법

#1)튜플을 통한 변수 생성
a, b = ("python", "bigdata")
print(a)
print(b)

(a, b) = "hello", "world"
print(a)
print(b)

(a, b) = ("안녕", "파이선")
print(a)
print(b)


#2)리스트를 활용한 변수 생성
a, b = ["python", "bigdata"]
print(a)
print(b)

[a, b] = "hello", "world"
print(a)
print(b)

[a, b] = ["안녕", "파이선"]
print(a)
print(b)


#3)동일한 값을 갖는 여러 변수 생성
a=b=c=123
print(a)
print(b)
print(c)


#4)두 변수의 값을 교환 (파이선에만 있음)
x = 3
y = 5
x, y = y, x
print(x)
print(y)








