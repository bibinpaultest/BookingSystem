from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from drf_extra_fields.fields import Base64ImageField
from .models import Register,Themes,ServiceType,Service,Facility,FacilityType,User,BusinessType
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        return user


class DomainRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ("email", "name", "subdomain", "theme",)


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = '__all__'

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityType
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(style={'inut_type':'password'})
    logo = Base64ImageField(required=False)
    proof = Base64ImageField(required=False)
    extra_kwargs = {"password": {"write_only": True}}
    class Meta:
        model = User
        fields =["username","email", "subdomain", "theme","businesstypes","businessname","email","first_name","last_name","mobilephone","password","logo","proof"]
    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            password=make_password(self.validated_data['password']),
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            mobilephone=self.validated_data['mobilephone'],
            theme = self.validated_data['theme'],
            subdomain = self.validated_data['subdomain'],
            businesstypes = self.validated_data['businesstypes'],
            businessname = self.validated_data['businessname'],
            logo = self.validated_data['logo'],
            proof = self.validated_data['proof'],
        )
        reg.save()

class BusinessTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessType
        fields = '__all__'

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'})