from django.shortcuts import render
from django.views import generic
from .models import Post
from django.core.mail import send_mail

# Create your views here.
def Contact(request):
    if request.method == "POST":
        message_name = request.POST['senders-name']
        message_email = request.POST['senders-email']
        message = request.POST['senders-message']

        send_mail(
            'Message from o' + message_name,
             message,
             message_email,
             ['damian_mikolajczak@icloud.com'],
             )
        
        return render(request, 'contact.html')
    else:
        return render(request,'contact.html')
    

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'entire_post.html'

