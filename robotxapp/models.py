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
    faculty_member_footer = models.CharField(max_length = 200)
    robotics_center_info_title = models.CharField(max_length = 30)
    robotics_center_info_about = models.CharField(max_length = 200)
    students_number = models.CharField(max_length = 5)
    students_number_footer = models.CharField(max_length = 200)
    department_title = models.CharField(max_length = 30)
    department_info_under_title = models.CharField(max_length = 200)

class Event(models.Model):
    event_name = models.CharField(max_length = 20)
    event_text = models.CharField(max_length = 80)
    event_time = models.DateField(null=True)

    def __str__(self):
        return self.event_name[:25]

class Research(models.Model):
    research_title = models.CharField(max_length = 50)
    research_content = models.CharField(max_length = 350)
    research_image = models.FileField(null=True, blank=True, upload_to='static/research_image/')

class Research_head(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/research_thumbnail/')

class Vision(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(blank=True, max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/vision_thumbnail/')
    goal_title_1 = models.CharField(max_length = 50)
    goal_content_1 = models.CharField(blank=True, max_length = 250)
    goal_image_1 = models.FileField(null=True, blank=True, upload_to='static/vision_image/')
    goal_title_2 = models.CharField(max_length = 50)
    goal_content_2 = models.CharField(blank=True, max_length = 250)
    goal_image_2 = models.FileField(null=True, blank=True, upload_to='static/vision_image/')
    goal_title_3 = models.CharField(max_length = 50)
    goal_content_3 = models.CharField(blank=True, max_length = 250)
    goal_image_3 = models.FileField(null=True, blank=True, upload_to='static/vision_image/')

class News(models.Model):
    head_statement = models.CharField(max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/news_thumbnail/')

class Contact(models.Model):
    head_statement = models.CharField(max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/contact_thumbnail/')
    telephone = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    contact_image = models.FileField(null=True, blank=True, upload_to='static/contact_image/')

class About(models.Model):
    head_statement = models.CharField(max_length = 60)
    thumbnail = models.FileField(null=True, blank=True, upload_to='static/about_thumbnail/')
    about_content = models.CharField(max_length = 1000)
    about_image = models.FileField(null=True, blank=True, upload_to='static/about_image/')
    faculty_content = models.CharField(max_length = 1000)
    partner_image1 =  models.FileField(null=True, blank=True, upload_to='static/partner_image/')
    partner_image2 =  models.FileField(null=True, blank=True, upload_to='static/partner_image/')
    partner_image3 =  models.FileField(null=True, blank=True, upload_to='static/partner_image/')