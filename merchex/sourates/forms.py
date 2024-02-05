from django import forms
from . import models
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("nom","mail","raison","message",)
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }