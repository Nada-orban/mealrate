from django.shortcuts import render
from rest_framework import viewsets
from .models import Meals,Rating
from .serializers import Mealserializers,Rateserializers



class Mealviewset(viewsets.ModelViewSet):
    queryset=Meals.objects.all()
    serializer_class=Mealserializers
    
class Rateviewset(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=Rateserializers


# Create your views here.
