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
        file = request.FILES['uploaded_file']
        data = file.read()

        report_parser = ReportParser(data)

        # check if report is parsed before
        try:
            report_id = report_parser.id()
            report = Report.objects.get(pk = report_id)

            response = redirect('payroll:admin')
            response['Location'] += '?upload_error=true'
            return response

        except Report.DoesNotExist:
            # get payslips
            payslips = report_parser.payslips()

            # get all job groups
            all_job_group = JobGroup.objects.all()
            def job_rate(job_group):
                for job in all_job_group:
                    if (job.group == job_group):
                        return job.rate
                return 0

            def job(job_group):
                for job in all_job_group:
                    if (job.group == job_group):
                        return job
                return None

    return redirect('payroll:all_payroll')
