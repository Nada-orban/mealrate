from rest_framework import serializers
from .models import Meals,Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class Userserializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','password')
        extra_kwargs={'password':{'write_only':True,'required':True}}
        
        
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
        
    
class Mealserializers(serializers.ModelSerializer):
    class Meta:
        model=Meals
        fields=('id','title','body','no_of_ratings','avg_rating')
        

class Rateserializers(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields='__all__'