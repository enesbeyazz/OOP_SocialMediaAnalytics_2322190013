import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from services.system import SocialMediaAnalyticsSystem
from utils.file_manager import FileManager

app = Flask(__name__)

# --- AYARLAR ---
# Yüklenen dosyalar buraya gidecek
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Klasör yoksa oluştur
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

system = SocialMediaAnalyticsSystem()
FileManager.load_data(system)

@app.route('/')
def index():
    all_posts = system.posts[::-1]
    return render_template('index.html', posts=all_posts, accounts=system.accounts)

@app.route('/add_account', methods=['POST'])
def add_account():
    username = request.form.get('username')
    platform = request.form.get('platform')
    followers = int(request.form.get('followers'))
    system.add_account(username, platform, followers)
    FileManager.save_data(system)
    return redirect(url_for('index'))

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    """HATA AYIKLAMALI (DEBUG) POST EKLEME"""
    if request.method == 'POST':
        # 1. HTML'den gelen ham verileri alalım
        account_id = int(request.form.get('account_id'))
        post_type = request.form.get('type') # Buradan ne geliyor? 'image' mi 'Image' mi?
        content = request.form.get('content')
        platform = request.form.get('platform')
        
        # 2. TERMİNALE YAZDIR (AJAN KODU BURASI)
        print("--------------------------------------------------")
        print(f"GELEN TİP: {post_type}")
        print(f"GELEN RESİM LİNKİ (FORM): {request.form.get('image_url')}")
        print(f"GELEN VİDEO LİNKİ (FORM): {request.form.get('video_url')}")
        print(f"GELEN DOSYALAR: {request.files}")
        print("--------------------------------------------------")

        extra_args = {}

        # --- RESİM İŞLEMLERİ ---
        # post_type.lower() diyerek büyük/küçük harf hatasını engelliyoruz
        if post_type and post_type.lower() == 'image':
            final_url = None
            
            # Dosya var mı?
            if 'image_file' in request.files:
                file = request.files['image_file']
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    final_url = f"/static/uploads/{filename}"
                    print(f"DOSYA KAYDEDİLDİ: {final_url}")
            
            # Dosya yoksa Link var mı?
            if not final_url:
                final_url = request.form.get('image_url')
                print(f"LİNK KULLANILIYOR: {final_url}")

            # EĞER HALA URL YOKSA, UYARI VERELİM (HATA OLMASIN DİYE BOŞ STRING ATADIM)
            if not final_url:
                print("DİKKAT: Hem dosya hem link boş geldi!")
                final_url = "" 

            extra_args['image_url'] = final_url
            extra_args['resolution'] = "1080p"

        # --- VİDEO İŞLEMLERİ ---
        elif post_type and post_type.lower() == 'video':
            final_url = None
            
            if 'video_file' in request.files:
                file = request.files['video_file']
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    final_url = f"/static/uploads/{filename}"
            
            if not final_url:
                final_url = request.form.get('video_url')

            if not final_url:
                print("DİKKAT: Video linki veya dosyası bulunamadı!")
                final_url = ""

            extra_args['video_url'] = final_url
            extra_args['duration'] = 60

        # Veriyi sisteme ekle
        system.add_post(post_type, account_id, content, platform, **extra_args)
        FileManager.save_data(system)
        return redirect(url_for('index'))

    return render_template('add_post.html', accounts=system.accounts)

@app.route('/like/<int:post_id>')
def like_post(post_id):
    system.log_interaction(post_id, 'like')
    FileManager.save_data(system)
    return redirect(url_for('index'))

@app.route('/analytics')
def analytics():
    top_posts = system.analytics.get_top_posts(system.posts)
    trends = system.analytics.get_trending_keywords(system.posts)
    platform_stats = system.analytics.get_platform_stats(system.posts)
    return render_template('analytics.html', top_posts=top_posts, trends=trends, stats=platform_stats)

if __name__ == '__main__':
    app.run(debug=True)