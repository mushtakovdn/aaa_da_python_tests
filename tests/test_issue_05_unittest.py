import unittest
from unittest.mock import patch
import io
import what_is_year_now


class TestCurrenYear(unittest.TestCase):

    def test_ymd(self):
        api_stub = '{"currentDateTime": "2019-03-01"}'
        expected = 2019
        with patch(
            'urllib.request.urlopen',
            return_value=io.StringIO(api_stub)
        ):
            ret = what_is_year_now.what_is_year_now()
            self.assertEqual(ret, expected)

    def test_dmy(self):
        api_stub = '{"currentDateTime": "01.03.2019"}'
        expected = 2019
        with patch(
            'urllib.request.urlopen',
            return_value=io.StringIO(api_stub)
        ):
            ret = what_is_year_now.what_is_year_now()
            self.assertEqual(ret, expected)

    def test_wrong_format(self):
        api_stub = '{"currentDateTime": "01-03-2019"}'
        with patch(
            'urllib.request.urlopen',
            return_value=io.StringIO(api_stub)
        ):
            self.assertRaises(ValueError, what_is_year_now.what_is_year_now)
