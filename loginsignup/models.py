from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()
    img =  models.ImageField(upload_to = 'pics')