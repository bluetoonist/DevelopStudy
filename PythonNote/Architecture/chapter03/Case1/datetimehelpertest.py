
import unittest
from Case1 import datetimehelper


class DateTimeHelperTestCase(unittest.TestCase):

    def setUp(self):
        print("Setting Up....")
        self.obj = datetimehelper.DateTimeHelper()

    def test_us_indian_conversion(self):

        d1 = "08/12/16"
        d2 = "07/11/2014"
        d3 = "04/29/00"

        """ unittest.TestCase 를 상속해 아래 코드처럼
        assertEqual()을 호출해
        첫 번째 파라미터는 호출 함수를,
        두 번째 파라미터는 예상 결과를,
        적으면 테스트를 수행할 수 있음
        """
        self.assertEqual(self.obj.us_to_indian(d1), "12/08/2016")
        self.assertEqual(self.obj.us_to_indian(d2), "11/07/2014")
        self.assertEqual(self.obj.us_to_indian(d3), "29/04/2000")

if __name__ == '__main__':
    unittest.main()