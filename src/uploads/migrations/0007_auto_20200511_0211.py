# Generated by Django 2.0.7 on 2020-05-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_auto_20200509_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='subject',
            field=models.CharField(choices=[('Business', 'Business'), ('Economics', 'Economics'), ('Commerce', 'Commerce'), ('Bangladesh_studies', 'Bangladesh Studies'), ('Accounting', 'Accounting'), ('Banking_Finance', 'Banking and Finance'), ('Business_Entrepreneurship', 'Business Entrepreneurship'), ('Geography', 'Geography'), ('Statistics', 'Statistics'), ('Language', 'Language'), ('Exam', 'Exam')], max_length=25),
        ),
    ]
