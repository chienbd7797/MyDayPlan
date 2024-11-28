from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Trang chủ
    path('login/', views.auth_page, name='login'),  # Trang đăng nhập/đăng ký
]


