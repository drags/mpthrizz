# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from player.models import MusicFile, Directory

def index(request):
    playlist_contents = get_all_songs() 
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def get_all_songs():
    mp3 = MusicFile.objects.all().order_by('artist', 'album', 'tracknumber')
    #mp3 =  MusicFile.objects.filter(artist__icontains='mc chris').order_by('artist', 'album', 'tracknumber')

    files = []
    for m in mp3:
        m.listing = ' - '.join( [m.artist, m.album, m.title] )
        m.href = m.path.replace(m.dir.dir, m.dir.relative_to_web)
        files.append(m)
    return files

