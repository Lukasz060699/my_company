from django.urls import path

from .views import *

urlpatterns = [
    path('', getAll, name="announcements"),
    path('add/', addNew, name="add_announcements"),
    path('edit/<int:pk>', editItem, name="edit_announcements"),
    path('delete/<int:pk>', deleteItem, name="delete_announcements"),
]
