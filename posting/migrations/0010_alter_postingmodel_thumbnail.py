# Generated by Django 4.2 on 2023-04-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0009_alter_postingmodel_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postingmodel',
            name='thumbnail',
            field=models.TextField(default='https://velog.velcdn.com/images/e_elin/post/393c51bc-9fef-48a8-ae11-f47bb3e57bbc/image.png'),
        ),
    ]
