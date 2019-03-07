#/section07/02-moduse2.py
"""----------------------------------------------------------------------------------------
#1) 클래스가 정의된 모듈 참조하기
import my_mod2
mem=my_mod2.Member("무궁화", "moo@soldesk.com")
mem.view_info()
#--------생성자가 실행되었습니다--------
#이름:무궁화 / 이메일:moo@soldesk.com


#2) 클래스가 정의된 모듈에 별칭 적용하기
import my_mod2 as user
mem=user.Member("홍길동", "hong@soldesk.com")
mem.view_info()
# --------생성자가 실행되었습니다--------
# 이름:홍길동 / 이메일:hong@soldesk.com

----------------------------------------------------------------------------------------"""
#3) 클래스가 정의된 모듈에서 특정 기능만 가져오기
from my_mod2 import Member
mem=Member("대한민국", "korea@soldesk.com")
mem.view_info()
# --------생성자가 실행되었습니다--------
# 이름:대한민국 / 이메일:korea@soldesk.com
