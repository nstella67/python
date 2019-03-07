#/section08/01-numpy1.py
#numpy 모듈 : 리스트의 기능 강화판
#numpy 모듈 설치
#   → cmd> pip install numpy
#   →      > pip list 모듈 설치 확인

# 모듈 가져오기
import numpy

arr=[1, 2, 3]
print(arr)       #[1, 2, 3]

a=numpy.array(arr)
print(a)        #[1 2 3]


#리스트를 통한 1차원 배열 만들기
a=numpy.array(arr)
print(a)                    #[1 2 3]
print(len(a))              #3

arr2=[1.2, 3, "4"]
print(arr2)             #[1.2, 3, '4']

#실수가 범위가 더 크므로 모든 원소가 실수형으로 변환
b=numpy.array([1, 2.3, 4, 5.6])
print(b)                #[1.  2.3 4.  5.6]

#모든 타입이 문자열로 변환
c=numpy.array([1.2, 3, '4'])
print(c)                #['1.2' '3' '4']

#모든 원소의 타입을 강제로 int로 지정
d=numpy.array([1, 2.4, 3, 4.6], dtype='int')
print(d)                #[1 2 3 4]

#리스트값을 배열형태로 변환
arr3=numpy.array([1, 2, 5, 7, 9])
size=len(arr3)
print("배열의 원소는 %d개 입니다."%size)        #배열의 원소는 5개 입니다.

#배열 원소 접근
print(arr3[0])      #1
print(arr3[1])      #2
print(arr3[3])      #7

for i, v in enumerate(arr3):
    print("%d번째 원소 :%d")
