from django import forms

from book.models import Books
from book.models import Category
from book.models import Transaction


class add_book(forms.ModelForm):
    class Meta:
        category = forms.ChoiceField(choices=Category.objects.all(), required=True,)
        model = Books
        fields = ["title", "author", "quantity", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {"class": "form-control", "placeholder": self.fields[field].label}
            )
