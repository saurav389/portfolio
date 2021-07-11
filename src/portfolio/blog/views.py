from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost
from .blogform import BlogPostModelForm

# Create your views here.
def PublicBlog(request):
	qs = BlogPost.objects.all()
	context = {"object_list":qs}
	return render(request,"blog/bloghome.html",context)
def BlogPostHome(request):
	qs = BlogPost.objects.filter(user=request.user)
	context={"object_list":qs}
	return render(request,"post.html",context)

def BlogPostView(request,slug):
	try:
	    qs = BlogPost.objects.filter(slug=slug,user=request.user).exists()
	except:
	    qs = BlogPost.objects.filter(slug=slug)
	    context = {"object_list":qs,"value":False}
	    return render(request,"blog/blogview.html",context)
	if qs is False:
		query = BlogPost.objects.filter(slug=slug)
		obj = get_object_or_404(BlogPost,slug=slug)
		form = BlogPostModelForm(request.POST or None, instance=obj)
		obj = form.save(commit=False)
		obj.views += 1
		obj.save()
		context={"object_list":query,
				 "value":False
				 }
		return render(request,"blog/blogview.html",context)
	else:
		query = BlogPost.objects.filter(slug=slug)
		context={"object_list":query,
				 "value":True}
		return render(request,"blog/blogview.html",context)



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