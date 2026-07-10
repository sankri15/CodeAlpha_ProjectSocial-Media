import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socials.settings')
django.setup()

from base.models import Profile

bios = {
    "jane_doe": "✨ Digital Creator | 📸 Photography lover | ✈️ Wanderlust\n'Finding beauty in the little things.'",
    "alexander": "👨‍💻 Tech enthusiast & developer | ☕ Coffee addict | Building the future one line of code at a time.",
    "sam_smith": "🎵 Music is life | 🎸 Guitarist | 🌊 Ocean child\n'Let the good times roll!'",
    "emma_w": "🎨 Artist & Designer | 🌿 Plant mom | 📚 Bookworm\nCreating things that make people smile.",
    "john_doe": "🚀 Entrepreneur | 💡 Idea generator | 🏃‍♂️ Marathon runner\nPushing limits every single day.",
    "sanjana": "✨ Web Developer | 💻 Tech Lover | 🌟 Making the web a more beautiful place!"
}

profiles = Profile.objects.all()

for profile in profiles:
    username = profile.user.username.lower()
    if username in bios:
        profile.description = bios[username]
        profile.save()
        print(f"Updated bio for {username}")
    else:
        # Default bio
        profile.description = "🌟 Exploring the world of social media! | ✨ Living life to the fullest."
        profile.save()
        print(f"Updated default bio for {username}")

print("Successfully seeded fun bios for all users!")
