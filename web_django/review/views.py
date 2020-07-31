from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from web_django.settings import BASE_DIR
from .models import *
from .forms import *
import os
import datetime
import random
import mutagen
import json


def index_views(request, *args, **kwargs):
	# path = os.path.join(BASE_DIR, 'static', 'picture')
	# listdir = os.listdir(path)
	# picture_list = []
	# for i in listdir:
	# 	dic = {}
	# 	dic['path'] = os.path.join('/static', 'picture', i)
	# 	dic['name'] = i.split(".")[0]
	# 	picture_list.append(dic)

	Picture_Random_orderTime()

	# print(Picture.objects.all())
	# print(Picture.objects.all().values('name'))
	# print(Picture.objects.all().values_list('name', 'uptime'))
	# print(Picture.objects.get(id=1))
	# print(Picture.objects.get(name='简言.jpg'))	# 未匹配到会报错
	# print(Picture.objects.filter(name='简言.jpg'))

	picture_list = Picture.objects.all().order_by('-orderTime')
	# print(picture_list)

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
	path = os.path.join(BASE_DIR, 'media', 'picture', filename)
	file = open(path, 'rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	# response['Content-Type'] = 'image/jpeg'
	response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename) \
		.encode('utf-8', 'ISO-8859-1')
	return response


# 加载静态资源
def picture_views(request, *args, **kwargs):
	filename = kwargs['filename']
	# path = os.path.join('picture', '{}.jpg'.format(filename))
	obj = Picture.objects.get(name=filename)
	return render(request, 'picture.html', locals())


# 图片上传
def up_views(request, *args, **kwargs):
	if request.method == "GET":
		puf = PictureUpForm()
		return render(request, 'up.html', locals())
	else:
		# img = request.FILES['image']
		# filename = img.name

		# path = os.path.join(BASE_DIR, 'static', 'picture', filename)
		# with open(path, 'wb+') as f:
		# 	for chunk in img.chunks():
		# 		f.write(chunk)

		# dic = {
		# 	'name': filename,
		# 	'nameHead': filename.split('.')[0],
		# 	'nameTail': filename.split('.')[1],
		# 	'uptime': datetime.datetime.now(),
		# 	'path': img
		# }

		puf = PictureUpForm(request.POST, request.FILES)
		if puf.is_valid():
			words = puf.cleaned_data['words']
			file = puf.cleaned_data['file']

			dic = {
				'name': file.name,
				'nameHead': file.name.split('.')[0],
				'nameTail': file.name.split('.')[1],
				'uptime': datetime.datetime.now(),
				'path': file,
				'words': words,
			}
			# 增加的第一种方式
			# Picture.objects.create(**dic)
			# 增加的第二种方式
			obj = Picture(**dic)
			obj.save()
			obj = Picture.objects.filter(name=file.name).order_by('-uptime')[0]
			name = obj.path.name.split('/')[-1]
			obj.name = name
			obj.save()

		return redirect('/review/index')


# 删除
def delete_views(request, *args, **kwargs):
	filename = kwargs['filename']
	Picture.objects.get(name=filename).delete()
	return redirect('/review/index')


def update_views(request, *args, **kwargs):
	filename = kwargs['filename']
	if request.method == "GET":
		return render(request, 'update_words.html')


def Picture_Random_orderTime():
	flag = True  # 是否更新数据
	last = OrderTime.objects.last()
	if last:
		now = datetime.datetime.now()
		lasttime = last.uptime
		interval = datetime.datetime.timestamp(now) - datetime.datetime.timestamp(lasttime)
		if interval < 60:
			flag = False
		else:
			last.delete()

	if flag:
		picture_list = Picture.objects.all()
		for obj in picture_list:
			obj.orderTime = random.randint(1, 999)
			obj.save()
		OrderTime.objects.create(uptime=datetime.datetime.now())


def music_views_1(request, *args, **kwargs):
	path = os.path.join(BASE_DIR, 'static', 'music')
	listdir = os.listdir(path)

	listdir = [i for i in listdir if i.endswith(".mp3")]

	name = kwargs['name']

	if name == "_random_" or name not in listdir:
		name = random.choice(listdir)

	music_path = os.path.join(path, name)
	inf = mutagen.File(music_path)
	tags = inf.tags

	if kwargs['flag'] == 0:
		TIT2 = tags["TIT2"].text[0]	# 歌曲名
		TPE1 = tags["TPE1"].text[0] # 作者
		TALB = tags["TALB"].text[0] # 专辑
		name_ = 'music/' + name
		return render(request, 'music_1.html', locals())

	elif kwargs['flag'] == 1:
		img = tags['APIC:'].data
		return HttpResponse(img, content_type='image/jpeg')