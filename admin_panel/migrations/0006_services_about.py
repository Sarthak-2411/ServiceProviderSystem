# Generated by Django 3.1.7 on 2021-06-27 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_auto_20210627_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='about',
            field=models.CharField(default='', max_length=50),
        ),
    ]
