from django.contrib import admin
from .models import Post, Category, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('id', 'category', 'tag_list', 'title', 'description', 'image', 'content', 'create_date', 'update_date', 'like')

  def tag_list(self, obj):
    return ','.join([t.name for t in obj.tags.all()])#
  
  def get_queryset(self, request):
    return super().get_queryset(request).prefetch_related('tags')
                                        # tags와 관련된 단어를 미리 셋팅을 해놓겠다(반정규화)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('id', 'post', 'short_content', 'create_date', 'update_date')