from django.shortcuts import render,redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Books, Transaction, WaitingTransaction

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
        try:
            if bookavailable.count():
                return render(request,'book_issue.html',{'book':bookavailable.get()})
            else:
                return render(request,'book_issue.html',{'book':bookavailable.get(),'message':'Book not Available at moment! Can you wait for book?'})
        except Exception as e:
            return render(request,'book_issue.html',{'message':'Book not Available at moment.! can you wait for book?'})
        
         
    def post(self,request,*args, **kwargs):
        bookavailable=Books.objects.filter(id=kwargs['book_id'],quantity__gt=0)
        book=request.POST.get("bookid", "")
        try:
            if bookavailable.count():
                 
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
                book1=Books.objects.filter(id=kwargs['book_id']).get()
                transexist=WaitingTransaction.objects.filter(book=book1,issue_by=request.user).get()
                if transexist:
                    messages.error(request,'opps you are already in waiting queue')
                    return redirect('mybooks')
                WaitingTransaction.objects.create(book=book1,issue_by=request.user)
                messages.success(request,"Your request added in queue.")
                return redirect('mybooks')
        except Exception as e:
            book1=Books.objects.filter(id=kwargs['book_id']).get()
            transexist=WaitingTransaction.objects.filter(book=book1,issue_by=request.user).get()
            if transexist:
                messages.error(request,'opps you are already in waiting queue')
                return redirect('mybooks')
            WaitingTransaction.objects.create(book=book1,issue_by=request.user)
            messages.success(request,"Your request added in queue.")
            return redirect('mybooks')
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

class MybookWaitingCBView(View):
    def get(self,request,*args, **kwargs):
        # get all books of user
        books=WaitingTransaction.objects.filter(issue_by=request.user)
        # waitinguser=[]
        # for book1 in books:
        #     waitinguser.append(WaitingTransaction.objects.filter(book=book1.book).order_by('issue_date'))
        # print(waitinguser)    
        return render(request,'book_user_waiting.html',{'books':books})
    def post(self,request,*args, **kwargs):
        pass

class UserWaitingList(View):
    def get(self,request,*args, **kwargs):
        book1=WaitingTransaction.objects.filter(id=kwargs['book_id']).get()
        waitinguser=WaitingTransaction.objects.filter(book=book1.book).order_by('issue_date')
        return render(request,'book_user_waiting_show.html',{'books':waitinguser})