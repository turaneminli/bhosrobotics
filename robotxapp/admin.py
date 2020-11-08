from django.contrib import admin
from .models import head_thumbnail, Project, Faculty, Event, Research

# Register your models here.
admin.site.register(head_thumbnail)
admin.site.register(Project)
admin.site.register(Faculty)
admin.site.register(Event)
admin.site.register(Research)