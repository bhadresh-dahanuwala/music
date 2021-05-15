from os import name
from django import forms
from django.core.validators import FileExtensionValidator

class UploadAudioForm(forms.Form):
    audio_file = forms.FileField(label='Choose Audio File', validators=[FileExtensionValidator(allowed_extensions=['m4a', 'mp4', 'mp3'])])
    title = forms.CharField(required=True, max_length=30, label='Title')
    album = forms.CharField(max_length=50, label="Album / Movie", required=False)
    artist = forms.CharField(max_length=75, label='Singer(s)', required=False)
