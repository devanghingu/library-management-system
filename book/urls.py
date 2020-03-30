from django.contrib import admin
from django.urls import path,re_path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('books',views.BooksCBView.as_view(),name='books'),
    path('books/issue/<int:book_id>',views.IssueBookCBView.as_view(),name='issuebook'),
    path('mybooks',views.MybookCBV.as_view(),name='mybooks'),
    path('mybooks/cancel/<int:book_id>',views.MybookcancelCBV.as_view(),name='cancel'),
    path('mybooks/return/<int:book_id>',views.MybookreturnCBV.as_view(),name='return'),
    path('mybooks/returned',views.PastTransactionCBV.as_view(),name='returned'),
    path('mybooks/queue',views.MybookWaitingCBView.as_view(),name='queue'),
    path('mybooks/queue/<int:book_id>',views.UserWaitingList.as_view(),name='userqueue'),

]