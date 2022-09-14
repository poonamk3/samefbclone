from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from .forms import SignupForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .forms import PostForm
class IndexView(TemplateView):
    template_name='enroll/home.html'


class HomeView(TemplateView):
    template_name='enroll/homehtml.html'

class PostSuccessView(TemplateView):
    template_name='enroll/postsuccess.html'


class RegisterView(CreateView):
    form_class = SignupForm
    template_name='enroll/index.html'
    success_url = '/accounts/login/'


class PostView(CreateView):
    form_class = PostForm
    template_name='enroll/post.html'
    success_url = '/postsuccess/'


@method_decorator(login_required, name='dispatch')            
class ProfileView(TemplateView):
    template_name='enroll/proflie.html'
    
