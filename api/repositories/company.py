from django.db import IntegrityError
from api.models.company import Company

def create_company(name: str, address: str) -> dict:
    """
    Create a new company and return its details as a dictionary.
    """
    try:
        company = Company.objects.create(name=name, address=address)
    except IntegrityError:
        # Handle duplicate key error
        return {'error': 'Company already exists.'}
    
    # Return company details as a dictionary
    
    return {
        'id': company.id,
        'name': company.name,
        'address': company.address,
    }
