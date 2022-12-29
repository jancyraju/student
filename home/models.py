from django.db import models

# Create your models here.
class Students(models.Model):
    stud_id=models.AutoField(primary_key=True)
    stud_name=models.CharField( max_length=100)
    stud_email=models.CharField( max_length=200)
    stud_phno=models.CharField( max_length=10)
    stud_address=models.CharField( max_length=400)
    stud_place=models.CharField( max_length=100)
    
    

