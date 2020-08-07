from django.db import models

# Create your models here.
class Feeding_Entry(models.Model):
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return "Feeding Entry: " + str(self.date)

class Pet(models.Model):
    name = models.CharField(max_length=128)
    species = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    diet = models.CharField(max_length=256)
    profile_pic = models.ImageField(upload_to='pet_profile_pics/')

    def __str__(self):
        return str(self.name) + " (" + str(self.species) + ")"
