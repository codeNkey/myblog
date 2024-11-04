from django.shortcuts import render
from .models import Post, Category, Tag, Comment
from django.views.generic import DetailView, TemplateView
                                #세부정보 랜더링   
class PostDV(TemplateView):# 지정된 템플릿 랜더링
  template_name = 'blog/post_detail.html'
  