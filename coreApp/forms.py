from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Enter your Tweet",
                "class": "form-control"
            }
        ),
        label="",
    )

    class Meta:
        model = Tweet
        exclude = ("user",)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Email Address'}
        )
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'First Name'}
        )
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Last Name'}
        )
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted small">'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<span class="form-text text-muted small">'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted small">'

 
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        # self.fields['email'].label = ''

        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        # self.fields['first_name'].label = ''

        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        # self.fields['last_name'].label = ''

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
