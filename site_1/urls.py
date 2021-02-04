"""site_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

    # views.py에서 만든 함수를 여기서 실
"""
from django.contrib import admin
from django.urls import path
from lotto import views #lotto에서 views.py 끌어오기

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index), #views.py index fun 연결해줘! -- main domanin은 생략됨(http:121..)
    path('hello/', views.hello, name='hello_main'),
    path('lotto/',views.index,name = 'index'),
    path('lotto/new/', views.post, name = "new_lotto"),
    path('lotto/<int:lottokey>/detail/',views.detail, name='detail'),
]
