from django.urls import path,include
from rest_framework import routers
from .views import Mealviewset,Rateviewset

router=routers.DefaultRouter()
router.register('meals',Mealviewset)
router.register('rating',Rateviewset)


urlpatterns = [
    path('',include(router.urls)),

    
    
]