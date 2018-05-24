from django.db import models
from django.utils import timezone

class JobGroup(models.Model):
    group = models.CharField(max_length = 5)
    rate = models.IntegerField(default = 0)

class Payslip(models.Model):
    pay_date = models.DateField('Paid Date')
    hours = models.IntegerField(default = 0)
    employee = models.IntegerField(default = 0)
    job_group = models.ForeignKey(JobGroup, on_delete = models.PROTECT)

class Payroll(models.Model):
    employee = models.IntegerField(default = 0)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
    amount = models.IntegerField(default = 0)
