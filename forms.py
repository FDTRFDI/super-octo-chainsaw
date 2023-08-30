
from django import forms 
from .models import Register ,Login 

class RegistreForm(forms.ModelForm):
    class Meta:
          model=Register
          fields=('first_name','last_name','email','address', 'phone','password', 'des')
          

       


class LoginForm (forms.ModelForm):
      class Meta:
           model=Login
           fields=('name','password')

       