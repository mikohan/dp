# Generated by Django 2.2.1 on 2019-09-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20190919_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
