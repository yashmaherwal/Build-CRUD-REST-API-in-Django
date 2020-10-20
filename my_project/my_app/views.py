from django.shortcuts import render
from django.http import request, JsonResponse
from .models import Employee
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import EmployeeSerializer
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
        # data = {"response":list(obj.values("id", "name"))}
        serializer_obj = EmployeeSerializer(obj, many=True)

        return Response(serializer_obj.data)    

    def post(self, request):
        # name = request.data["name"]
        
        # obj = Employee(name=name)
        # obj.save()
        # data = {'response':{'id':obj.id, 'name':obj.name}}
        # return Response(data)
        data = request.data
        serializer_obj = EmployeeSerializer(data = data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors)

class UpdateEmployee(APIView):

    def get_object(self, id):
        try:
            obj = Employee.objects.get(id=id)
            return obj
        except Employee.DoesNotExist:
            raise Http404

    def put(self, request, id):
        data = request.data
        obj = Employee.objects.get(id=id)
        serializer_obj = EmployeeSerializer(obj,data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializaer_obj.errors)
        
    def delete(self, request, id):
        obj = Employee.objects.get(id=id)
        obj.delete()
        return Response({"response": "Employee is successfully deleted."})





