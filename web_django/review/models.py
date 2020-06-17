from django.db import models

# class Company(models.Model):
#     name = models.CharField(max_length=10)
#
# class Group(models.Model):
#     name = models.CharField(max_length=10)
#
# class Person(models.Model):
#     name = models.CharField(max_length=10)
#
# class Customer(models.Model):
#     name    = models.CharField(max_length=10)
#     person  = models.OneToOneField(Person)	# 一对一
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     groups  = models.ManyToManyField(Group)	# 多对多

# models.ForeignKey 一对多

class Picture(models.Model):
	name = models.CharField(max_length=50)
	nameHead = models.CharField(max_length=50)
	nameTail = models.CharField(max_length=50)
	uptime = models.DateTimeField()
	path = models.FileField(upload_to="picture/")
	orderTime = models.IntegerField(default=1000)
	words = models.CharField(max_length=50, default="")

	def __str__(self):
		return self.name

	def getWord(self):
		if not self.words:
			return self.nameHead
		return self.words

class OrderTime(models.Model):
	uptime = models.DateTimeField()