from django.shortcuts import render
import requests


def main_page(request):
    if request.method == 'POST':
        url = 'http://ec2-54-90-171-104.compute-1.amazonaws.com/success'
        print('here')
        files = {'file': request.FILES['file'],
                 'aud': request.FILES['aud']}
        r = requests.post(url, files=files)
        context = dict(r.json())
        if 'wait for the next 5 minutes' in context['result']:
            context['result'] = 'Image and Audio received and dataset aug and training is in progress, please wait for the next 15 minutes'
        return render(request, 'app/index.html', {'context': context})
    else:
        return render(request, 'app/index.html', {'context': False})
