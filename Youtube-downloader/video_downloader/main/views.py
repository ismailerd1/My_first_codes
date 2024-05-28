from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):
    return render(request,'index.html')



def download_details(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        if not video_url:
            context = {
                'error': 'Please enter a valid YouTube video URL.'
            }
            return render(request, 'index.html', context)
        yt = YouTube(video_url)
        thumbnail_url = yt.thumbnail_url
        video_title = yt.title
        video_streams = yt.streams.filter(progressive=True, file_extension='mp4')
        context = {
            'thumbnail_url': thumbnail_url,
            'video_streams': video_streams,
            'video_title' : video_title,
        }
        return render(request, 'download_details.html', context)
    else:
        return render(request, 'index.html')