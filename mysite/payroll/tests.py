from django.test import TestCase

from payroll.util.classes import PayPeriod, ReportParser
import datetime

class PayPeriodTests(TestCase):

    def test_constructor_with_a_date_in_the_first_half(self):
        """
        to_str() returns 01/03/2018 - 15/03/2018 for a date 10/03/2018
        """
        test_date = datetime.date(2018, 3, 1)
        pay_period = PayPeriod(test_date)

        self.assertEqual(pay_period.start_date, datetime.date(2018, 3, 1))
        self.assertEqual(pay_period.end_date, datetime.date(2018, 3, 15))

    def test_constructor_with_a_date_in_the_second_half(self):
        """
        to_str() returns 16/03/2018 - 31/03/2018 for a date 22/03/2018
        """
        test_date = datetime.date(2018, 3, 22)
        pay_period = PayPeriod(test_date)

        self.assertEqual(pay_period.start_date, datetime.date(2018, 3, 16))
        self.assertEqual(pay_period.end_date, datetime.date(2018, 3, 31))

class ReportParserTests(TestCase):

    def test_id_with_report_id_equals_to_1(self):
        """
        id() returns 43 for a csv with report id 43 in footer
        """
        test_csv = b"date,hours worked,employee id,job group\n14/11/2016,7.5,1,A\n9/11/2016,4,2,B\n10/11/2016,4,2,B\nreport id,43,,"

        report_parser = ReportParser(test_csv)
        self.assertEqual(report_parser.id(), 43)


    def test_payslips_with_csv(self):
        """
        payslips() returns a list of payslips, 3 in this case, for a csv
        """
        test_csv = b"date,hours worked,employee id,job group\n14/11/2016,7.5,1,A\n9/11/2016,4,2,B\n10/11/2016,4,2,B\nreport id,43,,"

        report_parser = ReportParser(test_csv)
        payslips = report_parser.payslips()

        self.assertEqual(len(payslips), 3)
        self.assertEqual(payslips[0], ('14/11/2016', '7.5', '1', 'A'))
        self.assertEqual(payslips[1], ('9/11/2016', '4', '2', 'B'))
        self.assertEqual(payslips[2], ('10/11/2016', '4', '2', 'B'))
