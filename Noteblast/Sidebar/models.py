from django.db import models

# Create your models here.

class SideBar(models.Model):
    AllNotes = models.CharField(max_length=200)
    NewNotes = models.CharField(max_length=100)
    Trash = models.CharField(max_length=100)

class Meta():
    app_lable = "Sidebar"

class Trash (models.Model):
    NewNotes = models.CharField(max_length=100)
