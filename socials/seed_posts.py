import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post, Profile

# Realistic Unsplash photos for Profile Pictures
profile_images = {
    "jane_doe": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=400&fit=crop&q=80",
    "alexander": "https://images.unsplash.com/photo-1599566150163-29194dcaad36?w=400&fit=crop&q=80",
    "sam_smith": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&fit=crop&q=80",
    "emma_w": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=400&fit=crop&q=80",
    "john_doe": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&fit=crop&q=80"
}

# Realistic Unsplash photos for feed posts
feed_images = [
    "https://images.unsplash.com/photo-1472214103451-9374bd1c798e?w=800",
    "https://images.unsplash.com/photo-1506744626753-eda8151a7474?w=800",
    "https://images.unsplash.com/photo-1523731407965-2430cd12f5e4?w=800"
]

captions = [
    "Enjoying the beautiful outdoors today! Nature is amazing. 🌲✨",
    "A stunning view that takes my breath away. #landscape #photography",
    "Living my best life in this wonderful setting. Peace and tranquility. 🌊"
]

profiles = list(Profile.objects.all())

if not profiles:
    print("No profiles found. Seed users first.")
else:
    # Ensure media directory exists
    os.makedirs('media/images', exist_ok=True)
    os.makedirs('media/profile_images', exist_ok=True)
    
    # 1. Update Profile Pictures
    for profile in profiles:
        username = profile.user.username.lower()
        if username in profile_images:
            img_url = profile_images[username]
            print(f"Downloading profile picture for {username}...")
            result = urllib.request.urlretrieve(img_url)
            with open(result[0], 'rb') as f:
                profile.profileimg.save(f'{username}_profile.jpg', File(f), save=True)
                
    # 2. Create Feed Posts
    for i, url in enumerate(feed_images):
        # assign posts to the first few profiles
        profile = profiles[i % len(profiles)]
        
        print(f"Downloading feed post image {i+1}...")
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

print("Successfully seeded realistic profile pictures and feed posts!")
