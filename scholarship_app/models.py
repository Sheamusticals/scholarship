from django.db import models
from django.utils.timezone import timezone
GENDER_OPTIONS = (
    ('male','Male'),
    ('female','Female')
  
)

GUARDIAN_OPTIONS = (
    ('father','Father'),
    ('mother','Mother'),
    ('other','Other')
)
LEVEL_OPTIONS = (
    ('100','100'),
    ('200','200'),
    ('300','300'),
    ('400','400')
)




class Personal_Information(models.Model):
    First_Name = models.CharField(max_length=50,null=True)
    Last_Name = models.CharField(max_length=200)
    Date_Of_Birth =models.DateField(auto_now_add=True)
    Address =  models.CharField(max_length=254)
    Email = models.EmailField(max_length=254)
    Contact = models.CharField(max_length=50)
    

 

def __str__(self):
        return self.First_Name

class Guardian_Information(models.Model):
    
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=200)
    Occupation = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.EmailField( max_length=254)
    Contact = models.CharField(max_length=50)

     


def __str__(self):
        return self.Occupation

class School_Information(models.Model):
    Program = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=50)
    Index_Number =models.CharField(max_length=50)
    GPA=  models.CharField(max_length=50)
    Session = models.CharField( max_length=50)
    Contact = models.CharField(max_length=50)
    Reason =  models.TextField(null=True, blank=True)
    Level =  models.CharField(max_length=100,choices=LEVEL_OPTIONS, null=True)

def __str__(self):
        return self.Program




 


