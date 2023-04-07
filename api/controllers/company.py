from django.http import JsonResponse
from django.views.decorators.http import require_POST
from api.repositories.company import create_company

@require_POST
def create_company(request):
    company_name = request.POST.get('company_name')
    company_address = request.POST.get('company_address')

    # Create a new company in the database
    company_id = create_company(company_name, company_address)

    # Create the JSON response
    response = {
        'company_id': company_id,
        'company_name': company_name,
        'company_address': company_address,
        'message': 'Company created successfully'
    }

    return JsonResponse(response)
