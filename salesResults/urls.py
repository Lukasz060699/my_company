from django.urls import path

from .views import *

urlpatterns = [
    path('', getAll, name="salesResults"),
    path('add/', addNew, name="add_salesResults"),
    path('edit/<int:pk>', editItem, name="edit_salesResults"),
    path('delete/<int:pk>', deleteItem, name="delete_salesResults"),
]
