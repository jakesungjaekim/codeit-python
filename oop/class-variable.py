# 클래스 변수
class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        
        User.count += 1 
    
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("jake", "jake@codeit.kr", "123456")
user3 = User("김성재", "jake123@codeit.kr", "123456")

# 클래스  변수의 값을 설정할 때는 클래스 이름.클래스변수를  사용해야합니다.
User.count = 5

print(User.count)
print(user1.count)
print(user2.count)
print(user3.count)


