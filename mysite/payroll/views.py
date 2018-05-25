from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime

from .models import Payroll
from payroll.util.classes import PayPeriod, ReportParser

def all_payroll(request):
    payrolls = Payroll.objects.order_by('employee')
    context = {
        'title': "Welcome to this new payroll system!",
        'payrolls': payrolls,
    }

    return render(request, 'payroll/payroll.html', context)

def individual_payroll(request, employee_id):
    individual_payrolls = list(Payroll.objects.filter(employee = employee_id))

    context = {
        'title': "Welcome back user %s!" % employee_id,
        'payrolls': individual_payrolls,
    }
    return render(request, 'payroll/payroll.html', context)

def admin(request):
    data = request.GET
    upload_error = False
    if ('upload_error' in data):
        upload_error = True
    context = {
        'title': "Please select a report file you want to upload!",
        'upload_error': upload_error
    }

    return render(request, 'payroll/admin.html', context)

def report(request):
    if request.method == 'POST' and request.FILES['uploaded_file']:
        report_parser = ReportParser(request.FILES['uploaded_file'])

        # check if report is parsed before, todo dup report problem

        # get payslips, todo check ORM session

        # for add up each payslips according to employee id

        # update payroll

    return redirect('payroll:all_payroll')
