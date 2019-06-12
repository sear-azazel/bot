from django.urls import path

from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.2/intro/tutorial03/
app_name = 'accounts'

urlpatterns = [
    # ex: /accounts/signup/
    path('signup/', views.SignUpView.as_view(), name='signup'),
]