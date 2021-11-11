import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import *
from os import EX_CANTCREAT
from .models import Register, Themes,ServiceType,Service,FacilityType,Facility,User,BusinessType
from rest_framework import status
from django.db.models.query_utils import Q
class HelloWorld(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content)

class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {
            "username": request.user.username,
            "password": request.user.password,
        }
        return Response(content)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            }
        )


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.method == "DELETE":
        # user.delete()
        user.is_active = False
        user.save()
        return Response({"message": "User deleted"})


class DomainRegister(APIView):
   def get(self,request):
        register = Register.objects.all()
        serializer = DomainRegisterSerializer(register, many=True)
        return Response(serializer.data)

   def post(self, request):
        serializer = DomainRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class checkAvailability(APIView):

    def get(self, request):
        res = Register.objects.filter(subdomain=request.GET['name'])
        if len(res) == 0:
            return Response('Available', status=status.HTTP_200_OK)
        else:
            return Response('Not available', status=status.HTTP_200_OK)

class ThemesAPI(APIView):

    def get(self, request):
        restaurants = Themes.objects.all()
        serializer = ThemeSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ThemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessTypes(APIView):
    def get(self,request):
        register = BusinessType.objects.all()
        serializer = BusinessTypeSerializer(register, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BusinessTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Servicetype(APIView):

    def get(self, request):
        restaurants = ServiceType.objects.all()
        serializer = ServiceTypeSerializer(restaurants, many=True)
        return Response(serializer.data)

    # def get(self, request,type_id):
    #     restaurants = ServiceType.objects.filter(type_id=type_id)
    #     serializer = ServiceTypeSerializer(restaurants, many=True)
    #     return Response(serializer.data)

    def post(self, request):
        serializer = ServiceTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,type_id,format=None):
        serviceType= ServiceType.objects.filter(type_id=type_id,status=0).first()
        if serviceType==None:
            return Response({"message":'No data found'})
        serializer=ServiceTypeSerializer(serviceType,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': "0",
                                     'Message': "Service Type Successfully updated!",
                                     })
        else:
            return Response({"message":serializer.errors})
    def delete(self,request,type_id,format=None):
        serviceType= ServiceType.objects.filter(type_id=type_id,status=0).first()
        if serviceType==None:
            return Response({"message":'No data found'})
        serviceType.status=1
        serviceType.save()
        return Response({"message":'data deleted'})


class Services(APIView):

    def get(self, request):
        restaurants = Service.objects.filter(status=0).all()
        serializer = ServiceSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,service_id,format=None):
        service= Service.objects.filter(service_id=service_id,status=0).first()
        if service==None:
            return Response({"message":'No data found'})
        serializer=ServiceSerializer(service,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': "0",
                                     'Message': "Service Successfully updated!",
                                     })
        else:
            return Response({"message":serializer.errors})
    def delete(self,request,service_id,format=None):
        service= Service.objects.filter(service_id=service_id,status=0).first()
        if service==None:
            return Response({"message":'No data found'})
        service.status=1
        service.save()
        return Response({"message":'data deleted'})

class FacilityTypes(APIView):
    def get(self, request):
        restaurants = FacilityType.objects.filter(status=0).all()
        serializer = FacilityTypeSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacilityTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,facilitytype_id,format=None):
        facilityType= FacilityType.objects.filter(facilitytype_id=facilitytype_id,status=0).first()
        if facilityType==None:
            return Response({"message":'No data found'})
        serializer=FacilityTypeSerializer(facilityType,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': "0",
                                     'Message': "Facility Type Successfully updated!",
                                     })
        else:
            return Response({"message":serializer.errors})
    def delete(self,request,facilitytype_id,format=None):
        facilityType= FacilityType.objects.filter(facilitytype_id=facilitytype_id,status=0).first()
        if facilityType==None:
            return Response({"message":'No data found'})
        facilityType.status=1
        facilityType.save()
        return Response({"message":'data deleted'})

class Facilitys(APIView):

    def get(self, request):
        restaurants = Facility.objects.all()
        serializer = FacilitySerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,facility_id,format=None):
        facility= Facility.objects.filter(facility_id=facility_id,status=0).first()
        if facility==None:
            return Response({"message":'No data found'})
        serializer=FacilitySerializer(facility,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Status': "0",
                                     'Message': "Facility Type Successfully updated!",
                                     })
        else:
            return Response({"message":serializer.errors})
    def delete(self,request,facility_id,format=None):
        facility= Facility.objects.filter(facility_id=facility_id,status=0).first()
        if facility==None:
            return Response({"message":'No data found'})
        facility.status=1
        facility.save()
        return Response({"message":'data deleted'})

# class DomainRegister(APIView):
#    def get(self,request):
#         register = Register.objects.all()
#         serializer = DomainRegisterSerializer(register, many=True)
#         return Response(serializer.data)

