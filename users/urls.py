from django.urls import path,include
from .import views
app_name='users'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    #registrationpage
    path('register/',views.register,name='register'),
]
