from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article
from django.shortcuts import render

class ArticleList(ListView):
    model = Article
    paginate_by = 5
    ordering = ['-id']

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'password', 'author', 'content']
    success_url = reverse_lazy('index')

class ArticleDetail(DetailView):
    model = Article



class ArticleUpdate(UpdateView):
    model = Article
    fields = ['title', 'password', 'author', 'content']
    success_url = reverse_lazy('index')

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('index')

def Lock(request, id):
    post = Article.objects.get(id=id)
    return render(request, 'Board/lock.html', {'id': id})


