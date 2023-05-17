from django.db import models
from datetime import date

# Create your models here.
class EntryModel(models.Model):
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    name = models.CharField(max_length=20, primary_key=True)
    text = models.TextField(max_length=200)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=gender_choices, max_length=1)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField()
    entry_date = models.DateField(default=date.today)


