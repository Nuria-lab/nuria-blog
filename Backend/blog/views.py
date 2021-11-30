from typing import ContextManager
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import TemplateView
from .models import Post


class BlogHomePageView(TemplateView):
    template_name='blog/index.html'

    def get_context_data(self, **kwargs): 
        context=super().get_context_data(**kwargs)
        context['posts']=Post.postobjects.all()
        return context

# Create your views here.
