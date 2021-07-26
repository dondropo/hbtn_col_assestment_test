"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from models.user.views import sign_in, sign_up, home, create, update, user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', sign_in, name='login'),
    path('sign_up/', sign_up, name='sign_up'),
    path('home/', home, name='home'),
    path('home/user/create/', create, name='create'),
    path('home/user/update/', update, name='update'),
    path('home/user/', user, name='user')
]
