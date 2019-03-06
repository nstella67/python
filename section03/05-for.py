#/section03/05-for.py
#반복문

#1~11전까지
for x in range(1, 11) :
    print("x=%d" % x)

#1~10전까지
for y in range(1, 10) :
    z = 7*y
    print("7 * %d = %d" % (y,z))


#값의 변화 단계 조절하기
for a in range(0, 100, 10):
    print("a=%d" % a)


#10~0전까지 -2씩 감소
for b in range(10, 0, -2):
    print("b=%d" % b)












