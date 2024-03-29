# Generated by Django 4.2.8 on 2024-01-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('icon', models.ImageField(upload_to='icon/')),
                ('descr', models.TextField(max_length=500)),
            ],
        ),
    ]
