
from datetime import date
from django.core.validators import RegexValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Register(models.Model):
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    name = models.CharField(max_length=250)
    subdomain = models.CharField(max_length=250)
    theme = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Themes(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name

class ServiceType(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0,null=True, blank=True)
    def __str__(self):
        return self.name
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    type_id =  models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True, blank=True)
    stardate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    enddate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class ServiceType(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0,null=True, blank=True)
    def __str__(self):
        return self.name
class Service(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    service_id = models.AutoField(primary_key=True)
    type_id =  models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True, blank=True)
    stardate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    enddate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0,null=True, blank=True)

    def __str__(self):
        return self.name

class FacilityType(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    facilitytype_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0,null=True, blank=True)
    def __str__(self):
        return self.name
class Facility(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    facility_id = models.AutoField(primary_key=True)
    facilitytype_id =  models.ForeignKey(FacilityType, on_delete=models.CASCADE, null=True, blank=True)
    stardate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    enddate = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0,null=True, blank=True)

    def __str__(self):
        return self.name

class BusinessType(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        )
    businesstype_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0,null=True, blank=True)

    def __str__(self):
        return self.name
class User(models.Model):
    ACTIVE = 0
    INACTIVE = 1
    PRIVATE = 0
    PUBLIC = 1
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    )
    mobile_number_errors = {'required': 'Mobile number is required',
                            'invalid': 'Enter a valid 10 digit mobile number' +
                            'without spaces, + or isd code.'}
    _mobile_regex_validator = RegexValidator(regex=r"^\d{10}$",
                                             message="Phone number must be 10 digits without + or spaces.")
    email_errors = {'required': 'Email number is required',
                            'invalid': 'Enter a valid Email' +
                            'without spaces'}
    _email_regex_validator = RegexValidator(regex=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",
                                             message="Email must be Valid")
   
    
    user_id = models.AutoField(primary_key=True)
    tenent_id = models.PositiveIntegerField(unique=False,null=True, blank=True)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, null=True, blank=True)
    # servicetype = models.ForeignKey(ServiceType, on_delete=models.CASCADE, null=True, blank=True)
    # facility =  models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, blank=True)
    businesstypes=models.ForeignKey(BusinessType, on_delete=models.CASCADE, null=True, blank=True)
    businessname = models.CharField(max_length=60)
    subdomain = models.CharField(max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    email = models.CharField("Email", max_length=50,
                                     validators=[_email_regex_validator],
                                     blank=False, null=False, unique=True,
                                     error_messages=email_errors)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    mobilephone = models.CharField("Mobile Number", max_length=10,
                                     validators=[_mobile_regex_validator],
                                     blank=False, null=False, unique=True,
                                     error_messages=mobile_number_errors)
    # address =  models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(upload_to="UserImages", null=True, blank=True)
    proof = models.ImageField(upload_to="UserImages", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    password = models.CharField(max_length=1000, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1,null=True, blank=True)
    # is_active = models.BooleanField(('active'),default=True)


