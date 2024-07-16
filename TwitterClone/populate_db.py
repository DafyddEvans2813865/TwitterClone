import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TwitterClone.settings')
django.setup()

from django.contrib.auth.models import User
from Tclone.models import Profile, Bolt  # adjust the import according to your app name



# Create Users
def create_users():
    usernames = ['Alice', 'Bob', 'Carol', 'Dave', 'Evans','molly','Steve','Timmy','Emily','Grace']
    
    profile_images = [
        'images/alice.jpg', 'images/bob.jpg', 'images/carol.jpg', 'images/dave.jpg',
        'images/evans.jpg', 'images/molly.jpg', 'images/steve.jpg', 'images/timmy.jpg', 'images/emily.jpg','images/grace.jpg'
    ]

    bios = [
        "I love programming and enjoy exploring new technologies. In my spare time, I like to work on personal projects and contribute to open-source communities. I'm always eager to learn and share my knowledge with others.",
        "I enjoy hiking and outdoor activities. There's nothing quite like spending a weekend in the mountains or exploring a new trail. I also have a keen interest in environmental conservation and volunteer with local clean-up initiatives.",
        "Reading is my passion. I can spend hours lost in a good book, whether it's fiction, non-fiction, or poetry. I also enjoy writing and am working on my first novel. When I'm not reading or writing, I like to visit museums and art galleries.",
        "I'm a tech enthusiast and a coffee lover. I spend my days tinkering with gadgets, coding, and keeping up with the latest tech trends. On weekends, you can find me at local coffee shops, sampling different brews and working on side projects.",
        "As a developer, I am passionate about creating efficient and scalable solutions. I enjoy problem-solving and am constantly on the lookout for new challenges. In my free time, I like to engage with the developer community and attend tech meetups.",
        "Music is my life. I play the guitar and enjoy composing my own music. I'm also a big fan of live concerts and music festivals. When I'm not immersed in music, I like to explore new cuisines and try my hand at cooking.",
        "I am deeply committed to environmental conservation. I spend a lot of my time advocating for sustainable practices and participating in tree-planting drives. I believe in making a positive impact on our planet and inspiring others to do the same.",
        "Creativity is at the heart of everything I do. I love art and enjoy creating new things, whether it's painting, sculpture, or digital art. I also run a small online shop where I sell my handmade crafts. It's rewarding to see my creations bring joy to others.",
        "Fitness is my passion. I enjoy staying active and participate in various sports, including running, cycling, and swimming. I also follow a strict fitness regime and believe in the importance of a healthy lifestyle. Sharing fitness tips and motivating others is something I take pride in.",
        "I love programming and enjoy exploring new technologies. In my spare time, I like to work on personal projects and contribute to open-source communities. I'm always eager to learn and share my knowledge with others."
    ]   
    
    
    for username, image, bio in zip(usernames, profile_images, bios):
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password='password123')
            profile = Profile.objects.get(user=user)
            profile.profile_image = image
            profile.profile_bio = bio
            profile.save()

# Create Bolts
def create_bolts():
    users = User.objects.all()
    bolts_content = [
        "This is my very first bolt! I'm excited to start sharing my thoughts and ideas with everyone. Can't wait to connect with you all!",
        "sharing some of my thoughts on today's topics. I find it fascinating how technology is evolving so rapidly!",
        "Bolts are really cool! I love how they allow us to share snippets of our lives and ideas so easily.",
        "I like to share tech news and updates. Keeping up with the latest trends and breakthroughs is my passion.",
        "Hi everyone, I'm thrilled to be part of this community and looking forward to many interesting discussions!",
        "Hello. This platform seems like a great place to share insights and learn from others. Excited to get started!",
        "Greetings, I'm passionate about environmental issues and look forward to discussing them here.",
        "Hey, I love sharing creative ideas and projects. Can't wait to see what this community has to offer!",
        "Hi, I'm interested in sports and fitness, and I hope to connect with others who share the same passion!",
        "Hey, I love sharing creative ideas and projects. Can't wait to see what this community has to offer!"
    ]
    
    for user, content in zip(users, bolts_content):
        Bolt.objects.create(user=user, body=content)

# Main population function
def populate():
    create_users()
    create_bolts()
    print("Database population complete!")

if __name__ == '__main__':
    populate()
