from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "age","gender"]
        #  field_classes = {"username": forms.UsernameField}

class PostForm(forms.ModelForm):
    # title = forms.CharField(
    #     label="Post Title",
    #     max_length=50,
    #     required=True)
    # description = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={"rows":6}
    #     )
    # )
    # created_date =  forms.DateTimeField()

    class Meta:
        model= Post
        fields=["title","description"]