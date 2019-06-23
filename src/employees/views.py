from django.shortcuts import render
from .models import Employee


def EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'list.html'
