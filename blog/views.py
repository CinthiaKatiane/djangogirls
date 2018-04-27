from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

# test_mv
from django.db import models

def test_br(request):
    for p in Post.objects.raw('SELECT * FROM IN CASE exemplo'):
        pass

class Teste_LRM(models.Manager):
    def with_counts(self):
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

    
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
