def obj_to_post(obj, flag=True):# 다른파일에서도 사용할수 있게 파일 다로 생성
  post = dict(vars(obj))

  if obj.category:

  else:

  if obj.tags:

  else:

  if obj.image:

  else:

  if obj.update_dt:

  else:
    

  