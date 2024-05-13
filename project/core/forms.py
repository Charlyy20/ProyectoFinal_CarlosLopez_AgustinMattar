from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

#class CustomAuthenticationForm(AuthenticationForm):
#    class Meta:
#        model = User
#        fields = ('username', 'password')
#        widgets = {
#            'username': forms.TextInput(attrs={'class': 'input-django'}),
#            'password': forms.PasswordInput(attrs={'class': 'input-django'}),
            
#        }
        
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'input-django'})
        self.fields['password'].widget.attrs.update({'class': 'input-django'})