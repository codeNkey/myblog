from blog.models import Post,Category,Tag
def obj_to_post(obj, flag=True):# 다른파일에서도 사용할수 있게 파일 다로 생성
  post = dict(vars(obj))

  if obj.category:#값이 있으면
    post['category'] = obj.category.name
  else:
    post['category'] = 'NoCategory'
  if obj.tags:
    post['tags'] = [t.name for t in obj.tags.all()]
  else:
    post['tags'] = []
  if obj.image:
    post['image'] = obj.image.url
  else:
    post['image'] = 'https://via.placeholder.com/900x300/'
  if obj.update_date:
    post['update_date'] = obj.update_date.strftime('%Y-%m-%d %H:%M:%S')
  else:
    post['update_date'] = '9999-12-31 00:00:00'
  del post['_state'], post['category_id'], post['create_date']  
  if not flag:
    del post['tags'], post['update_date'],post['description'], post['content']

  return post
  