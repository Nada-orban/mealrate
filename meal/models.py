

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator





class Meals(models.Model):
    title=models.CharField(max_length=32)
    body=models.TextField(max_length=300)

    def no_of_ratings(self):
        ratings=Rating.objects.filter(meal=self)
        return len(ratings)#len( to make it number)
    
    
    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(meal=self)
        
        for x in ratings:
            sum += x.stars
            
            
        if len(ratings)>0:
            return len(ratings)
        else:
            return 0
    
    def __str__(self):
        return self.title
    
    
class Rating(models.Model):
    meal=models.ForeignKey(Meals,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    stars=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    # def __str__(self):
    #     return self.meal
    
    
    
class Meta:
    unique_together=(('user','meal'),)
    index_together=(('user','meal'),)
    
    