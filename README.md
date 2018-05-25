Dependencies:
- Python 3.6.5
- Django 2.0.5

Instructions to run tests:
$ cd $Insalled_folder$/se-challenge-payroll/mysite
$ python3 manage.py test payroll

Instructions to run web application:
$ cd $Insalled_folder$/se-challenge-payroll/mysite
$ python3 manage.py runserver

Instructions to use the web application:
- Open a web browser on the machine that running the web application
- Put http://127.0.0.1:8000/payroll/admin/ in the address bar to see a report upload page
- After selecting a CSV file and clicking submit, it should redirect it to the all employees' payroll page
- To see any individual's payroll, go to http://127.0.0.1:8000/payroll/employees/N/ where N is the employee ID 

Project explanation:
This is my first Django project. I spent a day to play around the tutorials and used the next day to finish this demo. Can't say I'm perticularly proud of anything, as this demo look so immature, but I do feel quite satisfied.

The implementation should be straight forward. The reason I create a separate table for JobGroup in Database is trying to minimize the hardcoded rate. This give me the ability to change rate for an existing job without affecting historical payrolls. For Payroll, my originally thought was to use a stirng to represent the time period, then comparing it to any new payrolls to do the accumulation. But I switched to use date time half way through, so I can order payroll by time in a more efficiant way.

Things that can be added or improved:
- Currupted data handling
- User login, there is no privacy for individual payrolls
- Use a more scalable DB
- CSV file size limit, especialy after this service is open to many companys
- Caching, inherently this service has a higher deamon on reading rather than writing
etc