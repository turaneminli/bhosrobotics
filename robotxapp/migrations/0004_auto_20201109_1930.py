# Generated by Django 3.0.8 on 2020-11-09 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robotxapp', '0003_auto_20201109_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('linkedin', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='partner_link1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='partner_link2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='partner_link3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_text',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_title',
            field=models.CharField(max_length=30),
        ),
    ]
