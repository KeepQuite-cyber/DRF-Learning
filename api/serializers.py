from students.models import Student
from rest_framework import serializers
from employees.models import Employee

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        field = "__all__"