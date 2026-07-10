import os
import django
import urllib.request
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from django.contrib.auth.models import User
from base.models import Profile

user = User.objects.filter(username__icontains='sanjana').first()
if user:
    profile = user.profile
    url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&fit=crop&q=80"
    result = urllib.request.urlretrieve(url)
    with open(result[0], 'rb') as f:
        profile.profileimg.save('sanjana_profile.jpg', File(f), save=True)
    print("Updated sanjana profile successfully!")
else:
    print("User sanjana not found")
