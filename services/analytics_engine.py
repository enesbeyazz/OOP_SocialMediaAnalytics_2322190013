from collections import Counter

class AnalyticsEngine:
    """
    Stage 1 & 3: Analitik Motoru.
    Tüm hesaplamalar ve algoritmalar burada döner.
    """
    
    @staticmethod
    def calculate_engagement_rate(post):
        """Etkileşim oranı hesaplama"""
        total_actions = post.likes + post.comments + post.shares
        if post.impressions == 0:
            return 0
        return (total_actions / post.impressions) * 100

    @staticmethod
    def get_top_posts(posts, top_n=3):
        """
        Stage 2 & 3 Algoritma: Sıralama (Sorting)
        Popülerliğe (Total Engagement) göre sıralar.
        """
        # Python'un Timsort algoritmasını kullanır (O(n log n))
        sorted_posts = sorted(posts, key=lambda p: p.get_total_engagement(), reverse=True)
        return sorted_posts[:top_n]

    @staticmethod
    def get_trending_keywords(posts, top_n=3):
        """
        Stage 3 Algoritma: Frekans Analizi (Trending Detection)
        Post içeriklerindeki kelimeleri sayar.
        """
        all_text = " ".join([p.content.lower() for p in posts])
        words = all_text.split()
        # Basit stopwords filtresi (bağlaçları çıkaralım)
        stopwords = ['ve', 'ile', 'de', 'da', 'the', 'a', 'in', 'is']
        filtered_words = [w for w in words if w not in stopwords and len(w) > 2]
        
        counter = Counter(filtered_words)
        return counter.most_common(top_n)

    @staticmethod
    def get_platform_stats(posts):
        """
        Stage 3: Kullanım Analitiği (Platform bazlı dağılım)
        """
        stats = {}
        for post in posts:
            if post.platform not in stats:
                stats[post.platform] = {'count': 0, 'likes': 0}
            stats[post.platform]['count'] += 1
            stats[post.platform]['likes'] += post.likes
        return stats