from django.db import models

# Create your models here.

class Dojos(models.Model):
    name = models.CharField(max_length=255)  # Dojos.obejcts.get(id='num_id') > {{object.name}}
    city = models.CharField(max_length=255) # Dojos.obejcts.get(id='num_id') > {{object.city}}
    state = models.CharField(max_length=2)
    desc = models.TextField()
    # ninjas                          #  # Dojos.obejcts.get(id='num_id') > {{object.ninjas.all()}}
    ## Hidden Field Here Render From Realtion With Ninjas = 'ninjas'
    ## Return All Ninja That Assoicated to Dojos.select
    # Related_name Of
    def __str__(self):
        return self.name

class Ninjas(models.Model):
    dojo_id = models.ForeignKey(Dojos,on_delete=models.CASCADE,related_name="ninjas")
    first_name = models.CharField( max_length=255)
    last_name = models.CharField( max_length=255)

    def __str__(self):
        return self.first_name
    