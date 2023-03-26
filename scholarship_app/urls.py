from django.urls import path
from . import views




urlpatterns = [
    path('',views.main,name='main'),
    path('guardian',views.guardian_form,name='guardian'),
     path('school',views.school,name='school'),
     path('success',views.success,name='success'),
    
]
