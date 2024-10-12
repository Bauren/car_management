from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, CommentViewSet, profile, add_car, logout_view
from . import views


router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.car_list, name='home'),
    path('add/', add_car, name='add_car'),
    path('register/', views.register, name='register'),
    path('cars/', views.car_list, name='car_list'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
]