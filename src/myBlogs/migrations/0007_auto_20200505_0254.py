# Generated by Django 2.0.7 on 2020-05-04 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0006_auto_20200505_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myblog',
            name='comentor_name',
        ),
        migrations.RemoveField(
            model_name='myblog',
            name='email',
        ),
        migrations.RemoveField(
            model_name='myblog',
            name='message',
        ),
    ]