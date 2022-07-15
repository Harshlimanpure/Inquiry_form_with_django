from django.db import models

# Create your models here.
class MForm(models.Model):
    name=models.CharField(max_length=50)
    father_name = models.CharField(max_length=50,null=True)
    mother_name = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=50,null=True)
    email=models.EmailField(max_length=50,null=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    