# Generated by Django 2.2.1 on 2019-09-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_blogs_short_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='number_views',
            field=models.IntegerField(default=0),
        ),
    ]
