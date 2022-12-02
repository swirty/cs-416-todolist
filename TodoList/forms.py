from TodoList.models import Task
from django.db import models
from django import forms

class CreateTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']

        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'})
        }