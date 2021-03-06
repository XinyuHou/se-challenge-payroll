# Generated by Django 2.0.5 on 2018-05-24 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=5)),
                ('rate', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_date', models.DateField(verbose_name='Paid Date')),
                ('hours', models.IntegerField(default=0)),
                ('employee', models.IntegerField(default=0)),
                ('job_group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payroll.JobGroup')),
            ],
        ),
    ]
