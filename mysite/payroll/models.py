from django.db import models
from django.utils import timezone

class JobGroup(models.Model):
    group = models.CharField(max_length = 5, primary_key=True)
    rate = models.IntegerField(default = 0)

class Report(models.Model):
    id = models.IntegerField(default = -1, primary_key=True)

class Payslip(models.Model):
    pay_date = models.DateField('Paid Date')
    hours = models.FloatField(default = 0.0)
    employee = models.IntegerField(default = 0)
    job_group = models.ForeignKey(JobGroup, on_delete = models.PROTECT)
    def __str__(self):
        return str(self.employee) + str(self.pay_date) + str(self.hours) + str(self.job_group.group)

class Payroll(models.Model):
    employee = models.IntegerField(default = 0)
    start_date = models.DateField(default = timezone.now)
    end_date = models.DateField(default = timezone.now)
    amount = models.FloatField(default = 0.0)

    def __str__(self):
        return str(self.employee) + str(self.start_date) + str(self.end_date) + str(self.amount)
