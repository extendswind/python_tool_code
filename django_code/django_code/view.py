from django.http import HttpResponse

# 处理请求 
# 浏览器GET请求：  http://127.0.0.1:8000/basicHandle/?par1=123
def basicHandle(request):
  response = 'response'

  # GET 请求
  # 和POST请求基本类似
  if request.method == 'GET':
    print(request.body)   # 某些没有指定参数的地方用得上
    try:  # 避免参数没被指定
      response = request.GET['par1']
    except:
      print('par1 not exist')
    return HttpResponse(response)

  #  POST 请求
  elif request.method == 'POST':
    parm = request.POST  
    response = request.POST['par1']
    return HttpResponse(response)

  # 其它
  else:
      return HttpResponse('others request')
        

# 处理URL
# 函数参数的url会得到链接访问后面的url
# 如http://127.0.0.1:8000/abc，url参数会为abc
def urlHandle(request, url):
    return HttpResponse(url)


# 直接返回URL指定的图片
# 测试URL http://127.0.0.1:8000/imgs/test.png
def imageHandle(request, file):
   filepath = 'imgs_test/' + file  # 本地图片的目录
   image_data = open(filepath,"rb").read() 
   return HttpResponse(image_data,content_type="image/png") #注意旧版的资料使用mimetype,现在    已经改为content_type 


# 默认的处理
def default(request):
    return(basicHandle(request))
