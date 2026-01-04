from services.system import SocialMediaAnalyticsSystem
from services.analytics_engine import AnalyticsEngine
from utils.file_manager import FileManager

def print_menu():
    print("\n--- SOCIAL MEDIA ANALYTICS PLATFORM ---")
    print("1. Hesap Ekle")
    print("2. Post Paylaş (Text/Image/Video)")
    print("3. Etkileşim Yap (Like/Comment)")
    print("4. Postları Listele & Ara")
    print("5. ANALİTİK: Trendler ve En İyiler")
    print("6. Verileri Kaydet")
    print("7. Verileri Yükle")
    print("0. Çıkış")
    print("---------------------------------------")

def main():
    system = SocialMediaAnalyticsSystem()
    
    # Başlangıçta örnek veri yoksa yüklemeyi dene
    # FileManager.load_data(system)

    while True:
        print_menu()
        choice = input("Seçiminiz: ")

        if choice == "1":
            user = input("Kullanıcı adı: ")
            plat = input("Platform (X/Insta/Face): ")
            foll = int(input("Takipçi sayısı: "))
            system.add_account(user, plat, foll)

        elif choice == "2":
            if not system.accounts:
                print("Önce bir hesap ekleyin!")
                continue
            
            # Kolaylık olsun diye ilk hesabı seçiyoruz, normalde seçtirilebilir
            acc_id = system.accounts[0].id
            print(f"Aktif Hesap: {system.accounts[0].username}")
            
            ptype = input("Tip (text/image/video): ").lower()
            content = input("İçerik: ")
            platform = input("Platform: ")
            
            if ptype == "text":
                system.add_post("text", acc_id, content, platform, language="TR")
            elif ptype == "image":
                url = "http://image.url"
                res = "1080p"
                system.add_post("image", acc_id, content, platform, url=url, res=res)
            elif ptype == "video":
                url = "http://video.url"
                dur = 60
                system.add_post("video", acc_id, content, platform, url=url, dur=dur)

        elif choice == "3":
            pid = int(input("Hangi Post ID'ye etkileşim yapılacak? (Listelemek için menü 4): "))
            type_ = input("Tip (like/comment/share/view): ")
            system.log_interaction(pid, type_)

        elif choice == "4":
            keyword = input("Arama kelimesi (Tümü için boş bırak): ")
            results = system.filter_posts_by_keyword(keyword)
            print(f"\n--- Sonuçlar ({len(results)}) ---")
            for p in results:
                print(f"ID: {p.id} | {p.get_summary()} | Beğeni: {p.likes}")

        elif choice == "5":
            print("\n--- ANALİTİK RAPORU ---")
            
            print("\n[EN POPÜLER 3 POST]")
            top_posts = system.analytics.get_top_posts(system.posts)
            for p in top_posts:
                print(f"Score: {p.get_total_engagement()} - {p.content}")

            print("\n[TREND OLAN KELİMELER]")
            trends = system.analytics.get_trending_keywords(system.posts)
            for word, count in trends:
                print(f"#{word}: {count} kez")

            print("\n[PLATFORM İSTATİSTİKLERİ]")
            stats = system.analytics.get_platform_stats(system.posts)
            for plat, data in stats.items():
                print(f"{plat}: {data['count']} post, {data['likes']} toplam beğeni")

        elif choice == "6":
            FileManager.save_data(system)

        elif choice == "7":
            FileManager.load_data(system)

        elif choice == "0":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz işlem!")

if __name__ == "__main__":
    main()