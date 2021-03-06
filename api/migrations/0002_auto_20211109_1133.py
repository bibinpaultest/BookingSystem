# Generated by Django 3.2.9 on 2021-11-09 11:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('businesstype_id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Active'), (1, 'Inactive')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('facility_id', models.AutoField(primary_key=True, serialize=False)),
                ('stardate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Active'), (1, 'Inactive')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('facilitytype_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Active'), (1, 'Inactive')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_id', models.AutoField(primary_key=True, serialize=False)),
                ('stardate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Active'), (1, 'Inactive')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Active'), (1, 'Inactive')], default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('tenent_id', models.PositiveIntegerField(blank=True, null=True)),
                ('businessname', models.CharField(max_length=60)),
                ('subdomain', models.CharField(max_length=60, unique=True)),
                ('username', models.CharField(max_length=60, unique=True)),
                ('email', models.CharField(error_messages={'invalid': 'Enter a valid Emailwithout spaces', 'required': 'Email number is required'}, max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='Email must be Valid', regex='^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$')], verbose_name='Email')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('mobilephone', models.CharField(error_messages={'invalid': 'Enter a valid 10 digit mobile numberwithout spaces, + or isd code.', 'required': 'Mobile number is required'}, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits without + or spaces.', regex='^\\d{10}$')], verbose_name='Mobile Number')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='UserImages')),
                ('proof', models.ImageField(blank=True, null=True, upload_to='UserImages')),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Active'), (1, 'Inactive')], default=1, null=True)),
                ('businesstypes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.businesstype')),
                ('theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.themes')),
            ],
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.AddField(
            model_name='service',
            name='type_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.servicetype'),
        ),
        migrations.AddField(
            model_name='facility',
            name='facilitytype_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.facilitytype'),
        ),
    ]
