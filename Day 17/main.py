class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following +=1

user1 = User('01','Kanniga')
user2 = User('02','Kaushik')
user1.follow(user2)
print(user1.followers)
print(user2.followers)
print(user1.following)
print(user2.following)