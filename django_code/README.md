

# 基本操作

创建项目  `django-admin startproject django-project`

启动项目  `python manage.py runserver 0.0.0.0:8000`


# 处理操作

基本的GET、POST请求处理 `path('basicHandle/', view.basicHandle)`

图片处理，直接返回并显示图片 `path(r'imgs/<str:file>/', view.imageHandle)`

输入url处理，返回请求中的url `path('<str:url>/', view.urlHandle)`

