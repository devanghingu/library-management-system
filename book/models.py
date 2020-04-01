from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Category(models.Model):
    """ Represent the category of books """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):
    """ Book related all information """
    title = models.CharField(max_length=230)
    author = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    issued = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    """ Number of  book issued by user """
    # STATUS = (  (0,'genarated'),  # when user make request
    #             (1,'issued'),   # when librarian relase book
    #             (2,'Return'))   # when user generate return request

    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    issue_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # when librarian accept book request
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(
        null=True, blank=True)  # when user return book
    # status =models.PositiveIntegerField(default=0,choices=STATUS)

    def __str__(self):
        return self.book.title


class WaitingTransaction(models.Model):
    """ waiting model when book is outof quantitiy """
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    issue_by = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.book.title) + str(self.issue_by)
