# from django.shortcuts import render
# from blog_app.models import Post
# from django.utils import timezone
# from django.shortcuts import redirect

#using ctrl+shift+p then type sort then select sort import
from django.shortcuts import redirect, render
from django.utils import timezone

from blog_app.models import Post
from blog_app.forms import PostForm

#crud
#c=create
#r=read/retrieve
#u=update
#d=delete


#function based views
def Post_create(request):
    form=PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect("draft-list")
    return render(request,"post_create.html",{"form": form})

def post_list(request):
    posts=Post.objects.filter(published_at__isnull=False).order_by("-published_at")
    return render(request,"post_list.html",{"posts": posts},)

def post_detail(request,pk):
    post=Post.objects.get(pk=pk,published_at__isnull=False)
    return render(request,"post_detail.html",{"post": post},)

def draft_list(request):
    drafts=Post.objects.filter(published_at__isnull=True).order_by("-published_at")
    return render(request,"draft_list.html",{"drafts": drafts},)

def draft_detail(request,pk):
    draft=Post.objects.get(pk=pk,published_at__isnull=True)
    return render(request,"draft_detail.html",{"draft": draft},)


def post_update(request,pk):
    post= Post.objects.get(pk=pk)
    form=PostForm(instance=post)
    if request.method =="POST":
        form= PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            if post.published_at:
                return redirect("post-detail",post.pk)  
            else:
                return redirect("draft-detail",post.pk)      
    return render(request,"post_create.html",{"form":form})

def post_delete(request,pk):
    post=Post.objects.get(pk=pk,published_at__isnull=False)
    post.delete()
    return redirect("post-list")


def draft_delete(request,pk):
    draft=Post.objects.get(pk=pk,published_at__isnull=True)
    draft.delete()
    return redirect("draft-list")



def draft_publish(request,pk):
    draft=Post.objects.get(pk=pk,published_at__isnull=True)
    draft.published_at=timezone.now()
    draft.save()
    return redirect("post-detail",draft.pk)

