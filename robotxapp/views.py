from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import head_thumbnail, Project, Faculty, Event, Research
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        first_part = head_thumbnail.objects.all()
        project = Project.objects.all()
        fac = Faculty.objects.all()
        event = Event.objects.all()
        res = Research.objects.all()
        
        template_name = 'index.html'
        
        context = {
			'head': first_part,
			'projects': project,
			'faculty': fac,
			'events': event,
			'res': res
		}
        
        return render(request, template_name, context)

class AboutView(TemplateView):
    template_name = 'about.html'

class ResearchView(ListView):
    model = Research
    template_name = 'research.html'
    context_object_name = 'researches'

class VisionView(TemplateView):
    template_name = 'vision.html'

class NewsView(TemplateView):
    template_name = 'news.html'

class ContactView(TemplateView):
    template_name = 'contact.html'