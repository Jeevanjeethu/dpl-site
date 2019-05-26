"""dplsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from dpl import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('blr1/', views.blr1),
    path('blr1pg2/', views.blr1pg2),
    path('blr2/', views.blr2),
    path('blr2pg2/', views.blr2pg2),
    path('blr2pg3/', views.blr2pg3),
    path('schedules/', views.schedules),
    path('hyd/', views.hyd),
    path('fun/', views.fun),
    path('ptblr1/', views.spa_pointstableblr1),
    path('ptblr2/', views.spa_pointstableblr2),
    path('pthyd/', views.spa_pointstablehyd),
    path('show/', views.show)
]
