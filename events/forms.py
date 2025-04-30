from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateTimeInput(attrs={
            'placeholder': '30/04/2025 14:00'
        })
    )

    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
