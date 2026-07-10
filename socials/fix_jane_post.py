import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post
from django.contrib.auth.models import User

try:
    user = User.objects.get(username="jane_doe")
    profile = user.profile
    post = Post.objects.filter(author=profile).first()

    if post:
        print("Downloading new image for Jane Doe's post...")
        url = "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800"
        result = urllib.request.urlretrieve(url)
        with open(result[0], 'rb') as f:
            post.image.save('jane_new_post.jpg', File(f), save=True)
        post.caption = "A beautiful sunset to end the day! 🌅"
        post.save()
        print("Jane Doe's post updated successfully!")
    else:
        print("No post found for Jane Doe.")
except Exception as e:
    print(f"Error: {e}")
