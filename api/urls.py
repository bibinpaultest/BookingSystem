from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("login", views.Login.as_view(), name="login"),
    path("hello", views.HelloWorld.as_view(), name="hello-world"),
    path("user", views.UserDetails.as_view(), name="user-info"),
    path("register", views.Register.as_view(), name="register"),
    path("registerationapprovel", views.Registerationapprovel.as_view(), name="registerationapprovel"),
    path("delete/<int:id>", views.delete_user, name="user-delete"),
    path("servicetype", views.Servicetype.as_view(), name="servicetype"),
    path("businesstypes", views.BusinessTypes.as_view(), name="businesstypes"),
    path("servicetype/<int:type_id>", views.Servicetype.as_view(), name="servicetype"),
    path("service/<int:service_id>", views.Services.as_view(), name="service"),
    path("service", views.Services.as_view(), name="service"),
    path("facilitytype", views.FacilityTypes.as_view(), name="facilitytype"),
    path("facilitytype/<int:facilitytype_id>", views.FacilityTypes.as_view(), name="facilitytype"),
    path("facility/<int:facility_id>", views.Facilitys.as_view(), name="facility"),
    path("facility", views.Facilitys.as_view(), name="facility"),
    path('domain/', views.DomainRegister.as_view()),
    path('checkAvailability/', views.checkAvailability.as_view()),
    path('themes', views.ThemesAPI .as_view(),name="themes"),
    path('subdomain/<str:domain>', views.SubdomainApi.as_view(),name="subdomain")
   
   

]

