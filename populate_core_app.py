import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_new_v01.settings')
django.setup()

from core.models import User, Tag, Ingredient

fakegen = Faker()


def create_super_user():
    user = User.objects.create_superuser(email="attachemd@gmail.com", password="1234")
    user.save()
    return user


def create_super_user2():
    user = User.objects.get_or_create(email="attachemd@gmail.com", password="1234")
    user.is_admin = True
    user.is_superuser = True
    user.is_staff = True
    user.save()
    return user


user = create_super_user()
tags = []


def populate_tag(N=5):
    for _ in range(N):
        # create fake data for entry
        fake_name = fakegen.word()

        # create new movie entry
        tag = Tag.objects.get_or_create(user=user, name=fake_name)[0]
        tags.append(tag)


def populate_ingredient(N=5):
    for _ in range(N):
        # create fake data for entry
        fake_name = fakegen.word()

        # create new movie entry
        ingredient = Ingredient.objects.get_or_create(user=user, name=fake_name)[0]


def populate_user(N=5):
    for _ in range(N):
        name = fakegen.name()
        first_name = name.split(' ')[0]
        last_name = ' '.join(name.split(' ')[-1:])
        username = first_name[0].lower() + last_name.lower().replace(' ', '')
        email = username + "@" + last_name.lower() + ".com"
        user = User.objects.create_user(email, password=username)
        user.name = username
        user.is_superuser = False
        user.is_staff = False
        user.save()


if __name__ == '__main__':
    print('populating script')
    # create_super_user()
    populate_tag(20)
    print("populate_tag: ")
    print(tags)
    populate_ingredient(20)
    populate_user()
    print('populating complete')
