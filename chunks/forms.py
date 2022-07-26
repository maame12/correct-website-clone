from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',  'password1', 'password2']
  
def _init_(self, *args, **kwargs):
        super(CustomUserCreationForm, self)._init_( *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
  
     

