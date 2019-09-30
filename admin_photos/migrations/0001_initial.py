# Generated by Django 2.2.1 on 2019-09-28 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_count', models.IntegerField(default=0)),
                ('checked_date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
