# Generated by Django 3.2.25 on 2024-10-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog_image/default_error.jpg', upload_to='blog_image/%Y/%m/%d/'),
        ),
    ]