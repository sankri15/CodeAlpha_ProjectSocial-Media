import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post, Profile
from django.contrib.auth.models import User

url = 'https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=800'  # Beautiful landscape

try:
    user = User.objects.filter(username='sanjana').first()
    if not user:
        user = User.objects.first()
        
    profile = user.profile
    
    post = Post(
        title="Nature vibes", 
        title_tag="nature", 
        author=profile, 
        caption="Taking some time to appreciate the little things. 🌿🏔️ What a beautiful world we live in.", 
        location="Swiss Alps"
    )
    
    print(f"Creating post for {user.username}...")
    result = urllib.request.urlretrieve(url)
    with open(result[0], 'rb') as f:
        post.image.save(f'{user.username}_new_post.jpg', File(f), save=False)
        
    post.save()
    print(f"Post created successfully!")
except Exception as e:
    print(f"Error creating post: {e}")
