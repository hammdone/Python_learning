# custom forms
from django import forms
from .models import ToDo
 
class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__" # all fields

class UpdateToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['task'] # only the task  field