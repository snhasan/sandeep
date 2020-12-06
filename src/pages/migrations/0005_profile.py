# Generated by Django 2.0.7 on 2020-07-17 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('email_1', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_2', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_1', models.CharField(blank=True, max_length=120, null=True)),
                ('phone_2', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
