import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Profile

locations = {
    'sanjana': 'New York, USA 🍎',
    'jane_doe': 'Paris, France 🗼',
    'liam_k': 'London, UK 🎡',
    'emma_w': 'Sydney, Australia 🦘',
    'olivia_w': 'Tokyo, Japan 🌸',
}

try:
    for username, loc in locations.items():
        profile = Profile.objects.filter(username=username).first()
        if profile:
            profile.location = loc
            profile.save()
            print(f"Set location for {username}")
    print("Locations updated!")
except Exception as e:
    print(e)
