from django import forms
from .models import User_table

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User_table
        fields = "__all__"
