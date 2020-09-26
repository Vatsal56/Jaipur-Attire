from django.db import models
from datetime import datetime  

class Size(models.Model):
    length = models.CharField(max_length=200)

    def __str__(self):
        return self.length

class Fabric(models.Model):
    fabric = models.CharField(max_length=200)

    def __str__(self):
        return self.fabric
    
class Clothe(models.Model):
    name = models.CharField(max_length=200)
    size = models.OneToOneField(Size, on_delete=models.CASCADE)
    fabric = models.OneToOneField(Fabric, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    up_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    

