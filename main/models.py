from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50 , null = False) 
    date_created = models.DateTimeField(auto_now_add=True , null = True)
    def __str__(self):
        return self.name



class Formation(models.Model):
    ETAT=(('activé','activé'),
            ('non activé','non activé'))

    name = models.CharField(max_length=50 , null = True)
    duree = models.IntegerField(null = True )
    #logo = models.ImageField(blank=True , null = True , upload_to ="logos" ,default='logo/default.jpg')
    logo = models.ImageField(upload_to='logos', blank=True, null=True , default='logo/default.jpg')
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    etat = models.CharField(max_length=200, null=True, choices=ETAT)
    description = models.CharField(max_length=500 , null =True) 
    date_created = models.DateTimeField(auto_now_add=True , null = True)
    def __str__(self):
        return self.name
