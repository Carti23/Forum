# Generated by Django 4.0.4 on 2022-06-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
