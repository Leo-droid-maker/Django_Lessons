# Generated by Django 3.1.7 on 2021-03-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojectapp', '0004_auto_20210308_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='new_product'),
        ),
    ]
