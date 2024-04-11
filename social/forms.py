from django import forms
from .models import Post,Profile
from .models import Comment
from django.contrib.auth.forms import PasswordResetForm
from django.forms import TextInput
# from .models import Comment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Story
from django.contrib.auth.forms import PasswordChangeForm as DjangoPasswordChangeForm

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['image']



class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['text', 'image']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }


class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )


class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'appearance-none rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline rounded-full', 'placeholder': 'Enter your new email'})
    )

    class Meta:
        model = User
        fields = ['email']


class UsernameUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'appearance-none rounded-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline rounded-full', 'placeholder': 'Enter your new username'})
    )

    class Meta:
        model = User
        fields = ['username']


class AccountDeletionForm(forms.Form):
    confirm = forms.BooleanField(label='I confirm that I want to delete my account', required=True)

class PasswordChangeForm(DjangoPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add classes and placeholders to form fields
        self.fields['old_password'].widget = TextInput(attrs={
            'class': 'border rounded-md p-2 w-full rounded-full',
            'placeholder': 'Old Password'
        })
        self.fields['new_password1'].widget = TextInput(attrs={
            'class': 'border rounded-md p-2 w-full rounded-full ',
            'placeholder': 'New Password'
        })
        self.fields['new_password2'].widget = TextInput(attrs={
            'class': 'border rounded-md p-2 w-full rounded-full ',
            'placeholder': 'Confirm New Password'
        })
