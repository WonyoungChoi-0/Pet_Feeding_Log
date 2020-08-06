from django.db import models

# Create your models here.
class Feeding_Entry(models.Model):
    date = models.DateField()
    supplement = models.CharField(max_length=128)
    notes = models.TextField()

    def __str__(self):
        return "Feeding Entry: " + str(self.date)
