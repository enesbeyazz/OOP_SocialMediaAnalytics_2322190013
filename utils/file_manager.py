import json
import os
from models.account import SocialAccount
from models.post import TextPost, ImagePost, VideoPost
from models.interaction import Interaction

class FileManager:
    @staticmethod
    def save_data(system, filename="data/data.json"):
        """Verileri JSON formatında dosyaya yazar."""
        if not os.path.exists("data"):
            os.makedirs("data")

        data = {
            "accounts": [acc.to_dict() for acc in system.accounts],
            "posts": [post.to_dict() for post in system.posts]
        }
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Veriler kaydedildi.")

    @staticmethod
    def load_data(system, filename="data/data.json"):
        """JSON dosyasından verileri sisteme geri yükler."""
        if not os.path.exists(filename):
            print("Kayıtlı veri bulunamadı.")
            return

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Hesapları yükle
        system.accounts = []
        for acc_data in data.get("accounts", []):
            acc = SocialAccount(acc_data['username'], acc_data['platform'], 
                                acc_data['followers_count'], acc_data['following_count'])
            acc.id = acc_data['id'] # Eski ID'yi koru
            acc.posts = acc_data['posts']
            system.accounts.append(acc)

        # Postları yükle
        system.posts = []
        for p_data in data.get("posts", []):
            post_type = p_data.get('type')
            
            # Nesneyi tekrar oluştur (Polimorfizm)
            if post_type == "TextPost":
                post = TextPost(p_data['account_id'], p_data['content'], p_data['platform'], p_data.get('language'))
            elif post_type == "ImagePost":
                post = ImagePost(p_data['account_id'], p_data['content'], p_data['platform'], 
                                 p_data.get('image_url'), p_data.get('resolution'))
            elif post_type == "VideoPost":
                post = VideoPost(p_data['account_id'], p_data['content'], p_data['platform'], 
                                 p_data.get('video_url'), p_data.get('duration'))
            else:
                continue # Bilinmeyen tip

            post.id = p_data['id']
            post.timestamp = p_data['timestamp']
            post.likes = p_data['likes']
            post.comments = p_data['comments']
            post.shares = p_data['shares']
            post.impressions = p_data['impressions']
            
            # Etkileşimleri yükle
            for i_data in p_data.get('interactions', []):
                inter = Interaction(i_data['type'], i_data['post_id'], i_data['account_id'])
                inter.timestamp = i_data['timestamp']
                post.interactions.append(inter)
            
            system.posts.append(post)
            
        print("Veriler başarıyla yüklendi.")