#/section03/06-for-list.py
#연속성 데이터 기반의 반복문 처리

test_str = "Python"
for i in test_str:
    print(i)

#몇번째 원소인지 알수 없다
test_list = ["python", "is", "good"]
for i in test_list:
    print(i)


count = 0 #원소의 인덱스를 별도의 변수 사용
for i in test_list:
    print("%d번째 원소:%s" % (count, i))
    count += 1


size = len(test_list)
for i in range(0, size):
    print("%d번째 원소:%s" % (i, test_list[i]))



for i, value in enumerate(test_list):
    print("%d번째 값 >> %s" % (i,value))









