import os
import django
import urllib.request
from django.core.files import File
from urllib.error import HTTPError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post, Profile

# Realistic Unsplash photos for feed posts (Valid IDs)
feed_images = [
    "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=800",
    "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=800",
    "https://images.unsplash.com/photo-1542204165-65bf26472b9b?w=800",
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800",
    "https://images.unsplash.com/photo-1444464666168-49b626f1110c?w=800"
]

captions = [
    "Enjoying the beautiful outdoors today! Nature is amazing. 🌲✨",
    "A stunning view that takes my breath away. #landscape #photography",
    "Living my best life in this wonderful setting. Peace and tranquility. 🌊",
    "Just a random beautiful capture from today's walk. 📸",
    "Nature always wears the colors of the spirit. 🌿🕊️"
]

profiles = list(Profile.objects.exclude(user__username='sanjana'))

if not profiles:
    print("No profiles found.")
else:
    os.makedirs('media/images', exist_ok=True)
    
    # Create Feed Posts
    for i, url in enumerate(feed_images):
        profile = profiles[i % len(profiles)]
        
        print(f"Downloading feed post image {i+1} for {profile.user.username}...")
        try:
            result = urllib.request.urlretrieve(url)
            post = Post.objects.create(
                title=f"Post {i+1}",
                author=profile,
                caption=captions[i],
                location="Explore Page"
            )
            with open(result[0], 'rb') as f:
                post.image.save(f'unsplash_feed_{i}.jpg', File(f), save=True)
            print(f"Created post {i+1} for {profile.user.username}")
        except HTTPError as e:
            print(f"Failed to download image {i+1}: {e}")

print("Successfully seeded posts with realistic images!")
