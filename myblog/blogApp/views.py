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

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'entire_post.html'

