from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import messages
from django.utils import timezone
from book.models import Books, Transaction, WaitingTransaction, Category
from . import forms
from django.core import paginator
from django.utils import timezone


class AddBookCBV(View):
    def get(self, request, *args, **kwargs):
        form = forms.add_book()
        context = {}
        context = {"form": form}
        return render(request, "librarian/add_book.html", context)

    def post(self, request, *args, **kwargs):
        form = forms.add_book(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New book Added")
            return redirect("books")
        else:
            return render(request, "librarian/add_book.html", context)


class AllBookCBV(View):
    """ """

    def get(self, request, *args, **kwargs):
        books = Books.objects.all()

        return render(request, "librarian/allbook.html", {"books": books})

    def post(self, request, *args, **kwargs):
        pass


class AddCategoryCBV(View):
    def get(self, request, *args, **kwargs):
        form = forms.add_category()
        cat = Category.objects.all()
        return render(
            request, "librarian/add_category.html", {"form": form, "category": cat}
        )

    def post(self, request, *args, **kwargs):
        form = forms.add_category(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category successfully Added")
            return redirect(self.request.path_info)
        else:
            cat = Category.objects.all()
            return render(
                request, "librarian/add_category.html", {"form": form, "category": cat}
            )


class CategoryDelete(View):
    def get(self, request, *args, **kwargs):
        cat = Category.objects.filter(id=kwargs["cat_id"])
        if cat.exists():
            cat.delete()
            messages.success(request, "Category Sucessfully Deleted. ")
            return redirect("addcategory")
        else:
            messages.error(request, "Category does't found. ")
            return redirect("addcategory")


class DeleteBook(View):
    def get(self, request, *args, **kwargs):
        book = Books.objects.filter(id=kwargs["book_id"])
        if book.exists():
            book.delete()
            messages.success(request, "Book Deleted Successfully")
            return redirect("allbook")
        else:
            messages.error(request, "Book not found")


class UpdateBook(View):
    def get(self, request, *args, **kwargs):
        book = Books.objects.filter(id=kwargs["book_id"])
        if book.exists():
            form = forms.add_book(instance=book.get())
            return render(request, "librarian/add_book.html", {"form": form})
        else:
            messages.error(request, "book not exist")
            return redirect("allbook")

    def post(self, request, *args, **kwargs):
        book = Books.objects.filter(id=kwargs["book_id"])
        form = forms.add_book(request.POST or None, instance=book.get())
        if form.is_valid():
            form.save()
            messages.success(request, "Book information successfulluy updated")
            return redirect("allbook")
        else:
            messages.error(request, "opps.!! Book information not valid")
            return render(request, "librarian/add_book.html", {"form": form})


class AllRequest(View):
    def get(self, request, *args, **kwargs):
        transaction = Transaction.objects.filter(issue_date=None)
        return render(
            request, "librarian/request_all.html", {"transaction": transaction}
        )

    def post(self, request, *args, **kwargs):
        pass


class Requestissue(View):
    def get(self, request, *args, **kwargs):
        trans = Transaction.objects.filter(id=kwargs["book_id"])
        if trans.exists():
            trans = trans.get()
            trans.issue_date = timezone.now()
            messages.success(
                request, "book Successfully issue to {0}..!".format(trans.issue_by)
            )
            trans.save()
        else:
            messages.error("issue book does not exist..!!")
        return redirect("allrequest")

    def post(self, request, *args, **kwargs):
        pass


class Requestreturn(View):
    def get(self, request, *args, **kwargs):
        if "book_id" in kwargs:
            trans = Transaction.objects.filter(id=kwargs["book_id"])
            if trans.exists():
                trans = trans.get()
                trans.return_date = timezone.now()
                book = Books.objects.filter(id=trans.book.id).get()
                book.quantity += 1
                book.save()
                trans.save()
                messages.success(
                    request, "book Successfully return of {0}..!".format(trans.issue_by)
                )
            else:
                messages.success(request, "Transaction of book does not exist..!")
            return redirect("allrequest")

        else:
            transaction = Transaction.objects.filter(
                return_date=None, issue_date__isnull=False
            )
            return render(
                request,
                "librarian/request_return_all.html",
                {"transaction": transaction},
            )


class Requestreject(View):
    def get(self, request, *args, **kwargs):
        trans = Transaction.objects.filter(id=kwargs["book_id"])
        if trans.exists():
            trans = trans.get()
            book = Books.objects.filter(id=trans.book.id).get()
            trans.delete()
            book.quantity += 1
            book.save()
            messages.success(
                request, "Request of {0} succesfully removed..!!".format(trans.issue_by)
            )
        else:
            messages.error("Request does not exist..!!")
        return redirect("allrequest")


class WaitingList(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
