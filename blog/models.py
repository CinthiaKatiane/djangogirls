from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	
	def publish(self):

		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


def test_lrm():
    w = Post.objects.execute('SELECT * FROM exemplo')
    q = Post.objects.raw('SELECT * FROM exemplo')
    q = Post.objects.raw('SELECT * FROM exemplo')
    q = Post.objects.execute('SELECT * FROM exemplo')
    q = Post.objects.raw('SELECT * FROM exemplo')