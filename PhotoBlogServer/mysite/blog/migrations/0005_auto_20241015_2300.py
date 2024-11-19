# Generated by Django 3.2.25 on 2024-10-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog_image/default_error.png', upload_to='blog_image/%Y/%m/%d/'),
        ),
    ]