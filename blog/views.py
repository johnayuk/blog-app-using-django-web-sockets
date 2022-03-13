from django.shortcuts import get_object_or_404, render,redirect
from blog.models import Message
from django.contrib import messages

# Create your views here.


def index(request):
    posts = Message.objects.order_by('-timestamp').all()[:10]
    # Message.objects.order_by('-timestamp').all()[:5]
    # return render(request, 'blog/post.html',{'posts':posts})
    return render(request, 'blog/index.html',{'posts':posts})


def delete_chat(request,pk):
    posts = Message.objects.get(id=pk)

    posts = get_object_or_404(Message, id = pk)

    if request.method == "POST":
        posts.delete()
        return redirect('posts')
    
    holder = {'posts':posts}
    return render(request, 'blog/index.html',{'posts':posts})