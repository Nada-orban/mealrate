from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Meals,Rating
from .serializers import Mealserializers,Rateserializers,Userserializers
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly




class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=Userserializers
    #no any one can make rated only authoticated people
    # authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)




class Mealviewset(viewsets.ModelViewSet):
    queryset=Meals.objects.all()
    serializer_class=Mealserializers
    #no any one can make rated only authoticated people
    # authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)
    
    
    
    
    @action(methods=['post'],detail=True)
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            # create or update
            
            
            #هنا instance كامله بترجع عشان كده لازم ارجع بالايدى وانا بعمل ال ابديت
            meal=Meals.objects.get(id=pk)
            #ده اللى الmeal بتساويه
            # here when update i want meal.id=1
            #         #{
            #     "id": 1,
            #     "title": "pancake",
            #     "body": "hi pancake"
                    # }
            
            stars=request.data['stars']
            
            user=request.user
            
            #becouse i am using tokens
            
            
            # username=request.data['username']
            # user=User.objects.get(username=username)
            
            
            
            try:
                #update
                rating=Rating.objects.get(user=user.id,meal=meal.id)
                #here i want in get (number(id) of user,number(id) of meal)
                rating.stars=stars
                rating.save()
                serializer=Rateserializers(rating,many=False)
                json={
                    'message':'meal rate update',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_202_ACCEPTED)
                
                
            except:
                #create
                rating=Rating.objects.create(user=user,stars=stars,meal=meal)
                serializer=Rateserializers(rating,many=False)
                json={
                    'message':'meal created',
                    'result':serializer.data
                }
                return Response(json,status=status.HTTP_200_OK)
            
            
        else:
            json={
                'message':'not stars found'
            }
            return Response(json,status=status.HTTP_400_BAD_REQUEST)  
            
            
            
            
            
            
            
class Rateviewset(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=Rateserializers
    
    #no any one can make rated only authoticated people
    # authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)
    
    #كده انا امنت ال update وcreate
    def update(self,request,*args, **kwargs):
        respose={
            'message':'not how you should update',
        }
        return Response(respose,status=status.HTTP_400_BAD_REQUEST)
    
    def create(self,request,*args, **kwargs):
        respose={
            'message':'not how you should create',
        }
        return Response(respose,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
