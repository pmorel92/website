# Generated by Django 2.0.3 on 2018-07-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_meeting_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='date',
            field=models.DateField(default='2018-07-31'),
        ),
    ]
