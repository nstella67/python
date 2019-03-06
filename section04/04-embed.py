# /section04/04-embed.py
# 자료형 조회
a = 123
print(type(a))      #<class 'int'>

b=123.45
print(type(b))      #<class 'float'>

print(type("Hello"))    #<class 'str'>
print(type(True))       #<class 'bool'>
print(type([1, 2]))     #<class 'list'>
print(type([1, 2]))     #<class 'list'>
print(type({"name":"Python"}))  #<class 'dict'>

#형변환
x="123"
y="45"
print(x+y)  #12345

x1=int(x)
y1=int(y)
print(x1+y1)    #168

x2=float(x1)
y2=float(y1)
print(x2+y2)    #168.0

print(str(x2)+str(y2))  #123.045.0


#수학관련 함수
print(pow(2, 3))    #2*2*2
print(abs(4))        #절대값
print(abs(-3.5))    

#나눗셈의 연산 결과를 정수 부분의 몫과 나머지로 계산하여 튜플로 리턴
print(divmod(7, 3))     #(2, 1)  =>(몫, 나머지)
hours=800
k=divmod(800, 24)
tp1="{0}일 {1}시간"
print(tp1.format(k[0], k[1]))   #33일 8시간

days, hours = divmod(960, 24)
print(tp1.format(days, hours))   #40일 0시간


#연속성 자료형과 관련된 내장 함수
# 리스트, 튜플, 딕셔너리

a={1, 2, 3}
print(len(a))

a=[1, 2, 3]
print(max(a))
print(min(a))
print(sum(a))

print(sum(a)/len(a))    # 평균

#-------------------------------------------------------------------------
a="Python"
b=list(a)
print(b)   #['P', 'y', 't', 'h', 'o', 'n']
b=tuple(a)
print(b)  #('P', 'y', 't', 'h', 'o', 'n')

c=(1, 2, 3)
d=list(c)
print(d)        #[1, 2, 3]
d=tuple(c)
print(d)        #(1, 2, 3)

e=[10, 20, 30]
f=list(e)
print(f)        #[10, 20, 30]
f=tuple(e)
print(f)        #(10, 20, 30)

#----------------------------------------------------------------------------------------------------

#딕셔너리 경우 key, value를 별도로 추려내기
g={"a":100, "b":200}
h=list(g.keys())
print(h)        #['a', 'b']

i=list(g.values())
print(i)        #[100, 200]
i=tuple(g.values())
print(i)        #(100, 200)

k=range(1, 10)
print(k)                #range(1, 10)
print(type(k))          #<class 'range'>

mylist=list(k)
print(mylist)           #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(mylist))     #<class 'list'>

k=list(range(1, 10, 3))
print(k)                    #[1, 4, 7]

#--------------------------------------------------------------------------------------------------

#리스트 자체를 정렬하기
data=[1, 4, 5, 3, 2]
#print(data.sort())      #원본 리스트 자체가 정렬

k=sorted(data)
print(data)         #[1, 4, 5, 3, 2]        원본 변화 없음
print(k)            #[1, 2, 3, 4, 5]
