# Generated by Django 3.2.21 on 2023-10-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='agegroup',
            name='restriction_desc',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='agegroup',
            name='restriction_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='agegroup',
            name='restriction_name',
            field=models.CharField(blank=True, max_length=54, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='cat_desc',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='condition',
            name='condition_desc',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]