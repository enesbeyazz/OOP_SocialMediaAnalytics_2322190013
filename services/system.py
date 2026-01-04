from models.post import TextPost, ImagePost, VideoPost
from models.account import SocialAccount
from models.interaction import Interaction
from services.analytics_engine import AnalyticsEngine

class SocialMediaAnalyticsSystem:
    """
    Stage 1: System Facade (Ana Yönetici)
    Tüm veriyi tutar ve işlemleri koordine eder.
    """
    def __init__(self):
        self.accounts = []
        self.posts = []
        self.analytics = AnalyticsEngine()

    def add_account(self, username, platform, followers=0):
        new_acc = SocialAccount(username, platform, followers)
        self.accounts.append(new_acc)
        print(f"Hesap eklendi: {username}")
        return new_acc

    def add_post(self, post_type, account_id, content, platform, **kwargs):
        """Factory Pattern benzeri post oluşturma"""
        if post_type == "text":
            new_post = TextPost(account_id, content, platform, kwargs.get('language', 'TR'))
        elif post_type == "image":
            new_post = ImagePost(account_id, content, platform, kwargs.get('url'), kwargs.get('res'))
        elif post_type == "video":
            new_post = VideoPost(account_id, content, platform, kwargs.get('url'), kwargs.get('dur'))
        else:
            print("Hatalı post tipi!")
            return None

        self.posts.append(new_post)
        
        # Hesabın post listesine de ekle
        acc = self.find_account_by_id(account_id)
        if acc:
            acc.posts.append(new_post.id)
            
        print(f"Post oluşturuldu ({post_type}): {content[:15]}...")
        return new_post

    def log_interaction(self, post_id, type):
        """Stage 2: Etkileşim Kaydı"""
        post = self.find_post_by_id(post_id)
        if post:
            interaction = Interaction(type, post_id)
            post.log_interaction(interaction)
            print(f"Etkileşim eklendi: {type} -> Post {post_id}")
        else:
            print("Post bulunamadı!")

    def find_post_by_id(self, p_id):
        # Stage 2 Algoritma: Linear Search (Basit arama)
        for p in self.posts:
            if p.id == p_id:
                return p
        return None
    
    def find_account_by_id(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                return acc
        return None

    def filter_posts_by_keyword(self, keyword):
        """Stage 2: Arama Fonksiyonu"""
        return [p for p in self.posts if keyword.lower() in p.content.lower()]