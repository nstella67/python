#/section02/02-list2.py
#2차원 리스트 - 리스트이 각 원소가 다른 리스트로 구성된 형태

#각 학생별 이름, 점수 정의
stud1 = ["홍길동", 98]
stud2 = ["무궁화", 82]
stud3 = ["라일락", 72]

#1차원 리스트
#->새로운 리스트 stud_group의 각 원소가 리스트가 되는 형태
stud_group = [stud1, stud2, stud3]
print(stud_group)

#2차원 리스트
#->1차원 원소에 접근하기
print(stud_group[0])
print(stud_group[1])

#->2차원 원소에 접근하기
print(stud_group[0][0])
print(stud_group[0][1])
print(stud_group[1][0])
print(stud_group[1][1])

#2차원 리스트의 일괄 생성
grade = [
          ["개나리", 60], ["진달래", 55]
        ]
print(grade)
#에러
#print(grade[3][1])
