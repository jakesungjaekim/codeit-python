# __init__ method
class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ****".format(self.name, self.password)

user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("jake", "jake@codeit.kr", "123456")
user3 = User("김성재", "jake123@codeit.kr", "123456")

print(user1.email)
print(user2.name)
print(user1.password)

# __str__ method
print(user1)
print(user2)


