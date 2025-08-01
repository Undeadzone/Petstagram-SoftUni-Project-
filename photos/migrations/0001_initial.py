# Generated by Django 4.2.21 on 2025-06-17 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_pets_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('tagged_pet', models.ManyToManyField(to='pets.pets')),
            ],
        ),
    ]
