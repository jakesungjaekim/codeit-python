# 인스턴스 메소드
class User:
    def say_hello(some_user):
        print("안녕하세요! 저는 {}입니다.".format(some_user.name))
    
    def login(some_user, my_email, my_password):
        if some_user.email == my_email and  some_user.password == my_password:
            print("로그인 성공입니다. 환영합니다")
        else:
            print("로그인 실패입니다. 없는 아이디거나 잘못된 비밀번호입니다.")
        
    def check_name(self, name):
        return self.name == name

# 서로 다른 인스턴스
user1 = User()
user2 = User()
user3 = User() 

# 인스턴스 변수 정의하기
# 인스턴스이름.속성이름 = '속성에 넣을 값'

user1.name = '김대위'
user1.email = 'captain@codeit.kr'
user1.password = '12345'

user2.name = '강영훈'
user2.email = 'younghoon@codeit.kr'
user2.password = '98765'

user3.name = 'jake'
user3.email = 'jake@codeit.kr'
user3.password = '78965'

# 인스턴스 변수 사용하기
# 인스턴스이름.인스턴스변수이름

print(user1.email)
print(user2.password)

User.say_hello(user1)
User.say_hello(user2)
User.say_hello(user3)

# 인스턴스 메소드의  특별한 규칙
user1.say_hello()
# 첫번째 파라미터는 자동으로 들어가는 특별한 규칙
user1.login("captain@codeit.kr", "12345")

# 셀프(첫번째 파라미타 권장사항)
# 인스턴스 메소드
class User:
    def say_hello(self):
        print("안녕하세요! 저는 {}입니다.".format(self.name))
    
    def login(self, my_email, my_password):
        if self.email == my_email and  self.password == my_password:
            print("로그인 성공입니다. 환영합니다")
        else:
            print("로그인 실패입니다. 없는 아이디거나 잘못된 비밀번호입니다.")


print(user1.check_name("김대위"))
