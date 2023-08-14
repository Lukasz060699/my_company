from django.urls import path

from .views import *

urlpatterns = [
    path('', getAll, name="workSchedule"),
    path('add/', addNew, name="add_workSchedule"),
    path('edit/<int:pk>', editItem, name="edit_workSchedule"),
    path('delete/<int:pk>', deleteItem, name="delete_workSchedule"),
]
