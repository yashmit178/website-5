# Generated by Django 2.2.8 on 2020-01-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_usage', '0021_auto_20200121_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='anonymous_usages',
            field=models.BooleanField(default=False),
        ),
    ]
