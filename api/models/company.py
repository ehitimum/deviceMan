from django.db import models
from django.db import migrations


class Company(models.Model):
    try:
        name = models.CharField(max_length=255)
        address = models.CharField(max_length=255)
    except:
        print("Errors inserting")
    
    class Meta:
            db_table = 'company'
