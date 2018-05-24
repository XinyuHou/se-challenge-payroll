from django.urls import path

from . import views

app_name = 'payroll'

urlpatterns = [
    path('employees/', views.all_payroll, name='all_payroll'),
    path('employees/<int:employee_id>/', views.individual_payroll, name='individual_payroll'),
    path('admin/', views.admin, name='admin'),
    path('report/', views.report, name='report'),
]
