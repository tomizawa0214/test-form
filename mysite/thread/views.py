from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, FormView, DetailView, TemplateView
from django.urls import reverse_lazy

from . forms import TopicModelForm, TopicForm
from . models import Topic

def topic_create(request):
    template_name = 'thread/create_topic.html'
    ctx = {}
    if request.method == 'GET':
        form = TopicForm()
        ctx['form'] = form
        return render(request, template_name, ctx)
    
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            topic = Topic()
            cleaned_data = topic_form.cleaned_data
            topic.title = cleaned_data['title']
            topic.message = cleaned_data['message']
            topic.user_name = cleaned_data['user_name']
            topic.category = cleaned_data['category']
            topic.save()   
            return redirect(reverse_lazy('base:top'))
        else:
            ctx['form'] = topic_form
            return render(request, template_name, ctx)

class TopicTemplateView(TemplateView):
    template_name = 'thread/detail_topic.html'
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['topic'] = get_object_or_404(Topic, id=self.kwargs.get('pk', ''))
        return ctx

class TopicDetailView(DetailView):
    template_name = 'thread/detail_topic.html'
    model = Topic
    context_object_name = 'topic'