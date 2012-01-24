# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core import serializers

from player.models import MusicFile, Playlist, PlaylistEntry

def index(request):
    if 'last_playlist' in request.session:
        playlist = request.session['last_playlist']
    else:
        playlists = Playlist.objects.order_by('created_on')
        if playlists.exists():
            playlist = playlists[0]
        else:
            pl_id = None
    
    if pl_id is not None:
        try:
            playlist_contents = PlaylistEntry.objects.filter(playlist=pl_id)
        except Exception:
            pass
    else:
        playlist_contents = []
    
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def add_playlist(request):
    """ create a new playlist, store in cookie """
    new_pl = Playlist(name=request.POST['playlist_name'])
    new_pl.save()
    return HttpResponse('Added')

def serve_mp3(request, file_id):
    """ stream mp3 content from disk to web 

    allows playing of mp3 files from anywhere on system where webserver user has file permissions """

    file_entry = get_object_or_404(MusicFile, pk=file_id)

    try:
        fd = open(file_entry.path, 'r')
    except Exception, err1:
        return HttpResponse('Unable to open ' + str(file_entry.path) + str(err1))

    #file_content = fd.read()
    resp= HttpResponse()
    resp['Content-Type'] = "audio/mpeg"
    resp['X-Sendfile'] = file_entry.path
    return resp


def get_playlist_contents(playlist):
    """ retrieve the contents of a playlist as a queryset """
    playlist_contents = PlaylistEntry.objects.filter(playlist=playlist)
    files = []
    for m in playlist_contents:
        m.listing = ' - '.join( [m.artist, m.album, m.title] )
        files.append(m)
    return files

def filebrowser_load(request):
    filebrowser_contents = get_all_songs()
    return render_to_response('browser.html', locals())


def load_playlist(request):
    """ load playlist, store in cookie """

def add_to_playlist(request, file_id, playlist_id):
    file = get_object_or_404(Playlist, file_id)
    playlist = get_object_or_404(MusicFile, playlist_id)
    playlist_entry = PlaylistEntry(playlist=playlist, musicfile=file)
    try:
        playlist_entry.save()
    except Exception, err1:
        return HttpResponse('Fail to save playlist_entry'+str(err1))
    return HttpResponse('Added file successfully ' + file_id + ' ' + playlist_id)

def delete_from_playlist(request, file_id, playlist_id):
    """ delete from playlist """
    
def get_all_songs():
    mp3 = MusicFile.objects.all().order_by('artist', 'album', 'tracknumber')
    #mp3 =  MusicFile.objects.filter(artist__icontains='mc chris').order_by('artist', 'album', 'tracknumber')

    files = []
    for m in mp3:
        m.listing = ' - '.join( [m.artist, m.album, m.title] )
        files.append(m)
    return files

