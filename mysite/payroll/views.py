from django.http import HttpResponse
from .models import Payroll

def all_payroll(request):
    first_five_payroll = Payroll.objects.order_by('employee')[:5]
    output = ', '.join([str(p.employee) for p in first_five_payroll])
    return HttpResponse(output)

    #return HttpResponse("Welcome to this new payroll system!")

def individual_payroll(request, employee_id):
    return HttpResponse("Welcome back user %s!" % employee_id)

def upload_report(request):
	return HttpResponse("Please select a report file you want to upload!")
