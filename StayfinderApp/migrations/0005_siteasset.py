# Generated by Django 5.1.2 on 2024-10-19 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StayfinderApp', '0004_alter_room_room_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logos/')),
                ('instagram_icon', models.ImageField(upload_to='social_media/')),
                ('twitter_icon', models.ImageField(upload_to='social_media/')),
            ],
        ),
    ]
