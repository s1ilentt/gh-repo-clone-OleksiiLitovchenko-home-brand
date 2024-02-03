# Generated by Django 4.2.8 on 2024-02-02 12:42

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_portfolio_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='+38(0xx)xxxxxxx', regex='^[\\+]?[(]?[0-9]{3}{)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$')])),
                ('message', models.TextField(max_length=300)),
                ('is_proctssed', models.BooleanField(default=False)),
                ('date_in', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_in',),
            },
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.TextField(default=datetime.datetime(2024, 2, 2, 14, 42, 4, 644572), max_length=50),
        ),
    ]