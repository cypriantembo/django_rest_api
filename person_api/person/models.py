from cgitb import lookup
from django.db import models


class City(models.Model):
    city = models.CharField(max_length=50, unique=True, null=False)
    
    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = "Cities"
     

class Career(models.Model):
    area_of_study = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.area_of_study


class Person(models.Model):
    #choices field as to be a tuple with key value pair, order key->value
    GENDER_CHOICES = (
        ('Male', 'M'),
        ('Female', 'F'),
    )
    name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True)
    career = models.ManyToManyField(Career)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)


