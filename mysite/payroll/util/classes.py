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
        return self.start_date.strftime('%m/%d/%Y') + ' - ' + self.end_date.strftime('%m/%d/%Y')

class ReportParser:
    def __init__(self, report):
        data = report.decode("utf-8")
        self.report_lines = []
        for line in data.splitlines():
            self.report_lines.append(tuple(line.split(",")))

    def id(self):
        last_line = self.report_lines[len(self.report_lines) - 1]

        return int(last_line[1])

    def payslips(self):
        # return all payslips as a list
        return self.report_lines[ 1 : len(self.report_lines) - 1]
