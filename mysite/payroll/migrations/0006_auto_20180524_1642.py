# Generated by Django 2.0.5 on 2018-05-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0005_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='hours',
            field=models.FloatField(default=0.0),
        ),
    ]
