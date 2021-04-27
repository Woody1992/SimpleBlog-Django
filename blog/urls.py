from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.search_results, name='search'),
    path('news/', views.posts_all, name='news'),
    path('news/<slug:category_slug>/', views.category_list, name='category_list'),
    path('<slug:post>/', views.post_single, name='post_single'),
]