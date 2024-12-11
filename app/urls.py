from django.urls import path
from .import views

urlpatterns = [
     path('',views.display,name='home'),
     path('one/<int:pk>',views.details,name='details'),
     path('edit/<int:jp>',views.update,name='edit'),
     path('add',views.create,name='add'),
]