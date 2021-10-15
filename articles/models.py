from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length = 120)
    Email = models.EmailField(max_length = 50)
    Subject = models.CharField(max_length = 255)
    Message = models.TextField(max_length = 1000)

    def __str__(self):
        return self.Name

