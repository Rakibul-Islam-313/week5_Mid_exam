from django.urls import path
from . import views
urlpatterns = [
    path('add_user/', views.registration, name='registration_page'),
    path('user_login/', views.UserLoginView.as_view(), name='login_page'),
    path('user_logout/', views.UserLogoutView.as_view(),name='logout_page'),
    path('users_profile/', views.User_profile,name = 'profile_page'),
    path('edit_profile/', views.edit_profile,name = 'edit_profile_page')

]
