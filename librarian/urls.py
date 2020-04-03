from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('addbook', views.AddBookCBV.as_view(), name='addbook'),
    path('book/delete/<int:book_id>',
         views.DeleteBook.as_view(), name='deletebook'),
    path('book/update/<int:book_id>',
         views.UpdateBook.as_view(), name='updatebook'),
    path('allbook', views.AllBookCBV.as_view(), name='allbook'),

    path('addcetagory', views.AddCategoryCBV.as_view(), name='addcategory'),
    path('category/delete/<int:cat_id>',
         views.CategoryDelete.as_view(), name='deletecategory'),
    path('allrequest', views.AllRequest.as_view(), name='allrequest'),

    path('allrequest/issue/<int:book_id>',
         views.Requestissue.as_view(), name='requestissue'),
    path('allrequest/return/', views.Requestreturn.as_view(), name='requestreturn'),
    path('allrequest/return/<int:book_id>',
         views.Requestreturn.as_view(), name='requestreturn'),
    path('allrequest/reject/<int:book_id>',
         views.Requestreject.as_view(), name='requestreject'),
    path('waitinglist', views.WaitingList.as_view(), name='waitinglist'),
]
