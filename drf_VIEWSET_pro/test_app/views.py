from django.shortcuts import render

# Create your views here.
from .serilizer import Employeserilizer
from .models import Employe
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny

class curd_view(ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = Employeserilizer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny,]