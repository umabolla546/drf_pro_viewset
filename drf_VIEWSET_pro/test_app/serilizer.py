from rest_framework.serializers import ModelSerializer
from .models import Employe


class Employeserilizer(ModelSerializer):
    class Meta:
        model=Employe
        fields="__all__"