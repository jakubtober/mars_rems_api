"""rest_api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.authtoken import views
from rest_app.views import (
    WelcomeView,
    SolCreateView,
    SolListAPIView,
    SolDetailView,
    SolDeleteView,
    SolUpdateView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', WelcomeView.as_view(), name='welcome'),
    path('api/sols/', SolListAPIView.as_view(), name='sols-list'),
    path('api/sols/<int:sol>/', SolDetailView.as_view(), name='sol-detail'),
    path('api/sols/create/', SolCreateView.as_view(), name='sol-detail'),
    path('api/sols/<int:sol>delete/', SolDeleteView.as_view(), name='sol-delete'),
    path('api/sols/<int:sol>/update/', SolUpdateView.as_view(), name='sol-update'),
    path('api/token-auth/', views.obtain_auth_token),
]

# auth token view tests
# request = requests.post('http://127.0.0.1:8000/api/token-auth/', data={'username': 'username', 'password': 'password'})
# {"token":"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}
# request = requests.post('http://127.0.0.1:800/api/sols/create/', headers={'Authorization': 'Token xxxxxxxxxxxxxxxxxxxxxxxxxxxx'})
# request = requests.post('http://jakubtober.pythonanywhere.com/api/sols/create/', headers={'Authorization': 'Token xxxxxxxxxxxxxxxxxx'})
