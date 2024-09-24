
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_form, name="user_insert"),
    path('<int:id>/', views.user_form, name="user_update"),
    path('delete/<int:id>/', views.user_delete, name="user_delete"),
    path('table/', views.user_table, name="user_table"),
]
