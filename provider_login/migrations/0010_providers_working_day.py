# Generated by Django 3.1.7 on 2021-06-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider_login', '0009_auto_20210627_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='working_day',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
