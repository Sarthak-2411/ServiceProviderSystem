# Generated by Django 3.1.7 on 2021-06-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_auto_20210627_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='about',
            field=models.CharField(default='', max_length=250),
        ),
    ]
