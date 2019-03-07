#/section07/04-os.py
# OS 제공 기본 모듈
#운영체제 자체의 기능에 접근할 수 있는 기능을 제공하는

import sys      #현재 시스템의 정보를 제공
import os       #운영체제 기능에 접근

#현재 운영체제 이름 얻기
#윈도우 win32, 리눅스 linus1, Mac darwin
print(sys.platform)     #win32

if sys.platform=="win32":
    command="dir"
else:
    command="ls -l"

os.system(command)
