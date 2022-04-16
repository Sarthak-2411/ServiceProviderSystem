# Generated by Django 3.1.7 on 2021-06-28 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('provider_name', models.CharField(max_length=20)),
                ('customer_phone', models.CharField(max_length=10)),
                ('provider_phone', models.CharField(max_length=10)),
                ('service_type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('complete_within', models.CharField(max_length=20)),
                ('date_requested', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_completed', models.DateTimeField(default=None)),
                ('bill', models.CharField(max_length=10)),
                ('accepted', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('status', models.CharField(default='Requested', max_length=20)),
            ],
        ),
    ]
