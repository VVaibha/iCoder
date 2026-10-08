from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    email=models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    content = models.TextField(max_length=1000)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)
    
    
    def __str__(self):
        return "message from : "+self.name +" - "+ self.email