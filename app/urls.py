from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/preview/', views.PreviewPostView.as_view(), name='preview'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('category/<str:category>/', views.CategoryView.as_view(), name='category'),
    path('bazaar', views.BazaarView.as_view(), name='bazaar_top'),
    path('fantasy', views.FantasyView.as_view(), name='fantasy_top'),
    path('critter', views.CritterView.as_view(), name='critter_top'),
    path('adventure', views.AdventureView.as_view(), name='adventure_top'),
    path('about', views.AboutView.as_view(), name='about_top'),
    path('mypage', views.MypageView.as_view(), name='mypage')
]