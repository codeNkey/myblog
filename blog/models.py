from django.db import models

# 게시글                                                                                           # on_delete=models.CASCADE 참조된 객체와 외래키 같이 삭제
class Post(models.Model):                       # blank=True 사용자가 입력폼을 제공하지 않아도 무방함 # on_delete=models.SET_NULL 참조된 객체 삭제되어도 외래키 필드는 삭제안됨 null=True가 필요함
  # FK(Foreign Key)                             # null=True  데이터 베이스에 저장될때 피드가 비어 있어도 됨   
  category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL) # 카테고리가 각 포스트 마다 없어도 된다. 
  tags = models.ManyToManyField('Tag', blank=True)# 여러개의 태그를 연결할수 있으며 태그는 비워둘 수도 있다                             
  title = models.CharField('TITLE', max_length=50)
  description = models.CharField('DESCRIPTION', max_length=50, blank=True, help_text='simple one-line text') 
                                                # 최대글자수제한 #
  image =models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)                                      
  content = models.TextField('CONTENT')
  create_date = models.DateField('CREATE DT', auto_now_add=True)#한번 바뀌면 끝
  update_date = models.DateField('UPDATE DT', auto_now=True)#업데이트가 될때 마다 바뀜
  like = models.PositiveIntegerField('LIKE', default=0)#좋아요를 누르지 않으면 기본값 0

  def __str__(self):
    return self.title

# 게시글의 종류를 지정
class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)#값이 겹치면 안된다 유니크=0 여러개의 카테고리는 하나의 카테고리에 들어올수 있다
  description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text')

  def __str__(self):
    return self.name
  
# 게시글의 해시 태그
class Tag(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

# 댓글
class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)#하나의 게시물은 여러가지의 댓글을 가질수 있다 1 대 다 관계
                          #문자열로 만들면 순서에 상관없이 받아오고 클래스이름으로 입력하면 위에 존재해야 한다    
  content = models.TextField('CONTENT')
  create_date = models.DateField('CREATE DT', auto_now_add=True)
  update_date = models.DateField('UPDATE DT', auto_now=True)

  @property
  def short_content(self):
    return self.content[:10]

  def __str__(self):
    return self.short_content
