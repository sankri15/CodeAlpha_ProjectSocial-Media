import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post, Profile
from django.contrib.auth.models import User

try:
    user = User.objects.get(username='sanjana')
    posts = Post.objects.filter(author=user.profile).order_by('id')
    
    if posts.count() >= 2:
        post_to_change = posts.first() # Change the older post
        image_url = 'https://images.unsplash.com/photo-1501504905252-473c47e087f8?w=800&q=80' # Coffee & laptop image
        img_path = 'temp_sanjana_post.jpg'
        urllib.request.urlretrieve(image_url, img_path)
        
        with open(img_path, 'rb') as f:
            post_to_change.image.save('sanjana_coffee_post.jpg', File(f), save=True)
            
        post_to_change.caption = "Working on some new code today! 💻☕"
        post_to_change.save()
        print("Successfully updated one of Sanjana's posts with a new photo!")
    else:
        print("Sanjana doesn't have 2 posts.")
except Exception as e:
    print(f"Error: {e}")
