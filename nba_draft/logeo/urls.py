from django.urls import path, include
from django.contrib import admin

from. import views
from .views import PasswordsChangeView, UserRegisterView, UserEditView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    #path('login/', views.inicio, name = 'inicio_login')
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view(template_name= 'change-password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name = 'show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name = 'edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name = 'create_profile_page')
]