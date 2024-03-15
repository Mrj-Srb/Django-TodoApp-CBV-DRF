from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username']

class TaskSerialiazer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id','content','is_done']
        
    
        
        

    