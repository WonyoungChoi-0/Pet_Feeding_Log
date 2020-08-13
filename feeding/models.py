from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    species = models.CharField(max_length=128)
    age = models.PositiveIntegerField()
    diet = models.CharField(max_length=256)
    profile_pic = models.ImageField(upload_to='pet_profile_pics/')

    def __str__(self):
        return str(self.name) + " (" + str(self.species) + ")"

class Feeding_Entry(models.Model):
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return str(self.pet.name) + " Feeding Entry: " + str(self.date)
