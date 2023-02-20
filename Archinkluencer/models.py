
from django.db import models
from datetime import date
from django import forms


# Create your models here.
# Tabelle angelegt:
class ModelDataIFC(models.Model):

    created_at = models.DateField(default= date.today)
    name = models.CharField(max_length=6)
    length = models.CharField(max_length=6)
    doorpos = models.CharField(max_length=6)
    door = models.CharField( max_length= 6)
    algo = models.CharField(max_length=200)
    wallname = models.CharField(max_length=100)
    wallname_wc = models.CharField(max_length=100)





    def __str__(self):
        return str(self.id) + ' ' + self.name



WallWc= [('wall_0', 'Wand_0'),('wall_1', 'Wand_1'), ('wall_2', 'Wand_2'), ('wall_3', 'Wand_3'), ('wall_4', 'Wand_4')]
WallSink= [('wall_0', 'Wand_0'),('wall_1', 'Wand_1'), ('wall_2', 'Wand_2'), ('wall_3', 'Wand_3'), ('wall_4', 'Wand_4')]

class WallsWc(forms.Form):
    widget1 = forms.Select(choices= WallWc)
    widget2 = forms.Select(choices=WallSink)

    def __str__(self):
        return str(self.id) + ' ' + self.widget1 + self.widget2





