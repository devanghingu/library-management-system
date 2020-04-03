from django.contrib import admin

from .models import Books
from .models import Category
from .models import Transaction
from .models import WaitingTransaction

# Register your models here.
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(WaitingTransaction)
