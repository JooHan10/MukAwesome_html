# Generated by Django 4.2 on 2023-04-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userinfo_favorite_userinfo_mbti_userinfo_tmi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='img',
            field=models.TextField(default=''),
        ),
    ]
