from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .forms import SignupForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import PostForm
from django.views.generic.list import ListView
from .models import Post
class IndexView(TemplateView):
    template_name='enroll/home.html'


class HomeView(TemplateView):
    template_name='enroll/homehtml.html'


class RegisterView(CreateView):
    form_class = SignupForm
    template_name='enroll/index.html'
    success_url = '/accounts/login/'
    

@method_decorator(login_required, name='dispatch')  
class PostView(CreateView):
    model= Post
    form_class = PostForm
    template_name='enroll/post.html'
    success_url = '/postsuccess/' 

    def get_queryset(self):
        # user = self.request.user
        user = self.request.user.is_authenticated
        return User.objects.filter(username=user)


@method_decorator(login_required, name='dispatch')            
class ProfileView(TemplateView):
    template_name='enroll/proflie.html'


class PostSuccessView(TemplateView):
    template_name='enroll/postsuccess.html'


class HomeLoginView(TemplateView):
    template_name='enroll/homelogin.html'

class PostListView(ListView):
    model = Post
    template_name='enroll/postlist.html'
    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author=user)

    
