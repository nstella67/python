#/section03/02-ref.py
#값 복사 : 정수, 실수, 논리값, 문자열 -> 원본은 그대로
#참조복사: 리스트, 튜플, 딕셔너리     -> 원본도 변경

a = 100
b = a
print(a)
print(b)

b = 200
print(a) #원본에 변화가 없다
print(b)


#객체의 참조 -> 리스트, 딕셔너리
foo = [1,2,3]
bar = foo
print(foo)
print(bar)

# -> 참조된 복사본을 변경하면 원본도 함께 변경됨
# -> 반대의 경우도 마찬가지
# -> 리스트, 딕셔너리에 적용됨
bar[1] = 20
print(foo)
print(bar)

#리스트 복사(고전적인 방법)
bar = [1,2,3]
cp1 = [0,0,0]
cp1[0] = bar[0]
cp1[1] = bar[1]
cp1[2] = bar[2]
print(bar)
print(cp1)

cp1[2] = 1000 #원본에 변화 없음
print(bar)
print(cp1)
#------------------------------------------
#원본에 영향이 없이
#리스트, 딕셔너리객체를 복사하고자 하는 경우
#1) 슬라이싱을 활용한 방법 (파이선에 많이 사용)
cp2 = bar[:]
print(bar)
print(cp2)
cp2[1] = 12345
print(bar) #원본에 영향없음
print(cp2)

#2) 함수를 사용하는 방법
cp3 = bar.copy()
cp3[0] = 789
print(bar) #원본에 영향없음
print(cp3)








