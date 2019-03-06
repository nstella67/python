#/section02/04-list4.py
#리스트 조작하기

list1 = [1, 2, 3]
list2 = [4, 5, 6]

#1) 리스트 사칙연산
#리스트끼리의 덧셈은 단순 병합
list3 = list1 + list2
print(list3) 

#리스트와 정수의 곱셈은 동일 내용을 반복한다
list4 = list1 * 3
print(list4) 



#2) 리스트의 수정, 확장, 축소
#대입연산자를 이용한 단일 값 수정
mylist = [1, 2, 3]
mylist[2] = 4 
print(mylist)

#주어진 범위를 수정
mylist = [1, 2, 3]
mylist[1:3] = [20, 30] 
print(mylist)

#주어진 범위보다 작은 갯수를 갖는 리스트 지정->리스트 잘림
mylist = [1, 2, 3]
mylist[1:3] = [1000] 
print(mylist)

#주어진 범위보다 많은 갯수를 갖는 리스트 지정->리스트 확장
mylist = [1, 2, 3]
mylist[1:2] = [7,8, 9, 0]
print(mylist)



#3)리스트 원소 삭제
#1번째 원소 삭제
mylist = [1, 2, 3, 4, 5]
del(mylist[1])
print(mylist)

#1번째~3번째전까지 삭제
mylist = [1, 2, 3, 4, 5]
del(mylist[1:3])
print(mylist)

#특정 범위를 삭제하는 또 다른 방법
mylist = [1, 2, 3, 4, 5]
mylist[1:3] = []
print(mylist)



#4)리스트의 원소삽입과 확장 비교

#인덱싱으로 접근하는 경우 -> 단순 삽입
mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist[1] = [100, 200] 
print(mylist)
print(len(mylist)) #원소의 갯수 : 5

#슬라이싱으로 접근하는 경우 -> 주어진 범위를 "확장"
mylist = [1, 2, 3, 4, 5]
print(mylist)
mylist[1:2] = [100, 200]
print(mylist)
print(len(mylist)) #원소의 갯수 : 6





