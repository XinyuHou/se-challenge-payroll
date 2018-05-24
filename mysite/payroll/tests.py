from django.test import TestCase

from payroll.util.classes import PayPeriod, ReportParser
import datetime

class PayPeriodTests(TestCase):

    def test_to_str_with_a_date_in_the_first_half(self):
        """
        to_str() returns 01/03/2018 - 15/03/2018 for a date 10/03/2018
        """
        test_date = datetime.date(2018, 3, 1)
        pay_period = PayPeriod(test_date)

        self.assertEqual(pay_period.to_str(), "03/01/2018 - 03/15/2018")

    def test_to_str_with_a_date_in_the_second_half(self):
        """
        to_str() returns 16/03/2018 - 31/03/2018 for a date 22/03/2018
        """
        test_date = datetime.date(2018, 3, 22)
        pay_period = PayPeriod(test_date)

        self.assertEqual(pay_period.to_str(), "03/16/2018 - 03/31/2018")
