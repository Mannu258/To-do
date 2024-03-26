from django.urls import path
from .views import *

urlpatterns = [
    path('',home ,name='list'),
    path('update_task/<str:pk>/',updatetask,name="update_task"),
    path('remove/<str:pk>',remove,name='remove')
]
