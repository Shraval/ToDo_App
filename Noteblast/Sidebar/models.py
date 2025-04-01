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

class Tag (models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"
    
class NewNote(models.Model):
    untitled = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.untitled}"

class NewToDo(models.Model):
    untitled = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.untitled}"

