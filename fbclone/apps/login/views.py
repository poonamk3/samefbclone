from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from .forms import SignupForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import PostForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.views.generic.edit import DeleteView
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
    # success_url = '/postsuccess/' 
    success_url = '/postlist/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(PostView,self).form_valid(form)

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
    ordering=['-created_at']
   

class MyPostView(ListView):
    model = Post
    template_name='enroll/postlist.html'
    ordering=['-created_at']
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

class PostDetailView(DetailView):
    model = Post
    template_name='enroll/detail.html'
    pk_url_kwarg = 'id'
    context_object_name = 'post'


class UpdateView(UpdateView):
    model = Post
    template_name='enroll/update.html'
    fields = ["title","image","description"]
    success_url ="/postlist/"


class DeleteView(DeleteView):
    model = Post
    template_name='enroll/delete.html'
    success_url ="/postlist/"
    
