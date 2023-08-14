from django.urls import path

from .views import *

urlpatterns = [
    path('', getAll, name="loyalityProgram"),
    path('add/', addNew, name="add_loyalityProgram"),
    path('edit/<int:pk>', getItem, name="getItem_loyalityProgram"),
    path('delete/<int:pk>', deleteItem, name="delete_loyalityProgram"),
]
