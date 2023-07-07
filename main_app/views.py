from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from .models import Album
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
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