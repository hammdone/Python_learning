# custom forms
from django import forms
from .models import ToDo
 
class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__" # all fields

    def clean_task(self): # checks if task was entered
        task = self.cleaned_data.get('task')
        if not task:
            raise forms.ValidationError("Task field cannot be empty.")
        return task

class UpdateToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['task'] # only the task field