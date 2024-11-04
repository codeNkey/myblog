from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
  path('post/<int:pk>/', views.PostDV.as_view(), name='post_detail')
]                                  # 클래스형 뷰를 함수형 뷰로 만들어줌(get,post 호출)  
