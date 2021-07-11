from django.db import models
from django.utils.text import slugify
from PIL import Image
from django.utils import timezone
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(user__username__icontains=query)
                    )

        return self.filter(lookup)

class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class BlogPost(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name ='blog')
	image   = models.ImageField(upload_to='Blog_image/%Y/%m/%d', blank=True, null=True)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	content = RichTextUploadingField(null=True,blank=True)
	views = models.IntegerField(default=0,blank=True,null=True)
	likes = models.IntegerField(default=0,blank=True,null=True)
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = BlogPostManager()

	class Meta:
	    ordering = ['-publish_date', '-updated', '-timestamp']

	def __str__(self):
	    return self.title


	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"/blog/{self.slug}/edit"

	def get_delete_url(self):
		return f"/blog/{self.slug}/delete"

	def save(self):
	    super().save()
	    img = Image.open(self.image.path)
	    if img.height>300 or img.width>300:
	        output_size = (700,300)
	        img.thumbnail(output_size)
	        img.save(self.image.path)

	#def save(self):
	#	self.slug = slugify(self.title)
	#def __str__(self):
	#	return self.title