from django.db import models

# Create your models here.

class Company(models.Model):
    class TypeChoice(models.TextChoices):
        ALGER = 'ALG', 'Alger'
        ORAN = 'ORN', 'Oran'
        ANNABA = 'ANB', 'Annaba'

    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=3, choices=TypeChoice.choices)

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
        return f'{self.first_name} {self.last_name} {self.company}'
    


