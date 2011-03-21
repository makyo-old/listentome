from django.db import models
from django.contrib.auth.models import User

class Record(models.Model):
    status_choices = (
            ('a', 'Available'),
            ('r', 'Reserved'),
            ('o', 'Checked-out'),
            ('m', 'Missing'),
            ('n', 'Not available')
            )

    title = models.CharField(max_length = 500)
    kind = models.CharField(max_length = 20)
    status = models.CharField(max_length = 1, choices = status_choices)
    performers = models.ManyToManyField('Performer', null = True)

class Performer(models.Model):
    name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 50, blank = True)

class Piece(models.Model):
    title = models.CharField(max_length = 500)
    composer = models.ForeignKey('Composer')

class Composer(models.Model):
    name = models.CharField(max_length = 200)
    external_link = models.CharField(max_length = 500, blank = True)
    about = models.TextField(blank = True)
    year_born = models.IntegerField(null = True)
    year_died = models.IntegerField(null = True)

class Movement(models.Model):
    piece = models.ForeignKey('Piece')
    title = models.CharField(max_length = 200)

class Component(models.Model):
    track_page_number = models.IntegerField(null = True)
    record = models.ForeignKey('Record')
    movement = models.ForeignKey('Movement')
