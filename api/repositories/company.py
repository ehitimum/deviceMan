from django.db import IntegrityError
from api.models.company import Company

def create_company(name, address):
    company = Company(name=name, address=address)
    company.save()
    return company.id