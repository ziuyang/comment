from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('comment/update/<int:pk>', views.comment_update, name='comment_update'),
    path('comment/delete/<int:pk>', views.comment_delete, name='comment_delete'),
    
    
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.home, name='logout'),
    path('accounts/', include('allauth.urls')),
    
]
