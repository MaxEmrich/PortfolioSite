from typing import Any
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Article

# Create your views here.
class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/index.html'
    paginate_by = 2

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 2

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists(): # does this person exit and has liked this post?
            context['liked_by_user'] = True
            return context
        return context



class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists(): # does this person exit and has liked this post?
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id) # this "remove" and "add" functions are built-in function in a many-to-many field

        article.save()
        return redirect('detail_article', pk) 
