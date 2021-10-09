from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    degree =models.CharField(max_length=200)
    description = models.TextField()


    def get_absolute_url(self):
        return reverse("doctor_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.name

class Patient(models.Model):
    name= models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    illness= models.CharField(max_length=200)
    allergies= models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    doctor= models.ForeignKey('basic_app.Doctor', related_name='patients')

    def get_absolute_url(self):
        return reverse("patient_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
