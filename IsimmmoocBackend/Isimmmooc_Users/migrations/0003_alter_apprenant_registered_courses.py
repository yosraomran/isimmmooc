# Generated by Django 4.1.2 on 2023-01-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Isimmmooc_App', '0001_initial'),
        ('Isimmmooc_Users', '0002_apprenant_registered_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apprenant',
            name='registered_courses',
            field=models.ManyToManyField(default=None, help_text='Registered Courses', related_name='registered_courses', to='Isimmmooc_App.cours'),
        ),
    ]
