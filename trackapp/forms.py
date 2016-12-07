from .models import SignUp
from django import forms


class  LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = SignUp
        fields = ['id','useremail','password']
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = SignUp

        fields  = ['id','username','useremail','password','contact','designation','address']