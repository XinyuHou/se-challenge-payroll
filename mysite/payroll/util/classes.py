class PayPeriod:
    def __init__(self, date):
        self.date = date
        # return a date period, [01/mm/yy - 15/mm/yy] or [16/mm/yy - last_day/mm/yy]

class ReportParser:
    def __init__(self, report):
        self.report = report

    def id(self):
        # return report id
        return 1

    def payslips(self):
        # return all payslips as a list
        return []
