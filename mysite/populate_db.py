import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','noticias')

import django
django.setup()

import random
from noticias.models import Product, Community, Notice, Image
from faker import Faker

fakegen = Faker()
