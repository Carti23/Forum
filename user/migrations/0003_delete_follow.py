# Generated by Django 4.0.4 on 2022-06-09 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_profile_followers_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
