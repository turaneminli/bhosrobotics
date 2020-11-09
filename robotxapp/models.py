from django.db import models
from djrichtextfield.models import RichTextField
from PIL import Image

# Create your models here.

class head_thumbnail(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(max_length = 60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='static/media/')

    def __str__(self):
        return "Home Page Greeting"

class Project(models.Model):
    project_title = models.CharField(max_length = 30)
    project_image = models.ImageField(null=True, blank=True, upload_to='static/media/')
    
    def __str__(self):
        return self.project_title[:25]

class Faculty(models.Model):
    faculty_member_number = models.CharField(max_length = 5)
    faculty_member_footer = models.TextField(max_length = 200)
    robotics_center_info_title = models.CharField(max_length = 30)
    robotics_center_info_about = models.TextField(max_length = 200)
    students_number = models.CharField(max_length = 5)
    students_number_footer = models.TextField(max_length = 200)
    department_title = models.CharField(max_length = 30)
    department_info_under_title = models.TextField(max_length = 200)

    def __str__(self):
        return "Brief about robotics center"

class Event(models.Model):
    event_name = models.CharField(max_length = 30)
    event_text = models.CharField(max_length = 120)
    event_time = models.DateField(null=True)

    def __str__(self):
        return self.event_name[:25]

class Research(models.Model):
    research_title = models.CharField(max_length = 50)
    research_content = models.TextField(max_length = 350)
    research_image = models.ImageField(null=True, blank=True, upload_to='static/media/')

    def __str__(self):
        return self.research_title[:25]

class Research_head(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(max_length = 60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='static/media/')
    
    def __str__(self):
        return "Research Page Greeting"

class Vision(models.Model):
    head_statement = models.CharField(max_length = 60)
    second_row = models.CharField(blank=True, max_length = 60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='static/media/')
    goal_title_1 = models.CharField(max_length = 50)
    goal_content_1 = models.TextField(blank=True, max_length = 250)
    goal_image_1 = models.ImageField(null=True, blank=True, upload_to='static/media/')
    goal_title_2 = models.CharField(max_length = 50)
    goal_content_2 = models.TextField(blank=True, max_length = 250)
    goal_image_2 = models.ImageField(null=True, blank=True, upload_to='static/media/')
    goal_title_3 = models.CharField(max_length = 50)
    goal_content_3 = models.TextField(blank=True, max_length = 250)
    goal_image_3 = models.ImageField(null=True, blank=True, upload_to='static/media/')

    def __str__(self):
        return "Vision Page"

class News(models.Model):
    head_statement = models.CharField(max_length = 60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='static/media/')

    def __str__(self):
        return "News Page"

class Contact(models.Model):
    head_statement = models.CharField(max_length = 60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='static/media/')
    telephone = models.CharField(max_length = 60)
    email = models.CharField(max_length = 60)
    contact_image = models.ImageField(null=True, blank=True, upload_to='static/media/')

    def __str__(self):
        return "Contact Page"


class About(models.Model):
    head_statement = models.CharField(max_length = 60)
    thumbnail = models.ImageField(null=True, blank=True, upload_to='static/media/')
    about_content = RichTextField()
    about_image = models.ImageField(null=True, blank=True, upload_to='static/media/')
    faculty_content = RichTextField()
    partner_image1 =  models.ImageField(null=True, blank=True, upload_to='static/media/')
    partner_link1 = models.CharField(blank = True, max_length = 100)
    partner_image2 =  models.ImageField(null=True, blank=True, upload_to='static/media/')
    partner_link2 = models.CharField(blank = True, max_length = 100)
    partner_image3 =  models.ImageField(null=True, blank=True, upload_to='static/media/')
    partner_link3 = models.CharField(blank = True, max_length = 100)
    
    def __str__(self):
        return "About, Faculty and Partners"


class Social(models.Model):
    youtube = models.CharField(max_length = 100)
    facebook = models.CharField(max_length = 100)
    linkedin = models.CharField(max_length = 100)
    instagram = models.CharField(max_length = 100)

    def __str__(self):
        return "Social Media links"


