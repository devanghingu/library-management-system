from django.shortcuts import render,redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Books , Transaction

@login_required()
def index(request):
    return redirect('books')
class BooksCBView(View):
    def get(self,request,*args, **kwargs):
        context={}
        context['books']=Books.objects.all()
        return render(request,'book_all.html',context)
    def post(self,request,*args, **kwargs):
        pass
# def book_status(request):
#     bookavailable=Books.objects.filter(id=kwargs['book_id'],quantity__gt=0)

class IssueBookCBView(View):
    def get(self,request,*args, **kwargs):
        # check user book does not morethen five
        bookavailable=Books.objects.filter(id=kwargs['book_id'],quantity__gt=0)
        if bookavailable.count():
            return render(request,'book_issue.html',{'book':bookavailable.get()})
        else:
            return 
        # Transaction.objects.filter()
         
    def post(self,request,*args, **kwargs):
        bookavailable=Books.objects.filter(id=kwargs['book_id'],quantity__gt=0).excl
        book=request.POST.get("bookid", "")
        print(book)
        if bookavailable.count():
            # check book already taken or not 
            bookexist=Transaction.objects.filter(issue_by=request.user,return_date=None,book=bookavailable.get())
            if bookexist:
                messages.warning(request,"book already issue by you. one book cannot issue multiple at a times ")
                return redirect('books')
            Transaction.objects.create(book=bookavailable.get(),issue_by=request.user)
            messages.success(request,"book has been issue done")
            return redirect('books')
        else:
            # waiting model
            return 0
class MybookCBV(View):
    def get(self,request):
        allbook=Transaction.objects.filter(issue_by=request.user,return_date=None)
        return render(request,'book_user_all.html',{'mybook':allbook})
    def post(self,request):
        pass

class MybookcencalCBV(View):
    def get(self,request,*args, **kwargs):
        pass
    def post(self,request,*args, **kwargs):
        pass