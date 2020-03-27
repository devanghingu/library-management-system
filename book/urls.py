from django.contrib import admin
from django.urls import path,re_path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('books',views.BooksCBView.as_view(),name='books'),
    path('books/issue/<int:book_id>',views.IssueBookCBView.as_view(),name='issuebook'),
    path('mybooks',views.MybookCBV.as_view(),name='mybooks')
]