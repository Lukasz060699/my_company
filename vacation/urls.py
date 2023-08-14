from django.urls import path

from .views import *

urlpatterns = [
    path('', getAll, name="vacation"),
    path('add/', addNew, name="add_vacation"),
    path('edit/<int:pk>', editItem, name="edit_vacation"),
    path('delete/<int:pk>', deleteItem, name="delete_vacation"),
]
