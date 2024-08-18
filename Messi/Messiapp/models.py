from django.db import models

# Create your models here.
class Place(models.Model):
    names=models.CharField(max_length=250)
    img=models.ImageField(upload_to='Pics')
    desc=models.TextField()



    def __str__(self):
        return self.names