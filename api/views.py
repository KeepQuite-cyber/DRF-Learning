from django.shortcuts import render
from rest_framework  import mixins,generics
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer , EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
# Create your views here.

@api_view(['GET' , 'POST'])
def studentView(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True) # Why many=True , bcz students are more than one.
        return Response(serializer.data , status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer = StudentSerializer(data=request.data)
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
    
# class based views

# class Employees(APIView):
#     def get(self , request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data , status=status.HTTP_200_OK)
    
#     def post(self , request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class EmployeesDetailView(APIView):
    def get_object(self , pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request , pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def put(self , request , pk):
        serializer = EmployeeSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Employees(mixins.ListModelMixin , mixins.CreateModelMixin ,generics.GenericAPIView):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer

     def get(self,request):
         return self.list(request)
     
     def post(self , request):
         return self.create(request)


class EmployeesDetailView(mixins.RetrieveModelMixin , mixins.DestroyModelMixin , mixins.UpdateModelMixin , generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self , request , pk):
        return self.retrieve(request , pk)
    
    def put(self , request , pk):
        return self.update(request , pk)
    
    def delete(self , request , pk):
        return self.destroy(request , pk)