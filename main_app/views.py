from typing import Any, Dict
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from .models import Album, Track, Playlist
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context
    
class About(TemplateView):
    template_name = "about.html"

# class Album:
#     def __init__(self, title, artist, year, img, genre):
#         self.title = title
#         self.artist = artist
#         self.year = year
#         self.img = img
#         self.genre = genre

# albums = [
#     Album('Heart Like a Wheel', 'Linda Ronstadt', '1974', 'https://media.pitchfork.com/photos/63f3d9d31fb8fd1f5544fc2d/1:1/w_600/Linda-Ronstadt.jpg', 'Rock'),
#     Album('Hasten Down the Wind', 'Linda Ronstadt', '1976', 'https://m.media-amazon.com/images/I/51joa8TzKvL._UF1000,1000_QL80_.jpg', 'Rock'),
#     Album('Court and Spark', 'Joni Mitchell', '1974', 'https://jonimitchell.com/img/covers/xcourt.jpg', 'Folk'),
#     Album('The Hissing of the Summer Lawns', 'Joni Mitchell', '1975', 'https://jonimitchell.com/img/covers/xhissing.jpg', 'Folk'),
#     Album('Tear Me Apart', 'Tanya Tucker', '1979', 'https://m.media-amazon.com/images/I/61OF3HWFffL._UF1000,1000_QL80_.jpg', 'Country'),
#     Album('Here You Come Again', 'Dolly Parton', '1977', 'https://upload.wikimedia.org/wikipedia/en/4/47/Hereyoucomeagain.jpg', 'Country'),
#     Album('Stranger in the Alps', 'Phoebe Bridgers', '2017', 'https://media.pitchfork.com/photos/6380d5021628784965dd6626/1:1/w_600/Phoebe-Bridgers-Stranger-in-the-Alps.jpg', 'Rock'),
#     Album('Carrie & Lowell', 'Sufjan Stevens', '2015', 'https://media.pitchfork.com/photos/5929ac5c5e6ef959693218f8/1:1/w_600/dbfa1978.jpg', 'Rock'),
# ]

class AlbumList(TemplateView):
    template_name = "album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = self.request.GET.get("artist")
        if artist != None:
            context["albums"] = Album.objects.filter(artist__icontains=artist)
        else:
            context["albums"] = Album.objects.all()
        return context
    
class AlbumCreate(CreateView):
    model = Album
    fields = ['title', 'artist', 'year', 'img', 'genre']
    template_name = "album_create.html"
    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.object.pk})

class AlbumDetail(DetailView):
    model = Album
    template_name = "album_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['title', 'artist', 'year', 'img', 'genre']
    template_name = "album_update.html"
    def get_success_url(self):
        return reverse('album_detail', kwargs={'pk': self.object.pk})

class AlbumDelete(DeleteView):
    model = Album
    template_name = "album_delete_confirmation.html"
    success_url = "/albums/"

class TrackCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        album = Album.objects.get(pk=pk)
        Track.objects.create(title=title, length=length, album=album)
        return redirect('album_detail', pk=pk)
    
class PlaylistTrackAssoc(View):
    def get(self, request, pk, track_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Playlist.objects.get(pk=pk).tracks.remove(track_pk)
        if assoc == "add":
            Playlist.objects.get(pk=pk).tracks.add(track_pk)
        return redirect('home')