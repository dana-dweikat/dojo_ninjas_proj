from django.db import models

# Create your models here.

class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField()
    
    # Related_name Of
    def __str__(self):
        return self.name

class Ninjas(models.Model):
    dojo_id = models.ForeignKey(Dojos,on_delete=models.CASCADE,related_name="ninjas")
    first_name = models.CharField( max_length=255)
    last_name = models.CharField( max_length=255)

    def __str__(self):
        return self.first_name
    