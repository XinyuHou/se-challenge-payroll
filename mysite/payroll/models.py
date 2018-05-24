from django.db import models

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
	pay_period = models.DateTimeField('Paid Date')
	amount = models.IntegerField(default = 0)
	