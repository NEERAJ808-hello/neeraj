from django.db import models

# Create your models here.
class users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    mobile = models.IntegerField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    note = models.CharField(max_length=150)

    def __str__(self):
        return self.note

class MyNotes(models.Model):
    note = models.CharField(max_length=150)

    def __str__(self):
        return self.note
