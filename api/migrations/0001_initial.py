# Generated by Django 3.2.9 on 2021-11-03 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('name', models.CharField(max_length=250)),
                ('subdomain', models.CharField(max_length=250)),
                ('theme', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('direction', models.CharField(max_length=120, verbose_name='Direction')),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
