from django import forms
from taskmanager.tasks.models import Task

class Task_form(forms.ModelForm):

    description = forms.CharField(label='Tarefa', widget=forms.Textarea)

    class Meta():
        model=Task
        fields=['description']