#    def post(self, request):
#         serializer = DomainRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Register(APIView):
    # def get(self,request):
    #     register = User.objects.all()
    #     serializer = RegisterSerializer(register, many=True)
    #     return Response(serializer.data)

    def get(self,request,format=None):
        userdata=User.objects.all()
        dataarr=[]
        for userdatas in userdata:
            dict={
                "user_id":userdatas.user_id,
                "username":userdatas.username,
                "email":userdatas.email,
                "first_name":userdatas.first_name,
                "last_name":userdatas.last_name,
                "mobilephone":userdatas.mobilephone,
                "subdomain":''if str(userdatas.subdomain)=="null"else userdatas.subdomain,
                "theme":(userdatas.theme_id),
                "businesstypes":(userdatas.businesstypes_id),
                "businessname":userdatas.businessname,
                'logo':""if str(userdatas.logo)==''else str("http://127.0.0.1:8000/api/v1/media/")+str(userdatas.logo),
                'proof':""if str(userdatas.proof)==''else str("http://127.0.0.1:8000/api/v1/media/")+str(userdatas.proof),
                # "servicetype":''if str(userdatas.servicetype)=='None'else (userdatas.servicetype_id),
                # "facility":''if str(userdatas.facility)=='None'else (userdatas.facility_id),
                'status':userdatas.status,
            }
            dataarr.append(dict)
        newlist = sorted(dataarr, key=lambda k: k['username']) 
        if dataarr==[]:
            return Response({'Status': "1",
                                     'Message':'No record Found',
                                     })
        return Response({
                                     'data':newlist,
                                     })



    def post(self,request,format=None):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            # response=passwordrule(data['password'])
            # if response !=None:
            #     return Response(response)
            user_object=serializer.save()
            user_obj = User.objects.get(username=data['username'])
            return Response({'Status': "0",
                                     'Message': "User Successfully created!",
                                     "user_id ":user_obj.user_id
                                     })
        else:
            return Response({'Status': "1", 'Message': serializer.errors}, )
class SubdomainApi(APIView):
    def get(self,request,domain,format=None):
        userdata=User.objects.filter(subdomain=domain,status=0).first()
        if userdata:
            dataarr=[]
            dict={
                "user_id":userdata.user_id,
                "username":userdata.username,
                "email":userdata.email,
                "first_name":userdata.first_name,
                "last_name":userdata.last_name,
                "mobilephone":userdata.mobilephone,
                "subdomain":''if str(userdata.subdomain)=="null"else userdata.subdomain,
                "theme":userdata.theme_id,
                "businesstypes":(userdata.businesstypes_id),
                "businessname":userdata.businessname,
                'logo':""if str(userdata.logo)==''else str("http://127.0.0.1:8000/api/v1/media/")+str(userdata.logo),
                'proof':""if str(userdata.proof)==''else str("http://127.0.0.1:8000/api/v1/media/")+str(userdata.proof),
                'status':userdata.status,
            }
            dataarr.append(dict)
        else:
            return Response({'Status': "1",
                                     'Message':'No record Found',
                                     })
        return Response({
                                     'data':dataarr,
                                     })

class Registerationapprovel(APIView):
    def post(self,request,format=None):
        user_id=request.data['user_id']
        status = request.data['status']
        user= User.objects.filter(user_id=user_id).first()
        if user==None:
            return Response({"message":'No data found'})
        else:
            user.status=status
            user.save()
            return Response({'Status': "0",
                                     'Message': "Successfully updated!",
                                     })

class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            try:
                try:
                    user_obj = User.objects.get(Q(username__iexact=data['username']) | Q(email__iexact=data['username']))
                    if user_obj:
                        
                        if check_password(data['password'],user_obj.password):
                            user_obj.last_updated = datetime.datetime.now()
                            user_obj.save()
                            # token_exist = Token.objects.filter(user_id=user_obj.user_id).first()
                            # if token_exist:
                            #     token_exist.delete()
                            user = User.objects.get(username =data['username'] )
                            # token, created = Token.objects.get_or_create(user=user_obj)
                            # my_request()
                            return Response({'message': "Successfully logged_in",
                                            'status': 0,
                                            'user_id': user_obj.user_id,
                                            'first_name': user_obj.first_name,
                                            'last_name': user_obj.last_name,
                                            'mobile_phone': user_obj.mobilephone,
                                            'username': user_obj.username,
                                            'email': user_obj.email,
                                            'last_login': user_obj.last_updated,
                                            "subdomain":''if str(user_obj.subdomain)=="null"else user_obj.subdomain,
                                            "theme":(user_obj.theme_id),
                                            "businesstypes":(user_obj.businesstypes_id),
                                            "businessname":user_obj.businessname,
                                            'logo':""if str(user_obj.logo)==''else str("http://127.0.0.1:8000/media/")+str(user_obj.logo),
                                            'proof':""if str(user_obj.proof)==''else str("http://127.0.0.1:8000/media/")+str(user_obj.proof),
                                            'status':user_obj.status
                                            })
                        else:
                            return Response(
                        {'message': "Invalid Password",
                         'status': "1"})
                except Exception as e:
                    print(str(e))
                    return Response(
                        {'message': "Invalid User",
                         'status': "1"})
                if user_obj.status != 0:
                    return Response({'message': "Inactive User",
                                    'status': "1"})
            except Exception as e:
                print("Login Error:", str(e))
        else:
            return Response(serializer.errors, )
