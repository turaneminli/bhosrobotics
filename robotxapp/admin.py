from django.contrib import admin
from .models import head_thumbnail, Project, Faculty, Event, Research, Research_head, Vision, News, About, Contact, Social

# Register your models here.
admin.site.register(head_thumbnail)
admin.site.register(Project)
admin.site.register(Faculty)
admin.site.register(Event)
admin.site.register(Research)
admin.site.register(Research_head)
admin.site.register(Vision)
admin.site.register(News)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Social)