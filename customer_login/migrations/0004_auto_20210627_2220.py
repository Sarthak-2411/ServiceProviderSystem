# Generated by Django 3.1.7 on 2021-06-27 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_login', '0003_auto_20210624_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='services',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
