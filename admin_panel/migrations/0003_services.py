# Generated by Django 3.1.7 on 2021-06-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0002_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser', models.CharField(max_length=10)),
            ],
        ),
    ]
