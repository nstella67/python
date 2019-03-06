#/section/05-parse.py
"""--------------------------------------------------------------
문자열의 인덱싱 및 슬라이싱

--------------------------------------------------------------"""

#인덱싱 - 특정 위치의 글자를 추출
str="Life is too short. You need Python"
print(str[3])	#0부터 시작
print(str[-3])	#h
print(str[-1])	#n

#슬라이싱 - 특정 범위의 글자들을 추출
print("#"+str[0:3]+"#")		#0~2
print("#"+str[5:7]+"#")		#5~6
print("#"+str[19:]+"#")		#19~끝까지
print("#"+str[:17]+"#")		#~16

print("#"+str+"#")
print("#"+str[:]+"#")
print("#"+str[19:-7]+"#")	#앞에서 19번째부터 뒤에서 -7번째 다음까지

#문제)
jumin="8712301"
birth=jumin[2:6]	#생년월일
gender=jumin[6:]	#성별
year="19"+jumin[:2]	#1987
month=jumin[2:4]	#12
day=jumin[4:6]		#30

print(jumin)
print(birth)
print(gender)
print(year)
print(month)
print(day)


