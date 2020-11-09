from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import head_thumbnail, Project, Faculty, Event, Research, Research_head, Vision, About, News, Contact
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
			'res': res, 
            'news': News.objects.all()
		}
        
        return render(request, template_name, context)



class ResearchView(TemplateView):
    template_name = 'research.html'
    
    def get(self, request, *args, **kwargs):
        
        template_name = 'research.html'
        
        context = {
			'researches': Research.objects.all(),
			'research_head': Research_head.objects.all(),
		}
        
        return render(request, template_name, context)

class VisionView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template_name = 'vision.html'
        
        context = {
			'vision': Vision.objects.all(),
		}
        
        return render(request, template_name, context)

class NewsView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template_name = 'news.html'
        
        context = {
			'news': News.objects.all(),
		}
        
        return render(request, template_name, context)

class ContactView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template_name = 'contact.html'
        
        context = {
			'contact': Contact.objects.all(),
		}
        
        return render(request, template_name, context)

class AboutView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        template_name = 'about.html'
        
        context = {
			'about': About.objects.all(),
		}
        
        return render(request, template_name, context)