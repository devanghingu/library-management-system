from django.contrib import admin
from .models import Books,Category,Transaction,WaitingTransaction
# Register your models here.
admin.site.register(Books)
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(WaitingTransaction)


