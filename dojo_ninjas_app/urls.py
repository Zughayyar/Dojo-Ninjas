from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('table', views.table),
    path('tree', views.tree),
    path('addDojo', views.add_dojo),
    path('deleteDojo/<int:id>', views.delete_dojo),
    path('addNinja', views.add_ninja),
    path('deleteNinja/<int:id>', views.delete_ninja),
]