from django.shortcuts import render
from pytube import YouTube
import os


# Create your views here.
def index(request):
    return render(request,'index.html')

def download(request):
    global url
    global title
    url = request.GET['url']
    yt = YouTube(str(url))
    video = []
    audio = []
    video = yt.streams.filter(progressive=True)
    audio  = yt.streams.filter(only_audio=True)
    # print(audio)
    embed_link = url.replace("watch?v=","embed/")
    title = yt.title
    thumb = yt.thumbnail_url
    # print(thumb)

    context = {'video': video ,'audio': audio, 'embed' : embed_link ,'bg':thumb, 'title': title}
    # context2 = { , 'embed' : embed_link , 'title': title}
    # ,
    
    return render(request,'download.html', context )

def yt_download_done(request,itag):
    global url
    homedir  = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == "POST":  
        temp = YouTube(url).streams.get_by_itag(int(itag))
        # print(temp)
        # if temp.type() == "audio/mpeg"
        YouTube(url).streams.get_by_itag(int(itag)).download(dirs)
        return render(request,'done.html', {'tit':title})
    else:
        return render(request,'error.html', {'tit':title})

def yt_mp3download_done(request,itag):
    global url
    homedir  = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == "POST":
        out_file = YouTube(url).streams.get_by_itag(int(itag)).download(dirs)
        # print(out_file)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        return render(request,'done.html', {'tit':title})
    else:
        return render(request,'error.html', {'tit':title})