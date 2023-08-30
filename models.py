from django.db import models

# Create your models here.



class Register(models.Model):
    first_name=models.CharField(max_length=50 ,blank=True)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    des=models.CharField(max_length=50)

def __str__(self):
    return self.name


class Login(models.Model):
        name=models.CharField(max_length=100)
        password=models.CharField(max_length=100)
    
def __str__(self):
    return self.name