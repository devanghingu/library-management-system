from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('address','mobile')

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})
        self.fields['address'].widget.attrs.update({'rows':3})
        
class Change_passwordForm(PasswordChangeForm):

    class Meta:
        model = User
        fields= ('old_password','new_password1','new_password2')

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        for field in self.fields:
          self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})