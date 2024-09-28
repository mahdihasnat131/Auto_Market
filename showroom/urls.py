from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:id>/', views.user_comments, name='comments'),
    path('buy_car/<int:id>/', views.buy_car, name='buy_car'),
    path('brand/<slug:brand_slug>/', views.home, name='home_by_brand'),
]
