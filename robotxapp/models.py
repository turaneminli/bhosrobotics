from django.db import models
# from djrichtextfield.models import RichTextField
from PIL import Image

# Create your models here.

class head_thumbnail(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/main_thumbnail/')

class Project(models.Model):
    project_title = models.CharField(max_length = 80)
    project_image = models.FileField(null=True, blank=True, upload_to='static/project_image/')
    
    def __str__(self):
        return self.project_title[:25]

class Faculty(models.Model):
    faculty_member_number = models.CharField(max_length = 5)
    faculty_member_footer = models.CharField(max_length = 80)
    robotics_center_info_title = models.CharField(max_length = 30)
    robotics_center_info_about = models.CharField(max_length = 80)
    students_number = models.CharField(max_length = 5)
    students_number_footer = models.CharField(max_length = 80)
    department_title = models.CharField(max_length = 30)
    department_info_under_title = models.CharField(max_length = 80)

class Event(models.Model):
    event_name = models.CharField(max_length = 20)
    event_text = models.CharField(max_length = 80)
    event_time = models.DateField(null=True)

    def __str__(self):
        return self.event_name[:25]

class Research(models.Model):
    research_title = models.CharField(max_length = 50)
    research_content = models.CharField(max_length = 150)
    research_image = models.FileField(null=True, blank=True, upload_to='static/research_image/')

class Research_head(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/research_thumbnail/')


