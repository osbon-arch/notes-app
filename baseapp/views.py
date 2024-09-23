from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required

from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
    return render(request,'baseapp/index.html')
@login_required
def topics(request):
    """show all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'baseapp/topics.html',context)


def topic(request,topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request,'baseapp/topic.html',context)

def new_topic(request):
    if request.method =='POST':
        form =TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('baseapp:topics')
    else:
        form = TopicForm()    
    
    return render (request,'baseapp/new_topic.html',{'form':form})   




