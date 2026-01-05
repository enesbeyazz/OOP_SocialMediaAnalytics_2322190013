import datetime

class SocialPost:
    def __init__(self, account_id, content, platform):
        """
        Stage 1 & 3: Base Class (Temel Sınıf)
        """
        self.id = id(self)
        self.account_id = account_id
        self.content = content
        self.platform = platform
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Etkileşim sayaçları (Encapsulation)
        self.likes = 0
        self.comments = 0
        self.shares = 0
        self.impressions = 0
        self.interactions = [] # Interaction objeleri

    def log_interaction(self, interaction):
        """Stage 2: Etkileşim kaydetme"""
        self.interactions.append(interaction)
        if interaction.type == 'like':
            self.likes += 1
        elif interaction.type == 'comment':
            self.comments += 1
        elif interaction.type == 'share':
            self.shares += 1
        elif interaction.type == 'view':
            self.impressions += 1

    def get_total_engagement(self):
        """Stage 2: Popülerlik hesaplama algoritması için metrik"""
        return self.likes + self.comments + self.shares

    def get_summary(self):
        """Polimorfizm için base method"""
        return f"Post [{self.id}]: {self.content[:20]}..."

    @property
    def type(self):
        """Template'de kullanılabilmesi için sınıf ismini döndür"""
        return self.__class__.__name__

    def to_dict(self):
        # Kayıt için sözlüğe çevirme
        data = self.__dict__.copy()
        data['interactions'] = [i.to_dict() for i in self.interactions]
        data['type'] = self.__class__.__name__ # Sınıf ismini kaydet (yüklerken lazım olacak)
        return data

# --- Stage 3: Polimorfik Alt Sınıflar ---

class TextPost(SocialPost):
    def __init__(self, account_id, content, platform, language="TR"):
        super().__init__(account_id, content, platform)
        self.language = language

    def get_summary(self):
        return f"[TEXT] ({self.language}): {self.content[:30]}..."

class ImagePost(SocialPost):
    def __init__(self, account_id, content, platform, image_url, resolution):
        super().__init__(account_id, content, platform)
        self.image_url = image_url
        self.resolution = resolution

    def get_summary(self):
        return f"[IMAGE] {self.resolution}: {self.content[:20]}..."

class VideoPost(SocialPost):
    def __init__(self, account_id, content, platform, video_url, duration):
        super().__init__(account_id, content, platform)
        self.video_url = video_url
        self.duration = duration # saniye cinsinden

    def get_summary(self):
        return f"[VIDEO] {self.duration}s: {self.content[:20]}..."