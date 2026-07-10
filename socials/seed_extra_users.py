import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from django.contrib.auth.models import User
from base.models import Profile, Post
from django.contrib.auth.hashers import make_password

users = [
    {"username": "olivia_w", "fname": "Olivia", "lname": "Williams", "desc": "🌸 Creating art out of chaos | Coffee enthusiast", "pp": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&fit=crop"},
    {"username": "liam_k", "fname": "Liam", "lname": "Knight", "desc": "🧗‍♂️ Adventure awaits | Travel & Tech", "pp": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&fit=crop"}
]

posts = [
    {"url": "https://images.unsplash.com/photo-1444464666168-49b626f1110c?w=800", "caption": "Lost in the wilderness. Best weekend ever!"},
    {"url": "https://images.unsplash.com/photo-1517816743773-6e0fd518b4a6?w=800", "caption": "Urban exploring in the big city 🏙️"}
]

os.makedirs('media/images', exist_ok=True)
os.makedirs('media/profile_images', exist_ok=True)

for i, u in enumerate(users):
    user, created = User.objects.get_or_create(username=u['username'], defaults={'email': f"{u['username']}@test.com", 'password': make_password('password')})
    if created:
        profile = Profile.objects.create(user=user, username=u['username'], fname=u['fname'], lname=u['lname'], description=u['desc'])
        
        # Download PP
        print(f"Downloading PP for {u['username']}...")
        try:
            result = urllib.request.urlretrieve(u['pp'])
            with open(result[0], 'rb') as f:
                profile.profileimg.save(f"{u['username']}_pp.jpg", File(f), save=True)
        except Exception as e:
            print(f"Failed PP: {e}")
            
        # Download Post
        print(f"Downloading Post for {u['username']}...")
        try:
            result_post = urllib.request.urlretrieve(posts[i]['url'])
            post = Post.objects.create(title=f"Post for {u['username']}", author=profile, caption=posts[i]['caption'], location="Explore Page")
            with open(result_post[0], 'rb') as f:
                post.image.save(f"{u['username']}_post.jpg", File(f), save=True)
        except Exception as e:
            print(f"Failed Post: {e}")
            
print("Extra users added!")
