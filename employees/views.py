from django.shortcuts import render
from django.views.generic import ListView
from .models import Employee


class EmployeeListView(ListView):
    model = Employee
    # context_object_name = 'employees'
    template_name = 'employee_list.html'
