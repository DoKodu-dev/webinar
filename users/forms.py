from django import forms
from users.models import Entry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['title', 'image', 'content']


class MySignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MySignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']

        if commit:
            user.save()

        return user