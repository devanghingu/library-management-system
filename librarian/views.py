from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib import messages
from django.utils import timezone
from book.models import Books, Transaction, WaitingTransaction
from . import forms


class AddBookCBV(View):
    def get(self, request, *args, **kwargs):
        form = forms.add_book()
        context = {}
        context = {'form': form}
        return render(request, 'librarian/add_book.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.add_book(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "New book Added")
            return redirect("books")


class AllBookCBV(View):
    """ """

    def get(self, request, *args, **kwargs):
        context = {}
        # return render()

    def post(self, request, *args, **kwargs):
        pass


class AddCategoryCBV(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class AllRequest(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class Requestissue(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class Requestreturn(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class Requestreject(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class WaitingList(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class AllRequest(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass
