import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post, Comment
from django.contrib.auth.models import User

try:
    user = User.objects.filter(username='sanjana').first()
    if not user:
        user = User.objects.first()
        
    post = Post.objects.filter(author=user.profile).last()
    
    if post:
        Comment.objects.create(post=post, name="jane_doe", body="Wow, this looks absolutely breathtaking! 😍 Have fun!")
        Comment.objects.create(post=post, name="liam_k", body="Beautiful shot! What camera did you use?")
        Comment.objects.create(post=post, name="emma_w", body="So jealous right now! Enjoy your trip! ✈️")
        print("Successfully added 3 comments to the post!")
    else:
        print("Could not find a post.")
except Exception as e:
    print(f"Error adding comments: {e}")
