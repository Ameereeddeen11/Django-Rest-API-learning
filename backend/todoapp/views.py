import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ToDoListSerializers
from .models import ToDoList

@api_view(['GET'])
def apiOverView(response):
    api_urls = {
        'List': '/todo-list/',
        'Detail View': '/todo-detail/<int:id>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<int:id>/',
        'Delete': '/todo-delete/<int:id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def apiListView(response):
    todolist = ToDoList.objects.all()
    serializers = ToDoListSerializers(todolist, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def apiDetailView(response, id):
    todo = ToDoList.objects.get(id=id)
    serializers = ToDoListSerializers(todo, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def apiPost(request):
    serializers = ToDoListSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save() 
    return Response(serializers.data)

@api_view(['PUT'])
def apiUpdate(request, pk):
    todo = ToDoList.objects.get(id=pk)
    serializer = ToDoListSerializers(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def apiDelete(request, id):
    todo = ToDoList.objects.get(id=id)
    todo.delete()
    return Response("Item succsesfully deleted")