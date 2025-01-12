# Generated by Django 5.0.6 on 2024-06-29 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='real_estates', to='api.manager')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='real_estates', to='api.customer')),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='list_of_real_estates',
            field=models.ManyToManyField(related_name='managers', to='api.realestate'),
        ),
        migrations.CreateModel(
            name='RealEstateDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('square', models.FloatField(default=None)),
                ('number_of_rooms', models.IntegerField(default=None)),
                ('floor', models.IntegerField(default=None)),
                ('number_of_floors', models.IntegerField(default=None)),
                ('description', models.TextField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default=None, max_length=255)),
                ('price_per_month', models.FloatField(default=None)),
                ('price_per_day', models.FloatField(default=None)),
                ('price_per_year', models.FloatField(default=None)),
                ('real_estate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='api.realestate')),
            ],
        ),
    ]
