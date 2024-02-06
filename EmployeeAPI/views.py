from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, Employees
from .serializers import DepartmentSerializer, EmployeeSerializer


# for files storage
from django.core.files.storage import default_storage

# Create your views here.
# Curated GET API Request function Department Models
@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Added record successfully', safe=False)
        return JsonResponse('Failed to Add a record', safe=False)
    elif request.method == 'PUT':
         department_data = JSONParser().parse(request)
         department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
         department_serializer = DepartmentSerializer(department, data=department_data)
         if department_serializer.is_valid():
             department_serializer.save()
             return JsonResponse("Updated Record Successfully", safe=False)
         return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('Record deleted successfully', safe=False)
    else:
        return JsonResponse('Inavlid request', safe=False)

@csrf_exempt
def employeeAPI(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Added record successfully', safe=False)
        return JsonResponse('Failed to add record', safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeID = employee_data['EmployeeID'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Update record successfully', safe=False)
        return JsonResponse('Failed to update record', safe=False)
    
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeID = id)
        employee.delete()
        return JsonResponse('Record deleted successfully', safe=False)
    else:
        return JsonResponse('invalid request', safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)