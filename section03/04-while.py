#/section03/04-while.py
#반복문

x = 1
while x<=10:
    print("x=%d" % x)
    x += 1

#7단 출력하기
y = 1
while y<10:
    z = 7 * y
    print("7 * %d = %d" % (y,z))
    y += 1


#1~10까지의 총합을 구하시오
x = 1
sum = 0
while x<=10:
    sum += x
    print("x=%d, sumg=%d" % (x,sum))
    x += 1













