# Generated by Django 3.0.8 on 2020-11-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotxapp', '0005_auto_20201110_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='partner_image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='partner_image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='head_thumbnail',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='research',
            name='research_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='research_head',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='vision',
            name='goal_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='vision',
            name='goal_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='vision',
            name='goal_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
        migrations.AlterField(
            model_name='vision',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='static/media/'),
        ),
    ]
