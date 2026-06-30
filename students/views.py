from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
# Create your views here.
def students(request):
    student = {
        "id" : 56,
        "name" : "Rahul",
        "Branch" : "IT"
    }
    return JsonResponse(student)