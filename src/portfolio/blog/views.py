from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost, BlogComment, CommentReply
from .blogform import BlogPostModelForm, commentForm, replyForm
from django.contrib.auth.models import AnonymousUser

# Create your views here.
def PublicBlog(request):
    qs = BlogPost.objects.all().order_by('-publish_date')
    context = {"object_list":qs}
    return render(request,"blog/bloghome.html",context)
def BlogPostHome(request):
    qs = BlogPost.objects.filter(user=request.user)
    context={"object_list":qs}
    return render(request,"post.html",context)

def BlogPostView(request,slug):
    try:
        print(request.user)
        qs = BlogPost.objects.filter(slug=slug,user=request.user).exists()
    except Exception as e:
        print("in exception block",e)
        qs = BlogPost.objects.filter(slug=slug)
        qrs = BlogPost.objects.get(slug=slug)
        comnt = BlogComment.objects.filter(blog=qrs.id).order_by('-updated')
        reply = CommentReply.objects.all()
        context = {"object_list":qs,"comment":comnt,"reply":reply,"value":False}
        return render(request,"blog/blogview.html",context)
        
    if qs is False:
        print("if user not found block")
        query = BlogPost.objects.filter(slug=slug)
        qrs = BlogPost.objects.get(slug=slug)
        comnt = BlogComment.objects.filter(blog=qrs.id)
        obj = get_object_or_404(BlogPost,slug=slug)
        form = BlogPostModelForm(request.POST or None, instance=obj)
        obj = form.save(commit=False)
        obj.views += 1
        obj.save()
        reply = CommentReply.objects.all()
        context={"object_list":query,
                 "comment":comnt,
                 "reply":reply,
                 "value":False
                 }
        return render(request,"blog/blogview.html",context)
    else:
        print("if user found block")
        query = BlogPost.objects.filter(slug=slug)
        qrs = BlogPost.objects.get(slug=slug)
        comnt = BlogComment.objects.filter(blog=qrs.id)
        reply = CommentReply.objects.all()
        context={"object_list":query,
                "comment":comnt,
                "reply":reply,
                 "value":True}
        return render(request,"blog/blogview.html",context) 


def blogcomment(request,*args, **kwargs):
    comment = request.POST.get('comment')
    slug = request.POST.get('slug')
    try:
        qs = BlogPost.objects.get(slug=slug)
        print("id is",qs.id)
        form = commentForm()
        formobj = form.save(commit=False)
        formobj.blog_id = qs.id
        formobj.readername = request.user
        formobj.comment = comment
        formobj.save()
        comnt = BlogComment.objects.filter(blog=qs.id)
        blog = BlogPost.objects.filter(slug=slug)
        context = {
                "msg":"Commented succesfully",
                "comment":comnt,
                "object_list":blog}
        return render(request,"blog/blogview.html",context)
    except:
        return redirect("/blog")


    
def Reply(request):
    blogid = request.POST.get('blogid')
    commentid = request.POST.get('commentid')
    reply = request.POST.get('reply')
    form = replyForm()
    if request.method == 'POST':
        formobj = form.save(commit=False)
        formobj.blog_id =blogid
        formobj.comment_id = commentid
        formobj.replyername = request.user
        formobj.reply = reply
        formobj.save()
    blog =BlogPost.objects.get(id=blogid)
    print(blog.slug)
    return redirect(f'/blog/{blog.slug}')



@login_required
def BlogPostNew(request):
    form = BlogPostModelForm()
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form = BlogPostModelForm()

    qs = BlogPost.objects.filter(user=request.user)
    context = {"form":form,
               "object_list":qs}
    return render(request,"blog/createblog.html",context)

@login_required
def BlogPostEdit(request,slug):
    postedit = BlogPost.objects.get(slug=slug)
    if(postedit.user == request.user):
        obj = get_object_or_404(BlogPost,slug=slug)
        form = BlogPostModelForm(request.POST or None, instance=obj)
        if request.method == 'POST':
            form = BlogPostModelForm(request.POST or None, request.FILES, instance=obj)
            if form.is_valid():
                obj.save()
                form = BlogPostModelForm()
                return redirect('/blog/')

        qs = BlogPost.objects.filter(user=request.user)
        context = {"form":form,
                   "object_list":qs}
        return render(request,"blog/blogupdate.html",context)
    else:
        print(postedit.user,request.user)
        return redirect('/blog/')

def BlogPostDelete(request,slug):

    return render(request,"blog/blogdelete.html",{})