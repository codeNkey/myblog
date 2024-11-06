from  django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
  path('post/list/', views.ApiPostLV.as_view(), name='post_list'),#vue의 method의 반응으로 api 실행
  path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),#vue의 method의 반응으로 api 실행
  path('catetag/', views.ApiCateTagView.as_view(), name='catetag_list'),#vue의 method의 반응으로 api 실행
  
]     


