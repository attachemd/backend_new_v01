import os
import random

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_new_v01.settings')
django.setup()

from core.models import User, Tag, Ingredient, Recipe

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


# tags = []


# def populate_tag(N=5):
#     for _ in range(N):
#         # create fake data for entry
#         fake_name = fakegen.word()
#
#         # create new movie entry
#         tag = Tag.objects.get_or_create(user=user, name=fake_name)[0]
#         tags.append(tag)
#
#
# def populate_ingredient(N=5):
#     for _ in range(N):
#         # create fake data for entry
#         fake_name = fakegen.word()
#
#         # create new movie entry
#         ingredient = Ingredient.objects.get_or_create(user=user, name=fake_name)[0]


def populate_user(n=5):
    for _ in range(n):
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


# def populate_recipe(n=1):
#     for _ in range(n):
#         title = fakegen.name()
#         time_minutes = random.randint(1, 60)
#         price = round(random.uniform(1.00, 100.00), 2)
#         link = fakegen.url()
#         pt = fakegen.text(max_nb_chars=30)
#         tagid = random.randint(1, 15)
#         ingredientid = random.randint(1, 15)
#         Tag.objects.create(
#             tags_id=tagid,
#             category_id=cid,
#             title=pt,
#             description=fake.text(max_nb_chars=100),
#             regular_price=(round(random.uniform(50.99, 99.99), 2)),
#             discount_price=(round(random.uniform(10.99, 49.99), 2)),
#         )
#         Ingredient.objects.create()
#         user = User.objects.create_user(email, password=username)
#         user.name = username
#         user.is_superuser = False
#         user.is_staff = False
#         user.save()


def populate_data():
    user = create_super_user()
    for _ in range(20):
        # create fake data for entry
        fake_name = fakegen.word()

        # create new movie entry
        tag = Tag.objects.get_or_create(
            user=user,
            name=fake_name
        )[0]
        # tags.append(tag)

    for _ in range(20):
        # create fake data for entry
        fake_name = fakegen.word()

        # create new movie entry
        ingredient = Ingredient.objects.get_or_create(
            user=user,
            name=fake_name
        )[0]

    def random_num():
        return random.randint(1, 20)

    def generate_random_recipe_attr_id(n):
        my_list = []
        for i in range(n):
            my_list.append(random_num())
        return my_list

    for _ in range(10):
        recipe_name = fakegen.text(max_nb_chars=30)
        tag_ids = generate_random_recipe_attr_id(
            random.randint(1, 10)
        )
        ingredient_ids = generate_random_recipe_attr_id(
            random.randint(1, 10)
        )
        recipe = Recipe.objects.create(
            user=user,
            # tags=[tagid],
            # ingredients=[ingredientid],
            title=recipe_name,
            time_minutes=random.randint(1, 60),
            price=round(random.uniform(1.00, 100.00), 2),
            link=fakegen.url(),
        )
        # users = User.objects.filter(email__in=emails)
        ingredients = Ingredient.objects.filter(
            # id=[ingredientid]
            id__in=ingredient_ids
        )
        tags = Tag.objects.filter(
            # id=tagid
            id__in=tag_ids
        )
        recipe.tags.set(tags)
        recipe.ingredients.set(ingredients)


if __name__ == '__main__':
    print('populating script')
    # create_super_user()
    # populate_tag(20)
    populate_user()
    populate_data()
    # populate_ingredient(20)
    print('populating complete')
