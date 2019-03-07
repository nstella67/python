#/section/05-datetime.py
#시스템의 현재 날짜 정보 조회하기

import datetime as DT

now_time=DT.datetime.now()
print(now_time)                     #2019-03-07 11:23:35.251571

#현재시각 객체에서 원하는 값만 추출하기
print(now_time.year)                #2019
print(now_time.month)             #3
print(now_time.day)                 #7
print(now_time.hour)               #11
print(now_time.minute)            #23
print(now_time.second)            #35
print(now_time.microsecond)     #251571

#요일 이름 출력
d=now_time.weekday()
print(d)                                #3
days=("월", "화", "수", "목", "금", "토", "일")
print(days[d])                        #목

#출력 형식 만들기
print(now_time.strftime("%y/%m%d %H:%M:%S"))        #19/0307 11:23:35
