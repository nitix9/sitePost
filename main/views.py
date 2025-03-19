from django.shortcuts import render, redirect
from . import models
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

def index (request):
    query = request.GET.get('q')
    if query:
        posts = models.Post.objects.filter(title__icontains=query)
    else: posts = models.Post.objects.all() 
    paginator = Paginator(posts, 5) 

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number) 
    return render(request, 'main/index.html', {'posts': page_obj,'query':query})

def post_detail(request, post_id):
    try:
        post = models.Post.objects.get(pk=post_id)
        comments=post.comments.all()
    except models.Post.DoesNotExist:
        raise Http404("Post does not exist")
    if request.method == "POST":
        text = request.POST.get("text")
        name = request.POST.get("name")
        if text and name: 
            models.Comment.objects.create(post=post, text=text, name=name)      
            return redirect("post_detail", post_id=post.id) 
    return render(request, "main/post.html", {"post": post,"comments":comments})
