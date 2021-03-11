# Generated by Django 3.1.7 on 2021-03-06 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='page name')),
                ('description', models.TextField(blank=True, verbose_name='description of page')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='category name')),
                ('description', models.TextField(blank=True, verbose_name='description of page')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='product name')),
                ('image', models.ImageField(blank=True, upload_to='products_images')),
                ('short_desc', models.CharField(blank=True, max_length=64, verbose_name='short description')),
                ('description', models.TextField(blank=True, verbose_name='full description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='quantity')),
                ('size', models.CharField(blank=True, max_length=4, verbose_name='size')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprojectapp.productcategory')),
            ],
        ),
    ]
