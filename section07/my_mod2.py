#/section07/my_mod2.py

class Member:
    username=None
    email=None

    def __init__(self, username, email):
        print("--------생성자가 실행되었습니다--------")
        self.username=username
        self.email=email

    def view_info(self):
        tp1="이름:{0} / 이메일:{1}"
        print(tp1.format(self.username, self.email))

