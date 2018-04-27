from django.db import models
from django.utils import timezone

# teste lrm
from django.db import connection


class Post(models.Model):
	people = models.Manager()
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

	def testa_exec_raw(self):
		with connection.cursor() as cursor:
			cursor.execute(' SELECT p.id, p.question, p.poll_date, COUNT(*) FROM polls_opinionpoll p, polls_response r')
			cursor.execute('SELECT p.id = r.poll_id GROUP BY p.id, p.question, p.poll_date')
			Post.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
			Post.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
			result_list = []
			for row in cursor.fetchall():
				p = self.model(id=row[0], question=row[1], poll_date=row[2])
				p.num_responses = row[3]
				result_list.append(p)
		return result_list
	
	def testa_exec(self):
		connection.cursor().execute(' SELECT p.id, p.question, p.poll_date, COUNT(*) FROM polls_opinionpoll p, polls_response r')
		connection.cursor().execute(' SELECT p.id, p.question, p.poll_date, COUNT(*) FROM polls_opinionpoll p, polls_response r')
		
		with connection.cursor() as cursor:
			cursor.execute(' SELECT p.id, p.question, p.poll_date, COUNT(*) FROM polls_opinionpoll p, polls_response r')
			cursor.execute('SELECT p.id = r.poll_id GROUP BY p.id, p.question, p.poll_date')
			result_list = []
			for row in cursor.fetchall():
				p = self.model(id=row[0], question=row[1], poll_date=row[2])
				p.num_responses = row[3]
				result_list.append(p)
		return result_list

	def testa_raw(self):
		with connection.cursor() as cursor:
			Post.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
			Post.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
			result_list = []
			for row in cursor.fetchall():
				p = self.model(id=row[0], question=row[1], poll_date=row[2])
				p.num_responses = row[3]
				result_list.append(p)
		return result_list

class test_fr(models.Model):

	people = models.Manager()
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

	def testa_fr(self):
		Post.objects.raw('SELECT last_name, birth_date, first_name, id FROM myapp_person')
		return result_list
