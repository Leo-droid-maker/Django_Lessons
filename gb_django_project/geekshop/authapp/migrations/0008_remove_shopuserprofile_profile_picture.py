# Generated by Django 3.1.7 on 2021-04-12 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_shopuserprofile_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopuserprofile',
            name='profile_picture',
        ),
    ]
