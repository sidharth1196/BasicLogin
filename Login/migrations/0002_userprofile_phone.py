# Generated by Django 2.2.6 on 2019-11-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='9192939495', max_length=15),
        ),
    ]
