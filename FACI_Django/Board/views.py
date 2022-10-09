from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Article
from django.shortcuts import render
from django.db import connection

class ArticleList(ListView):
    model = Article
    paginate_by = 5
    ordering = ['-id']

class ArticleCreate(CreateView):
    model = Article
    fields = ['title', 'password', 'author', 'content', 'answer']
    success_url = reverse_lazy('index')

class ArticleDetail(DetailView):
    model = Article

class ArticleAnswer(DetailView):
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
    pw = ""
    try:
        cursor = connection.cursor()
        query = "select password from Board_article where id = "+str(id)
        result = cursor.execute(query)
        stocks = cursor.fetchall()
        connection.commit()
        connection.close()
        pw = stocks[0][0]
    except:
        connection.rollback()
        print("Failed Selecting in StockList")

    return render(request, 'Board/lock.html', {'pw': pw, 'id' : id})

def LockAnswer(request, id):
    post = Article.objects.get(id=id)
    pw = ""
    try:
        cursor = connection.cursor()
        query = "select password from Board_article where id = "+str(id)
        result = cursor.execute(query)
        stocks = cursor.fetchall()
        connection.commit()
        connection.close()
        pw = stocks[0][0]
    except:
        connection.rollback()
        print("Failed Selecting in StockList")

    return render(request, 'Board/lock_answer.html', {'pw': pw, 'id' : id})


