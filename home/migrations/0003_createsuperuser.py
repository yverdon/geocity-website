# -*- coding: utf-8 -*-
import os
from django.db import migrations


def create_superuser(apps, schema_editor):
    """ Create the admin role
    """
    from django.contrib.auth.models import User
    DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME', "default")
    DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
    DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
    DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')
    print("DJANGO_SU_NAME: {}".format(DJANGO_SU_NAME))
    
    superuser = User.objects.create_superuser(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD)

    superuser.save()



def remove_superuser(apps, schema_editor):
    """ Delete the admin role
    """
    from django.contrib.auth.models import User
    DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME', "default")
    DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
    DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
    DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')
    superuser = User.objects.filter(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD
    )

    superuser.delete()


class Migration(migrations.Migration):

    run_before = [
        ('wagtailcore', '0053_locale_model'),
    ]

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.RunPython(create_superuser, remove_superuser),
    ]
