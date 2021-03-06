# Generated by Django 2.0.7 on 2020-05-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0002_auto_20200425_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myblog',
            name='file',
        ),
        migrations.AddField(
            model_name='myblog',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='myblog',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
