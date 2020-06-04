from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, FormView, DetailView, TemplateView

from . models import Topic


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