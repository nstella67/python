#/section09/03-font.py
#폰트이름 확인하기
#글꼴을 사용하려면 글꼴의 실제 이름을 알아야 함

from matplotlib import font_manager

#폰트매니저 리빌드
#   → 시스템 글꼴폴더(C:\Windows\Fonts) 스캔?
font_manager._rebuild()

#시스템 글꼴 목록을 리스트로 가져오기
font_list=font_manager.findSystemFonts()

for file_path in font_list:
    #폰트파일의 경로를 사용하여 폰트속성 객체 가져오기
    fp=font_manager.FontProperties(fname=file_path)

    #폰트속성을 통해 파이썬에 설정해야 하는 폰트이름 조회
    font_name=fp.get_name()

    #폰트파일 경로와 폰트이름 출력하기
    print("%s>>%s"%(file_path, font_name))



