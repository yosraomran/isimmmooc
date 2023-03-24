# Generated by Django 4.1.2 on 2023-01-19 16:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FormateurCV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(blank=True, help_text='CV de Formateur', upload_to='CVs/Formateur/')),
            ],
            options={
                'ordering': ['-cv'],
            },
        ),
        migrations.CreateModel(
            name='Organisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Nom de l Organisme', max_length=20)),
                ('mail', models.EmailField(blank=True, help_text='Email de l Organisme', max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Numero de telephone de l Organisme', max_length=128, region=None)),
                ('web_site', models.URLField(blank=True, help_text='Web Site de l Organisme')),
                ('file_exist', models.FileField(blank=True, help_text='File Exist de l Organisme', null=True, upload_to='Organisme_files/')),
                ('adress', models.CharField(help_text='Adresse de l Organisme', max_length=200)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='PreOrganisme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Nom de l Organisme', max_length=20)),
                ('mail', models.EmailField(blank=True, help_text='Email de l Organisme', max_length=200)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Numero de telephone de l Organisme', max_length=128, region=None)),
                ('web_site', models.URLField(blank=True, help_text='Web Site de l Organisme')),
                ('file_exist', models.FileField(blank=True, help_text='File Exist de l Organisme', null=True, upload_to='PreOrganisme_files/')),
                ('adress', models.CharField(default='', help_text='Adresse de l Organisme', max_length=200)),
                ('accepted', models.BooleanField(default=False)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='PreFormateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Prenom de Formateur', max_length=20)),
                ('last_name', models.CharField(blank=True, help_text='Nom de Formateur', max_length=30)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2001, 12, 26, 0, 0), help_text='Date de naissance de Formateur')),
                ('mail', models.EmailField(blank=True, default=None, help_text='Email de Formateur', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, help_text='Numero de telephone de Formateur', max_length=128, region=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to='PreFormateur/')),
                ('accepted', models.BooleanField(default=False)),
                ('cv', models.ForeignKey(blank=True, default=None, help_text='CV de PreFormateur(si existe)', null=True, on_delete=django.db.models.deletion.CASCADE, to='Isimmmooc_Users.formateurcv')),
                ('organisme', models.ForeignKey(blank=True, default=None, help_text='Organisme de Formateur(si existe)', null=True, on_delete=django.db.models.deletion.CASCADE, to='Isimmmooc_Users.organisme')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-first_name'],
            },
        ),
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Prenom de Formateur', max_length=20)),
                ('last_name', models.CharField(blank=True, help_text='Nom de Formateur', max_length=30)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2001, 12, 26, 0, 0), help_text='Date de naissance de Formateur')),
                ('mail', models.EmailField(blank=True, default=None, help_text='Email de Formateur', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, help_text='Numero de telephone de Formateur', max_length=128, region=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Formateur/')),
                ('cv', models.ForeignKey(blank=True, default=None, help_text='CV de Formateur(si existe)', null=True, on_delete=django.db.models.deletion.CASCADE, to='Isimmmooc_Users.formateurcv')),
                ('organisme', models.ForeignKey(blank=True, default=None, help_text='Organisme de Formateur(si existe)', null=True, on_delete=django.db.models.deletion.CASCADE, to='Isimmmooc_Users.organisme')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-first_name'],
            },
        ),
        migrations.CreateModel(
            name='Comite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, help_text='Prenom du Comite', max_length=255)),
                ('last_name', models.CharField(default=None, help_text='Nom du Comite', max_length=255)),
                ('grade', models.CharField(blank=True, help_text='Niveau du Comite', max_length=255)),
                ('department', models.CharField(default=None, help_text='Departement du Comite', max_length=255)),
                ('email', models.EmailField(blank=True, help_text='Email du Comite', max_length=255, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default=None, help_text='Numero de telephone du Comite', max_length=12, region=None, unique=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-last_name'],
            },
        ),
        migrations.CreateModel(
            name='Apprenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Prenom de l Apprenant', max_length=20)),
                ('last_name', models.CharField(blank=True, help_text='Nom de l Apprenant', max_length=30)),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2001, 12, 26, 0, 0), help_text='Date de naissance de l Apprenant')),
                ('mail', models.EmailField(blank=True, default=None, help_text='Email de l Apprenant', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, help_text='Numero de Telephone de l Apprenant', max_length=128, region=None)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Apprenant/')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-first_name'],
            },
        ),
    ]
