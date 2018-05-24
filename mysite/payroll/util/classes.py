from calendar import monthrange
import datetime

class PayPeriod:
    def __init__(self, date):
        year = date.year
        month = date.month
        day = date.day
        first_day, last_day = monthrange(year, month)
        if (day <= 15):
            self.start_date = datetime.date(year, month, 1)
            self.end_date = datetime.date(year, month, 15)
        else:
            self.start_date = datetime.date(year, month, 16)
            self.end_date = datetime.date(year, month, last_day)

    def __str__(self):
        return self.to_str()

    def to_str(self):
        # return a date period, mm/01/yy - mm/15/yy or mm/16/yy - mm/last_day/yy
        return self.start_date.strftime('%m/%d/%Y') + ' - ' + self.end_date.strftime('%m/%d/%Y')

class ReportParser:
    def __init__(self, report):
        self.report = report

    def id(self):
        # return report id
        return 1

    def payslips(self):
        # return all payslips as a list
        return []
