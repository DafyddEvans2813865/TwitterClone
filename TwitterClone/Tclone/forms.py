from django import forms
from .models import Bolt, Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class ProfilePicForm(forms.ModelForm):
    profile_image = forms.ImageField(label="Profile Picture")
    
    class Meta:
        model = Profile
        fields = ('profile_image',)

class ProfileBioForm(forms.ModelForm):
    profile_bio = forms.CharField(label="Profile Bio", widget= forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = Profile
        fields = ('profile_bio',)
    
    ##have the current bio in the text area 
    def __init__(self, *args, **kwargs):
        super(ProfileBioForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['profile_bio'].initial = self.instance.profile_bio


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
        exclude = ("user","likes",)