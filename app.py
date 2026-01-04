from flask import Flask, render_template, request, redirect, url_for
from services.system import SocialMediaAnalyticsSystem
from utils.file_manager import FileManager

app = Flask(__name__)

# Sistemi başlat
system = SocialMediaAnalyticsSystem()
# Varsa eski verileri yükle
FileManager.load_data(system)

@app.route('/')
def index():
    """Anasayfa: Postları listele"""
    # Postları ters çevirelim ki en yenisi en üstte görünsün
    all_posts = system.posts[::-1]
    return render_template('index.html', posts=all_posts, accounts=system.accounts)

@app.route('/add_account', methods=['POST'])
def add_account():
    """Yeni hesap ekleme işlemi"""
    username = request.form.get('username')
    platform = request.form.get('platform')
    followers = int(request.form.get('followers'))
    
    system.add_account(username, platform, followers)
    FileManager.save_data(system) # Her işlemde kaydet
    return redirect(url_for('index'))

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    """Post paylaşma sayfası"""
    if request.method == 'POST':
        account_id = int(request.form.get('account_id'))
        post_type = request.form.get('type')
        content = request.form.get('content')
        platform = request.form.get('platform')
        
        # Ekstra alanlar
        extra_args = {}
        if post_type == 'image':
            extra_args['url'] = request.form.get('image_url')
            extra_args['res'] = "1080p"
        elif post_type == 'video':
            extra_args['url'] = request.form.get('video_url')
            extra_args['dur'] = 60
        
        system.add_post(post_type, account_id, content, platform, **extra_args)
        FileManager.save_data(system)
        return redirect(url_for('index'))

    return render_template('add_post.html', accounts=system.accounts)

@app.route('/like/<int:post_id>')
def like_post(post_id):
    """Beğeni butonu"""
    system.log_interaction(post_id, 'like')
    FileManager.save_data(system)
    return redirect(url_for('index'))

@app.route('/analytics')
def analytics():
    """Analiz sayfası"""
    top_posts = system.analytics.get_top_posts(system.posts)
    trends = system.analytics.get_trending_keywords(system.posts)
    platform_stats = system.analytics.get_platform_stats(system.posts)
    
    return render_template('analytics.html', 
                           top_posts=top_posts, 
                           trends=trends, 
                           stats=platform_stats)

if __name__ == '__main__':
    app.run(debug=True)