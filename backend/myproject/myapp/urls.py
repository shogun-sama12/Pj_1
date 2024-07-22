from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView
from .views import ArticleDetail, ArticleList, CreateArticle, UpdateArticle, DeleteArticle, ArticleApi
from rest_framework import routers

# Создайте и настройте маршрутизатор DRF
router = routers.DefaultRouter()
router.register(r'api/article', ArticleApi, basename='article')

urlpatterns = [
    # Основные пути
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    
    # Шаблоны
    path('tashak/', TemplateView.as_view(template_name='tashak.html')),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),
    path('change_password/success/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_success.html'), name='change_password_success'),
    
    # Представления статей
    path('articles/', ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('article/<int:pk>/edit/', UpdateArticle.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', DeleteArticle.as_view(), name='article_delete'),
    path('article/add_new/', CreateArticle.as_view(), name='add_article'),
    
    # Тестовый маршрут
    path('test/', views.test_view),

    # Пути для API
    path('', include(router.urls)),  # Включите маршруты DRF
]
