#/section02/05-list5.py
#리스트 관련 함수

my_list = [1, 2, 3]
size = len(my_list)   #갯수조회
print(size)

my_list = [1, 2, 3]
my_list.append(4)     #맨뒤 추가
print(my_list)

my_list = [1, 2, 3]
my_list.insert(1, 10) #중간 삽입
print(my_list)

#맨 마지막 요소를 꺼내고 삭제 -> 마지막 요소 리턴
my_list = [1, 2, 3]
k = my_list.pop()
print(k)

print(my_list.pop())
print(my_list) 

#리스트 확장
my_list = [1, 2, 3]
addon = [10, 9 , 8, 7]
my_list.extend(addon)  #my_list = my_list+addon과 동일
print(my_list) 
#주어진 값과 일치하는 원소 갯수 세기
my_list = [1, 2, 3, 2]
c = my_list.count(2)

#해당 값이 가장 처음 나타나는 위치(인덱스 반환)
my_list = [1, 2, 3, 10, 1, 2, 3, 10]
x = my_list.index(10)
print(x) 

#주어진 값과 일치하는 첫번째 원소 삭제
my_list = [1, 2, 3, 10, 1, 2, 3, 10]
my_list.remove(10)
print(my_list) 


my_list = [1,3,5,7,9]
my_list.reverse()          #순서 뒤집기
print(my_list)

my_list = [9,3,5,1,7]
my_list.sort()             #순차정렬
print(my_list) 

my_list = [9,3,5,1,7]
my_list.sort(reverse=True) #역순정렬
print(my_list) 

text = "Hello,Python,World,Good"
my_list = text.split(",")
print(my_list)
