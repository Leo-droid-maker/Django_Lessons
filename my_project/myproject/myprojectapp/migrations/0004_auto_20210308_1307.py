# Generated by Django 3.1.7 on 2021-03-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0003_auto_20210308_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='popular product'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(default=False, verbose_name='popular product'),
        ),
    ]
