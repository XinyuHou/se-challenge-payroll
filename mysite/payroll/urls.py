from django.urls import path

from . import views

urlpatterns = [
    path('employees', views.all_payroll, name='all_payroll'),
    path('employees/<int:employee_id>/', views.individual_payroll, name='individual_payroll'),
    path('report/', views.upload_report, name='upload_report'),
]
