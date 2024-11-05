from django.http import JsonResponse
from django.views.generic.list import BaseListView

class ApiPostLV(BaseListView):
  
  def render_to_response(self, context, **respose_kwargs):# index.html의 axios.get에서 가져옴
    qs = context['object_list']
    postList = [ obj_to_post(obj, False) for obj in qs]
    return JsonResponse(data=postList, safe=False, status=200)
                                  # 안전검사를 건너 뛰어라 안전한 데이터다, 강제적으로 상태를 200으로 고정 