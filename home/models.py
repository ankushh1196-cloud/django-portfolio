from django.db import models

class Contact(models.Model): #create a database table named contact
    name = models.CharField(max_length=30)
    email = models.EmailField()
    desc=models.TextField()
    def __str__(self):
        return self.name +',' + self.email

