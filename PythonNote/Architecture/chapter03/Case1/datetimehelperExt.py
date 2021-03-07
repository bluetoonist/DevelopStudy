"""
앞서 작성했던 datetimehelper에 대해 단위 테스트 케이스를 확장
"""
import unittest
import datetime
from Case1 import datetimehelper
from unittest.mock import patch

class DateTimeHelperTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = datetimehelper.DateTimeHelper()

    def test_date(self):
        my_date =  datetime.datetime(year=2016, month=8, day=16)

        with patch.object(self.obj, "today", return_value=my_date):

            # DateTimeHelper()에서 date() 메소드를 호출
            response = self.obj.date()

            self.assertEqual(response, '16/08/2016')

    def test_weekday(self):
        my_date = datetime.datetime(year=2016, month=8, day=21)

        with patch.object(self.obj, "today", return_value=my_date):
            response = self.obj.weekday()
            self.assertEqual(response, "Sunday")

    def test_us_indian_conversion(self):

        d1 = "08/12/16"
        d2 = "07/11/2014"
        d3 = "04/29/00"
        self.assertEqual(self.obj.us_to_indian(d1), "12/08/2016")
        self.assertEqual(self.obj.us_to_indian(d2), "11/07/2014")
        self.assertEqual(self.obj.us_to_indian(d3), "29/04/2000")

if __name__ == '__main__':
    unittest.main()
