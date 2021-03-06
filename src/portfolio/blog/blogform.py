from django import forms
from .models import BlogPost, BlogComment, CommentReply

class DateInput(forms.DateInput):
    input_type = 'date'
class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','slug','image','content','publish_date']
        labels = {"slug":"Category"}
        widgets = {
                    'publish_date':DateInput()

                    }
    def clean_title(self,*args,**kwargs):

        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk) # id=instance.id
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title

class commentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = '__all__'

class replyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = '__all__'