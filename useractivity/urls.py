from django.contrib import admin
from django.urls import path,re_path, include
from . import views
urlpatterns = [
    path('profile',views.profileCBView.as_view(),name='profile'),
    path('change_password',views.ChangePasswordCBView.as_view(),name="change_password"),
]