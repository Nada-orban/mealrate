from django.urls import path,include
from rest_framework import routers
from .views import Mealviewset,Rateviewset,Userviewset

router=routers.DefaultRouter()
router.register('users',Userviewset)
router.register('meals',Mealviewset)
router.register('rating',Rateviewset)


urlpatterns = [
    path('',include(router.urls)),
  
    

    
    
]