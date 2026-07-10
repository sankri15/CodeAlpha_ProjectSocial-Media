import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Post

dummy_locations = [
    'London, UK',
    'Mumbai, India',
    'Paris, France',
    'New York City, USA',
    'Tokyo, Japan',
    'Sydney, Australia',
    'Dubai, UAE',
    'Bali, Indonesia',
    'Rome, Italy'
]

try:
    posts = Post.objects.all()
    count = 0
    for post in posts:
        # Update if location is empty or looks weird
        if not post.location or post.location.lower() == 'explore page':
            post.location = random.choice(dummy_locations)
            post.save()
            count += 1
            
    print(f"Successfully updated {count} posts with new locations!")
except Exception as e:
    print(f"Error updating post locations: {e}")
