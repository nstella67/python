#/section04/03-print.py
#print()함수의 사용 방법들

print("Hello Python")				#Hello Python
print("Life"+"is"+"short")			#Lifeisshort
print("Life" "is" "short")			#Lifeisshort

a=100
print("Life", "is", "short", a)		#Life is short 100

print("Life", end="")				#end 안쓰면 줄바꿈이 없음 Life
print("is", end="")					#is
print("short", end="")				#short

#end는 출력 후 마무리를 어떻게 할지 지정하는 기능
print("You", "need", "Python", end="~~:)")	#You need Python~~:)

