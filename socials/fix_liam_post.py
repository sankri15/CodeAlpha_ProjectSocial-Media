import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post
from django.contrib.auth.models import User

try:
    user = User.objects.get(username="liam_k")
    profile = user.profile
    post = Post.objects.filter(author=profile).first()

    if post:
        print("Downloading new image for Liam's post...")
        url = "https://images.unsplash.com/photo-1449844908441-8829872d2607?w=800"
        result = urllib.request.urlretrieve(url)
        with open(result[0], 'rb') as f:
            post.image.save('liam_new_post.jpg', File(f), save=True)
        post.caption = "A new perspective on the city. 🏙️✨"
        post.save()
        print("Liam's post updated successfully!")
    else:
        print("No post found for Liam.")
except Exception as e:
    print(f"Error: {e}")
