from django import forms
from .models import Bolt

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class BoltPostForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={"placeholder":"Enter Your Bolt",
                                      "class":"form-control",
                                      }
                                    ),
                                    label=""
                           )
    
    class Meta:
        model = Bolt
        exclude = ("user",)