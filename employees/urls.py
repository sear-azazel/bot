from .views import EmployeeListView
from django.conf.urls import include, url

urlpatterns = [
    url('list', EmployeeListView.as_view()),
]
