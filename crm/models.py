from django.db import models

# Create your models here.

class Previous(models.Model):
    previous = models.URLField(max_length=200, blank=True, null=True)

class Company(models.Model):
    class TypeChoice(models.TextChoices):
        ALGER = 'Alger', 'Alger'
        ORAN = 'Oran', 'Oran'
        ANNABA = 'Annaba', 'Annaba'

    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=25, choices=TypeChoice.choices)

    def __str__(self):
        return self.name

class Contact(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.company}'
    


