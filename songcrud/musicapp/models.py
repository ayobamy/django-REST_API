from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} + ' ' + {self.last_name}"

class Song(models.Model):
    title = models.CharField(max_length = 150)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)

    def __str__(self):
        return f"Song details: \n{self.title}\n{self.date_released}\n{self.likes}"

class Lyrics(models.Model):
    content = models.TextField()
    song_id = models.IntegerField()
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)

    def __str__(self):
        return self.content
