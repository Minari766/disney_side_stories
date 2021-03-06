from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='account_signup'),
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile_edit'),
    path('mainprof/', views.MainProfView.as_view(), name='mainprof'),
    path('mypost/', views.MyPostViewTwo.as_view(), name='mypost'),
    path('guest_login/', views.guest_login, name='guest_login'),
]