from traceback import print_tb

class Client:
    pass



class User:
    def __init__(self, user_id, username):
        print("This is the constructor for user class...")
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Asma")


print(user_1.follower)

user_2 = User("002", "Fatima")


user_1.follow(user_2)
print(f"This is user 1 followers {user_1.follower}")
print(f"This is user 1 following {user_1.following}")


print(f"This is user 1 followers {user_2.follower}")
print(f"This is user 1 following {user_2.following}")