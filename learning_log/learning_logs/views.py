from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    '''page of learning log'''
    return render(request, 'learning_logs/index.html')
    
def topics(request):
    '''show all topics'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
    
def topic(request, topic_id):
    '''show special topic and its all entries'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
    
def new_topic(request):
    '''add new topic'''
    if request.method != 'POST':
        #not post data: add a new form
        form = TopicForm()
    else:
        #post data: process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
    
def new_entry(request, topic_id):
    '''add new item for topic'''
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        #not post data: add a new form
        form = EntryForm()
    else:
        #post data: process data
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
            
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    '''editing existed item'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        #request for firstime, using present entry to fill form
        form = EntryForm(instance=entry)
    else:
        #post data: process data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)