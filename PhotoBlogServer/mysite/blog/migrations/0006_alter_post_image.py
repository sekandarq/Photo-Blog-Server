# Generated by Django 3.2.25 on 2024-11-17 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20241015_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog_image/%Y/%m/%d/'),
        ),
    ]
