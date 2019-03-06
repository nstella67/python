#/section05/01-fileio.py
"""-------------------------------------------------------------------------------------------
#1) CSV 파일 저장을 
grade=[ {"name":"홍길동", "kor":90, "eng":85, "mat":100},
            {"name":"무궁화", "kor":30, "eng":80, "mat":90},
            {"name":"라일락", "kor":60, "eng":55, "mat":70}
        ]
tp1="{0}, {1}, {2}, {3}\n"

#CSV 파일 저장을 위한 f객체 생성
    # → Excel : csv는 euc-kr형식
    # → Sublime : euc-kr형식은 읽지 못함
with open("grade.csv", "w", encoding="utf-8") as f:
    f.write("이름  국어  영어   수학\n")
    for item in grade:
        tmp=tp1.format(item["name"], item["kor"], item["eng"], item["mat"])
        f.write(tmp)
-------------------------------------------------------------------------------------------"""

#2) CSV 파일 읽기
with open("grade.csv", "r", encoding="utf-8") as f:
    csv_list=f.readlines()
    print(csv_list)

    for i, line in enumerate(csv_list):
        if i>0:
            item=line.strip().split(",")
            #print(item)
            name=item[0]
            kor=int(item[1])
            eng=int(item[2])
            mat=int(item[3])
            total=kor+eng+mat
            aver=total/3

            tp1="{0} {1} {2} {3} {4} {5:0.2f}"
            print(tp1.format(name, kor, eng, mat, total, aver))

            