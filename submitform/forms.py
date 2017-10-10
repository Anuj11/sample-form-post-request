from django import forms

from .models import submit


class SubmitForm(forms.ModelForm):
    class Meta:
        model = submit
        fields = ('name', 'message', )
