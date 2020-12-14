from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    # path('area/<str:area>/', views.AreaView.as_view(), name='area'),
    path('bazaar', views.BazaarView.as_view(), name='bazaar_top'),
    path('fantasy', views.FantasyView.as_view(), name='fantasy_top')
]