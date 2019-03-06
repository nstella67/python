#/section05/01-fileio.py

#파일 입출력
# → r : 읽기 모드
# → w : 쓰기 모드
# → a : 추가 모드
#------------------------------------------------------------------------------------
"""-----------------------------------------------------------------------------------
#1) 파일 쓰기
f=open("helloworld.txt", "w", encoding="utf-8")
f.write("Hello Python!!\n\n")
f.write("안녕하세요~파이선!!\n")
f.close()

#2) 파일 읽기
f=open("helloworld.txt", "r", encoding="utf-8")
data=f.read()
print(data)
f.close()

#3) 쓰기 모드로 파일 객체 생성하기
#   →  f.colse()는 자동으로 수행함. 생략가능
with open("helloworld.txt", "w", encoding="utf-8") as f:
    for i in range(1, 10):
        f.write("%d>>"%i)
        f.write("Life is too short, ")
        f.write("you need Python\n")

    print("파일 저장이 완료되었습니다")
-----------------------------------------------------------------------------------"""

#4) 읽기 모드로 파일 객체 생성하기
with open("helloworld.txt", "r", encoding="utf-8") as f:
    #data=f.read()
    #print(data)
    lines=f.readlines()     #각 행을 원소로 갖는 리스트 생성
    print(lines)

print("행의 갯수 : %d" % len(lines))
for item in lines:
    print(item.strip())     #공백제거
