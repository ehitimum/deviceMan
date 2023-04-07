from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'company'
