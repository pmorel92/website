# Generated by Django 2.0.3 on 2018-07-31 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_agency_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='url',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]
