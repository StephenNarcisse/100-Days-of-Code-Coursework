class User:
    def __init__(self, user_id, username):
        # if the parameter is in the initialization it MUST be provided during the creation of the object
        self.id = user_id
        self.username = username
        self.followers = 0
        # followers is not in the initialization but still constructed for later use.
        self.following = 0
        self.follow_list = []

    def follow(self, user):
        self.follow_list.append(user)
        user.followers += 1
        self.following += 1

    pass


user_1 = User("Shadowps9", "King Trash")
user_2 = User("Wess", "Wes")

user_1.follow(user_2)
