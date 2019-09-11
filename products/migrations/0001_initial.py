# Generated by Django 2.2.1 on 2019-09-10 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('parent_id', models.IntegerField(null=True)),
                ('slug', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cross',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orig_n', models.CharField(max_length=50)),
                ('oem_n', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=100)),
                ('car', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('condition', models.BooleanField(default=True)),
                ('weight', models.FloatField(blank=True)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('real_weight', models.FloatField(blank=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Categories')),
                ('cross', models.ManyToManyField(to='products.Cross', verbose_name='cross verbose name')),
            ],
        ),
    ]
