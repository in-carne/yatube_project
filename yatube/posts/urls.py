# ice_cream/urls.py
from django.urls import path
from . import views

# urlpatterns = [
#     # Главная страница
#     path('<str:user>', views.index),
#     ]


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком мороженого
    path('posts/<str:any_slug>/', views.group_posts),
    # Страница с информацией об одном сорте мороженого;
    # в качестве параметра ожидает целое положительное число или 0
    # path('posts/<pk>/', views.posts_detail),
]
