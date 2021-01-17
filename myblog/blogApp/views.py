from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Comment
from django.core.mail import send_mail
from rest_framework import  viewsets
from . import serializers
from django.contrib.auth.models import User
from django import forms



#Contact function was defind to handle HTTP methods
def post_detail(request, slug):
    template_name = 'entire_post.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def Contact(request):
    if request.method == "POST":
        message_name = request.POST['senders-name']
        message_email = request.POST['senders-email']
        message = request.POST['senders-message']
        message_recipient = request.POST['email-recipiest']

        if message_recipient=='Damian':
                mail_to = 'damian.mikolajczak@student.put.poznan.pl'
        else:
                mail_to = 'barbara.sibinska@student.put.poznan.pl'
        
        send_mail(
            'Message from ' + message_name,
            message,
            message_email,
            [mail_to],
            )
        return render(request, 'contact.html',{'message_name':message_name})
    else:
        return render(request,'contact.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'entire_post.html'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
