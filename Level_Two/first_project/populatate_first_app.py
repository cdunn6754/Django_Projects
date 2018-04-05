import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## POP script

import random
from first_app.models import AccessRecord, WebPage, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social', 'MarketPlace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):

        # get topic for entry
        top = add_topic()

        # create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fakce access record for WebPage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating.")
    populate(20)
    print("Population Complete.")
