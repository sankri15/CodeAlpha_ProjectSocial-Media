import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from django.contrib.auth.models import User
from base.models import Profile, FollowersCount

# Create sample users
sample_names = ["jane_doe", "alexander", "sam_smith", "emma_w", "john_doe"]

for name in sample_names:
    if not User.objects.filter(username=name).exists():
        user = User.objects.create_user(username=name, password='password123', email=f'{name}@example.com')
        user.first_name = name.capitalize()
        user.save()
        
        profile, created = Profile.objects.get_or_create(user=user)
        profile.username = name
        profile.fname = name.capitalize()
        profile.save()
        print(f"Created user {name}")
    else:
        print(f"User {name} already exists.")

print("Sample users created successfully!")
