from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView,View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from myapp.forms import PostForm
from myapp.models import User
from myapp.forms import CustomUserCreationForm
from myapp import forms
from .models import Post
def home(request):
    count = User.objects.count()
    return render(request, "myapp/home.html", {"count": count})


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

class SignUp(CreateView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)

    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")


@login_required
def secret_page(request):
    return render(request, "myapp/demo.html")


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "myapp/demo.html"

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = "myapp/demo.html"
    
class PostView(LoginRequiredMixin,View):
    def get(self,request):
        form= PostForm()
        return render(request,"myapp/post.html",{"form":form})

    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,"myapp/post.html",{"form":form})