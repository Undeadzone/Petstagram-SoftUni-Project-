# Generated by Django 4.2.21 on 2025-05-31 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_gender_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='profile_images/user.png', upload_to='profile_images/'),
        ),
    ]
