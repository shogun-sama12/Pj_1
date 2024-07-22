from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import RegistrationForm

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})

def profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

from django.views.generic import ListView, DeleteView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Article
class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name= 'articles'
class ArticleDetail(DeleteView):
    model = Article
    template_name ='article_detail.html'
    context_object_name='article'
class CreateArticle(CreateView):
    model = Article
    template_name = 'add_article.html'
    fields = ['title','content']
    success_url = reverse_lazy('article_list')
class UpdateArticle(UpdateView):
    model = Article
    template_name = 'update_article.html'
    fields = ['title','content']
    success_url = reverse_lazy('article_list')
class DeleteArticle(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    fields = ['title','content']
    context_object_name='article'
    success_url = reverse_lazy('article_list')

    # ------------------api--------------
from rest_framework import viewsets
from .serializers import ArticleSerializer

class ArticleApi(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    http_method_names = ['get', 'post']

from django.http import HttpResponse

def test_view(request):
    return HttpResponse('Test view working!')