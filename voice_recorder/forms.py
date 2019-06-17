from django.forms import forms


class AudioForm(forms.Form):
    audio = forms.FileField()
