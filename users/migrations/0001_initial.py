# Generated by Django 3.0.3 on 2020-02-06 18:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('company', models.CharField(max_length=30)),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.EmailField(error_messages={'unique': 'The email should be unique'}, max_length=254, unique=True)),
                ('job', models.CharField(max_length=30)),
                ('amount_users', models.IntegerField()),
                ('country', models.CharField(blank=True, max_length=35, null=True)),
                ('cp', models.CharField(max_length=5)),
                ('state', models.CharField(max_length=30)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='El formato del número debe ser 9999999999', regex='\\+?1?\\d{10}')])),
                ('password', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(message='Password doesnt comply', regex='^[A-Za-z0-9@#$]{8,16}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]