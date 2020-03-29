from django.shortcuts import render,redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Books , Transaction,WaitingTransaction

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
        bookavailable=Books.objects.filter(id=kwargs['book_id'],quantity__gt=0)
        book=request.POST.get("bookid", "")
        print(book)
        if bookavailable.count():
            # check book already taken or not 
            bookexist=Transaction.objects.filter(issue_by=request.user,return_date=None,book=bookavailable.get())
            if bookexist:
                messages.warning(request,"book already issue by you. one book cannot issue multiple at a times ")
                return redirect('books')
            bookavailable=bookavailable.get()
            Transaction.objects.create(book=bookavailable,issue_by=request.user)
            bookavailable.quantity-=1
            bookavailable.save()
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

class MybookcancelCBV(View):
    def get(self,request,*args, **kwargs):
        #check transection exist or not 
        transation_exist=Transaction.objects.filter(issue_by=request.user,issue_date=None,id=kwargs['book_id'])
        if transation_exist.count():
            return render(request,'book_cancel.html',{'trans':transation_exist.get()})
        else:
            messages.error(request,"book's transaction does not exist.!!")
            return redirect('mybooks')
    def post(self,request,*args, **kwargs):

        transation_exist=Transaction.objects.filter(issue_by=request.user,issue_date=None,id=kwargs['book_id'])
        if transation_exist.count():
            transation_exist=transation_exist.get()
            book1=Books.objects.filter(id=transation_exist.book.id).get()
            book1.quantity+=1
            transation_exist.delete()
            book1.save()
            messages.success(request,'Transaction deleted ')
            return redirect('mybooks')
        else:
            return redirect('mybooks')
class MybookreturnCBV(View):
    def get(self,request,*args, **kwargs):
        transation_exist=Transaction.objects.filter(issue_by=request.user,return_date=None,id=kwargs['book_id'])
        if transation_exist.count():
            return render(request,'book_return.html',{'trans':transation_exist.get()})
        else:
            messages.error(request,"book's transaction does not exist.!!")
            return redirect('mybooks')
    def post(self,request,*args, **kwargs):
        transation_exist=Transaction.objects.filter(issue_by=request.user,return_date=None,id=kwargs['book_id'])
        if transation_exist.count():
            transation_exist=transation_exist.get()
            transation_exist.return_date=timezone.now()

            book1=Books.objects.filter(id=transation_exist.book.id).get()
            book1.quantity+=1
            book1.save()
            transation_exist.delete()

            return redirect('mybooks')
        else:
            messages.error(request,"book's transaction does not exist.!!")
            return redirect('mybooks')
class PastTransactionCBV(View):
    def get(self,request,*args, **kwargs):
        transation_exist= Transaction.objects.filter(issue_by=request.user, return_date__isnull=False)
        if transation_exist:
            return render(request,'book_return_transaction.html',{'tran':transation_exist})