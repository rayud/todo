from django import forms  
from crud.models import Todo
from django.forms import fields

class TodoForm(forms.ModelForm):  
    class Meta:  
        model = Todo  
        fields = "__all__"