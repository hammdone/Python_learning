"""
URL configuration for todo_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.main, name='todo'), # main home
    path('remove/<int:item_id>/', views.remove, name='remove'), # remove
    path('edit/<int:item_id>/', views.edit, name='edit'),  # editing
    path('is_complete/<int:item_id>/', views.is_complete, name='is_complete'), # complete
]