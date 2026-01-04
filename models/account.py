class SocialAccount:
    def __init__(self, username, platform, followers_count=0, following_count=0):
        """
        Stage 1: SocialAccount sınıfı.
        """
        self.id = id(self)
        self.username = username
        self.platform = platform  # Örn: "X", "Instagram", "Facebook"
        self.followers_count = followers_count
        self.following_count = following_count
        self.posts = [] # Bu kullanıcının postlarının ID listesi

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "platform": self.platform,
            "followers_count": self.followers_count,
            "following_count": self.following_count,
            "posts": self.posts
        }