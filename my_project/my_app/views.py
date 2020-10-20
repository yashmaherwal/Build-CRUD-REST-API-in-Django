from django.shortcuts import render
from django.http import request, JsonResponse
from .models import Employee
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

@csrf_exempt
@api_view(['GET'])
def EmployeeDetails(request):
    if request.method == 'GET':
        obj = Employee.objects.all()
        data = {"response":list(obj.values("id", "name"))}
        return JsonResponse(data)

    elif request.method == "POST":
        name = request.POST["name"]
        obj = Employee(name=name)
        obj.save()
        data = {'response':{'id':obj.id, 'name':obj.name}}
        return JsonResponse(data)

    
class ListEmployee(APIView):

    def get(self, request):
        obj = Employee.objects.all()
        data = {"response":list(obj.values("id", "name"))}
        return JsonResponse(data)

    def post(self, request):
        name = request.POST["name"]
        obj = Employee(name=name)
        obj.save()
        data = {'response':{'id':obj.id, 'name':obj.name}}
        return JsonResponse(data)