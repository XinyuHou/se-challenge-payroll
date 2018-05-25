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

            with transaction.atomic():
                # add up each payslip according to employee id and PayPeriod
                payslip_group = {}
                for payslip in payslips:
                    date = payslip[0]
                    employee_id = payslip[2]
                    hours = payslip[1]
                    job_group = payslip[3]

                    dt = datetime.strptime(date, "%d/%m/%Y")
                    pay_period = PayPeriod(dt)

                    result = payslip_group.get((int(employee_id), pay_period.start_date), None)

                    salary = 0
                    if (result):
                        salary = result

                    payslip_group[(int(employee_id), pay_period.start_date)] = salary + float(hours) * job_rate(job_group)

                # update payroll
                for payroll in payslip_group:
                    employee_id = payroll[0]
                    pay_period_start = payroll[1]
                    payment = payslip_group[(employee_id, pay_period_start)]

                    criterion1 = Q(employee = employee_id)
                    criterion2 = Q(start_date__lte = pay_period_start)
                    criterion3 = Q(end_date__gte = pay_period_start)

                    payrolls = Payroll.objects.filter(criterion1 & criterion2 & criterion3)
                    if len(payrolls) == 1:
                        pr = payrolls[0]
                        pr.amount += payment
                    else:
                        pr = Payroll()
                        pp = PayPeriod(pay_period_start)
                        pr.employee = employee_id
                        pr.start_date = pp.start_date
                        pr.end_date = pp.end_date
                        pr.amount = payment

                    pr.save()

                # Update report
                r = Report(id = report_id)
                r.save()

    return redirect('payroll:all_payroll')
