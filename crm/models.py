from django.db import models
from django.utils import timezone

# Create your models here.



class Company(models.Model):
    class TypeChoice(models.TextChoices):
        ALGER = 'Alger', 'Alger'
        ORAN = 'Oran', 'Oran'
        ANNABA = 'Annaba', 'Annaba'

    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=25, choices=TypeChoice.choices)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "compagnies"

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
    

class Offer(models.Model):
    class TypeChoice(models.TextChoices):
        RFQ = 'RFQ', 'RFQ'
        OFFER = 'Offer', 'Offer'
        NEGO = 'Negotiation', 'Negotiation'
        WON = 'Won', 'Won'
        LOST = 'Lost', 'Lost'

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    step = models.CharField(max_length=11, choices=TypeChoice.choices)
    amount = models.FloatField(default=0)
    number = models.CharField(max_length=15, unique=True)
    date = models.DateField()


