from django.forms import ModelForm
from django import forms
from .models import ContactForm


class ContactView(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactForm