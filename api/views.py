from django.shortcuts import render
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET' , 'POST'])
def studentView(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True) # Why many=True , bcz students are more than one.
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer = StudentSerializer(data=request.data)
        print("Data Requested = " , request.data)
        print("serializer = " , serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentDetailView(request , pk):
    try :
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)