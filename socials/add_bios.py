import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Profile

bios = {
    'sanjana': "Software Developer 💻 | Coffee Addict ☕ | Love exploring new places 🌍",
    'jane_doe': "Fashion & Lifestyle Blogger ✨ | Living my best life in Paris 🥐",
    'liam_k': "Photographer 📸 | Capturing moments around the world ✈️ | London based",
    'emma_w': "Fitness enthusiast 🏋️‍♀️ | Dog mom 🐶 | Beach vibes only 🌊",
    'olivia_w': "Tech nerd 🤓 | Gamer 🎮 | Anime lover 🌸"
}

try:
    for username, bio in bios.items():
        profile = Profile.objects.filter(username=username).first()
        if profile:
            profile.description = bio
            profile.save()
            print(f"Updated bio for {username}")
    print("Successfully added bios to sample users!")
except Exception as e:
    print(f"Error adding bios: {e}")
