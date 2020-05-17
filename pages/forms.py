from django import forms
from django.forms import ModelForm
from .models import Project, Contact


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
