from rest_framework import serializers
from .models import Meals,Rating




class Mealserializers(serializers.ModelSerializer):
    class Meta:
        model=Meals
        fields='__all__'
        

class Rateserializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'