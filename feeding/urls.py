from django.urls import path, include
from feeding import views

app_name = 'feeding'

urlpatterns = [
    path('', views.index, name='index'),
    path('feeding_schedule/', views.feeding_schedule, name='feeding_schedule'),
    path('<int:pk>/', views.delete_entry, name='delete_entry'),
]
