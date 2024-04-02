from django.db import models

# Create your models here.
class Alert(models.Model):
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.photo.url
