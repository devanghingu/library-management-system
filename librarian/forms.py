from django import forms

from book.models import Books
from book.models import Category
from book.models import Transaction


class add_book(forms.ModelForm):
    class Meta:
        category = forms.ChoiceField(
            choices=Category.objects.all(),
            required=True,
        )
        model = Books
        fields = ["title", "author", "quantity", "category"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class":
                "form-control",
                "placeholder":
                self.fields[field].label
            })

    def clean_title(self):
        data = self.cleaned_data["title"]
        data.strip().lower().title()
        return data


class add_category(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({
            "class":
            "form-control",
            "placeholder":
            "Category Name or Title"
        })

    def clean_name(self):
        data = self.cleaned_data["name"]
        data = str(data.strip().lower())
        data = data.title()
        allCategory = Category.objects.all()
        for cat in allCategory:
            if data == cat.name.title():
                raise forms.ValidationError("Category already Exist.!")
        return data
