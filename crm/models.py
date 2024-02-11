from django.db import models

# Create your models here.

class Contact(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.company}'
    


