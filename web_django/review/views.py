from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse

from web_django.settings import BASE_DIR
import os


def index_views(request, *args, **kwargs):
	path = os.path.join(BASE_DIR, 'static', 'picture')
	listdir = os.listdir(path)
	picture_list = []
	for i in listdir:
		dic = {}
		dic['path'] = os.path.join('/static', 'picture', i)
		dic['name'] = i.split(".")[0]
		picture_list.append(dic)
	return render(request, "review_index.html", locals())


def date_views(request, *args, **kwargs):
	print(args)
	print(kwargs)
	return HttpResponse("{year}.{month}.{day} : {words}".format(**kwargs))


# 重定向
def birday_views(request, *args, **kwargs):
	print(args)
	print(kwargs)
	redirect_url = "/review/date/{year}/{month}/{day}/生日>>{words}".format(**kwargs)
	# return HttpResponseRedirect("/review/date/{year}/{month}/{day}/生日>>{words}".format(**kwargs))
	return redirect(redirect_url)


# 文件下载
def download_views(request, *args, **kwargs):
	filename = kwargs['filename']
	path = os.path.join(BASE_DIR, 'static', 'picture', '{}.jpg'.format(filename))
	file = open(path, 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	# response['Content-Type'] = 'image/jpeg'
	response['Content-Disposition'] = 'attachment;filename="{}.jpg"'.format(filename) \
		.encode('utf-8', 'ISO-8859-1')
	return response


# 加载静态资源
def picture_views(request, *args, **kwargs):
	filename = kwargs['filename']
	path = os.path.join('picture', '{}.jpg'.format(filename))
	return render(request, 'picture.html', locals())


# 图片上传
def up_views(request, *args, **kwargs):
	if request.method == "GET":
		return render(request, 'up.html')
	else:
		img = request.FILES['image']
		filename = img.name
		path = os.path.join(BASE_DIR, 'static', 'picture', filename)
		with open(path, 'wb+') as f:
			for chunk in img.chunks():
				f.write(chunk)
		redirect_url = "/review/picture/{}".format(filename.split(".")[0])
		return redirect(redirect_url)