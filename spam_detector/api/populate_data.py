import os
import sys
import django

# Set the path to your Django project
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

# Set the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spam_detector.settings")
django.setup()

import random
from api.models import User, Contact, PhoneNumber

def create_users():
    # Create sample users
    user1 = User.objects.create(username='rain_doe', phone_number='1234567550', email='john@example.com', password='password3')
    user2 = User.objects.create(username='kane_doe', phone_number='9876543710', email='jane@example.com', password='password4')

    return [user1, user2]

def create_contacts(users):
    # Create sample contacts for each user
    for user in users:
        Contact.objects.create(user=user, name=f'{user.username}_contact3', phone_number='1111118811', email='contact3@example.com')
        Contact.objects.create(user=user, name=f'{user.username}_contact4', phone_number='2227722222', email='contact4@example.com')


if __name__ == "__main__":
    users = create_users()
    create_contacts(users)
    print("Data populated successfully.")