import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Message
from django.contrib.auth.models import User

try:
    # Assuming 'sanjana' is the main user. 
    # Fallback to the first superuser if not found.
    me = User.objects.filter(username='sanjana').first()
    if not me:
        me = User.objects.first()
        
    jane = User.objects.filter(username='jane_doe').first()
    liam = User.objects.filter(username='liam_k').first()
    
    if me and jane:
        print(f"Adding messages between {me.username} and {jane.username}...")
        # Chat with Jane
        Message.objects.create(sender=jane, receiver=me, body="Hey! Did you see my new post?")
        time.sleep(1)
        Message.objects.create(sender=me, receiver=jane, body="Yes! The photos look absolutely amazing! Where did you take them?")
        time.sleep(1)
        Message.objects.create(sender=jane, receiver=me, body="Thanks! ❤️ I took them at the new botanical gardens downtown.")
        time.sleep(1)
        Message.objects.create(sender=me, receiver=jane, body="Oh I need to go there! We should definitely plan a trip together soon.")
        time.sleep(1)
        Message.objects.create(sender=jane, receiver=me, body="For sure! Let me know when you're free this weekend.")
        
    if me and liam:
        print(f"Adding messages between {me.username} and {liam.username}...")
        # Chat with Liam
        Message.objects.create(sender=liam, receiver=me, body="Are we still on for the project meeting tomorrow?")
        time.sleep(1)
        Message.objects.create(sender=me, receiver=liam, body="Yep! 10 AM works perfectly for me. See you then.")
    
    print("Mock messages successfully added!")
except Exception as e:
    print(f"Error adding messages: {e}")
