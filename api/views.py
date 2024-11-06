from django.http import JsonResponse
from django.views.generic.list import BaseListView
from .utils import obj_to_post
from blog.models import Post
from django.views.generic.detail import BaseDetailView

class ApiPostLV(BaseListView):
  model = Post
  def render_to_response(self, context, **response_kwargs):# index.html의 axios.get에서 가져옴
    qs = context['object_list']
    postList = [ obj_to_post(obj, False) for obj in qs]
    return JsonResponse(data=postList, safe=False, status=200)# json타입이 아니라도 처리한다, 강제적으로 상태를 200으로 고정 하세요

class ApiPostDV(BaseDetailView):
  model = Post
  def render_to_response(self, context, **response_kwargs):
    obj = context['object']
    post = obj_to_post(obj)
    return JsonResponse(data=post, safe=True, status=200)
                
  