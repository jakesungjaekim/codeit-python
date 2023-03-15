# __init__ method
class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw
        
        User.count += 1 
    def __str__(self):
        return "사용자: {}, 이메일: {}, 비밀번호: ****".format(self.name, self.password)

    # cls는 규칙입니다.
    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다".format(cls.count))

    # def number_of_users(self):
    #     print("총 유저 수는: {}입니다.".format(User.count))


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("jake", "jake@codeit.kr", "123456")
user3 = User("김성재", "jake123@codeit.kr", "123456")

User.number_of_users()
user1.number_of_users()