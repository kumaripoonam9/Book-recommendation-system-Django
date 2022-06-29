from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        name = self.fname + " " + self.lname
        return name