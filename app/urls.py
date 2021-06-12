from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('area/<str:area>/', views.IndexView.as_view(), name='index'),
    path('area/<str:area>/<str:category>/', views.IndexView.as_view(), name='index'),
    # path('area/<str:area>/<str:category>/<str:attraction>/', views.IndexView.as_view(), name='index'),
    path('area/<str:area>/<str:attraction>/<str:category>/', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/preview/', views.PreviewPostView.as_view(), name='preview'),
    # path('category/<str:category>', views.CategoryView.as_view(), name='category'),
    # path('category/<str:category>/<str:area>', views.CategoryView.as_view(), name='category'),
    # path('category/<str:area>/<str:category>', views.CategoryView.as_view(), name='category'),
    path('about', views.AboutView.as_view(), name='about_top'),
    # path('mypage', views.MypageView.as_view(), name='mypage'),
    path('favorite', views.FavoriteView.as_view(), name='favorite'),
    path('mypost', views.MyPostView.as_view(), name='mypost'),
    path('category/<str:category>/', views.CategoryNameView.as_view(), name='category_name'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('like/', views.LikeView, name='like'),
]

