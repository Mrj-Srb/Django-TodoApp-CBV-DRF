from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from .serializers import TaskSerialiazer

# Create your views here.

class TaskListAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerialiazer

    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerialiazer

    def get_queryset(self):
        
        user = self.request.user
        queryset = Task.objects.filter(user=user)
        return queryset

    




    
    
    
    
    

