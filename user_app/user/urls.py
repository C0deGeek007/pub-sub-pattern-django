from django.urls import path
from user import views
urlpatterns = [
    path('getUsers', views.getAllUsers, name="get-users"),
    path('updateUserPermission', views.updateUser, name="update-user"),
    path('createUser', views.createUser, name="create-user"),
    path('getUserPermission', views.getUserPermission, name="get-user-permission"),  
  ]
