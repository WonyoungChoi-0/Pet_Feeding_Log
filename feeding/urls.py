from django.urls import path, include
from feeding import views

app_name = 'feeding'

urlpatterns = [
    path('my_pets/', views.index, name='index'),
    path('<int:pk>/', views.delete, name='delete'),
    path('edit_pet/<int:pk>/', views.edit_pet, name='edit_pet'),
    path('edit_entry/<int:pk>/', views.edit_entry, name="edit_entry"),
    path('feeding_schedule/<int:pk>/', views.feeding_schedule, name='feeding_schedule'),
    path('edit_pet/', views.edit_pet, name='edit_pet'),
    path('register_pet/', views.register_pet, name='register_pet'),
    path('register/', views.register, name='register'),
    path('', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
