#section02/06-string_function.py
# 문자열 관련 함수

str="Life is too short. You need Python"

print(len(str))				#34
print(str.count("i"))		#2
print(str.count("a"))		#0
print(str.count("short"))	#1
print(str.count("nice"))	#0

#특정 글자나 단어가 마지막으로 등장하는 위치 조회
#마지막으로 나타나는 글자의 위치를 왼쪽에서 0부터 카운트
#찾지 못할 경우 -1 리턴
print(str.rfind("i"))		#5
print(str.count("a"))		#0
print(str.count("short"))	#1
print(str.count("nice"))	#0

#특정 글자나 단어가 처음 등장하는 위치 조회
print(str.index("short"))
#찾지 못할 경우 에러 발생(쓰지 않음)
#print(str.index("nice"))	#에러

#특정 단어나 글자로 시작하는지 여부 검사(True, False)
print(str.startswith("L"))		#T
print(str.startswith("l"))		#F
print(str.startswith("Life"))	#T
print(str.startswith("H"))		#F
print(str.startswith("Hello"))	#F

#특정 단어나 글자로 끝나는지 여부(True, False)
print(str.endswith("N"))		#F
print(str.endswith("n"))		#T
print(str.endswith("Python"))	#T
print(str.endswith("python"))	#F

upchar=str.upper()
print(upchar)

lowchar=str.lower()
print(lowchar)

print(str.swapcase())					#대소문자 서로 바꿔서
print(str.capitalize())					#문장의 첫 글자 대문자
print(str.title())						#각 단어의 첫 글자 대문자
print(str.replace("Life", "My height"))	#My height is too short. You need Python

k="   py th on  "
print("#"+k.lstrip()+"#")	##py th on#
print("#"+k.rstrip()+"#")	##   py th on#
print("#"+k.strip()+"#")	##py th on#

a=","
b=a.join("python")
print(b)			#p,y,t,h,o,n