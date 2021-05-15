from django.shortcuts import render
from .forms import UploadAudioForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

import music_tag

def upload_audio(request):
    context = {}
    if request.method == 'POST':
        upload_audio_form = UploadAudioForm(request.POST, request.FILES)
        if upload_audio_form.is_valid():
            audio_file = request.FILES['audio_file']
            fs = FileSystemStorage()
            file_name = fs.save(audio_file.name, audio_file)

            # Edit metadata
            f = music_tag.load_file(fs.location + '/' + audio_file.name)
            f['title'] = upload_audio_form.cleaned_data['title']
            f['artist'] = upload_audio_form.cleaned_data['artist']
            f['album'] = upload_audio_form.cleaned_data['album']
            f.save()
            with open(fs.location + '/' + audio_file.name, 'rb') as updated_file:
                response = HttpResponse(updated_file.read(), content_type='audio/mp4a-latm')
                response['Content-Disposition'] = 'inline; filename=' + upload_audio_form.cleaned_data['title'] + '.m4a'
                return response
    else:
        upload_audio_form = UploadAudioForm()
    context['form'] = upload_audio_form
    return render(request, 'audio_properties/upload_audio.html', context=context)