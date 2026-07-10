import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post
from django.contrib.auth.models import User

# Using distinct, beautiful Unsplash images
users_to_update = {
    'emma_w': 'https://images.unsplash.com/photo-1517841905240-472988babdf9?w=800',  # Beautiful portrait
    'jane_doe': 'https://images.unsplash.com/photo-1483985988355-763728e1935b?w=800'  # Fashion/shopping
}

for username, url in users_to_update.items():
    try:
        user = User.objects.get(username=username)
        profile = user.profile
        post = Post.objects.filter(author=profile).first()
        
        if post:
            print(f"Updating post for {username}...")
            result = urllib.request.urlretrieve(url)
            with open(result[0], 'rb') as f:
                post.image.save(f'{username}_new_post.jpg', File(f), save=True)
            print(f"{username}'s post updated successfully!")
        else:
            print(f"No post found for {username}")
    except Exception as e:
        print(f"Error updating {username}: {e}")
