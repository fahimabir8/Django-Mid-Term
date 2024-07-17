from django.urls import path
from . import views

urlpatterns = [
   
    # path('login/', views.user_login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.sign_up, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
   
]
