from django.db import models
import time

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=250)
    year = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Track(models.Model):
    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return self.title
    
    def get_length(self):
        return time.strftime("%-M:%S", time.gmtime(self.length))
    
class Playlist(models.Model):
    title = models.CharField(max_length=150)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.title