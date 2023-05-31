from django.db import models
from rest_framework import serializers

class Course(models.Model):
    name=models.CharField(max_length=50)
    auther=models.CharField(max_length=50)
    price=models.IntegerField()
    discount=models.IntegerField(default=0)
    duration=models.FloatField()

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'


#model serializer
class Intructor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return self.email



class Course1(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField()
    intructor=models.ForeignKey(Intructor,on_delete=models.CASCADE,related_name='courses')

from rest_framework import serializers





class IntructorSeri1(serializers.ModelSerializer):
    class Meta:
        model=Intructor
        fields='__all__'