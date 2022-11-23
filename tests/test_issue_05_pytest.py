from unittest.mock import patch
import pytest
import io
import what_is_year_now


def test_ymd():
    api_stub = '{"currentDateTime": "2019-03-01"}'
    expected = 2019
    with patch(
        'urllib.request.urlopen',
        return_value=io.StringIO(api_stub)
    ):
        ret = what_is_year_now.what_is_year_now()
        assert ret == expected


def test_dmy():
    api_stub = '{"currentDateTime": "01.03.2019"}'
    expected = 2019
    with patch(
        'urllib.request.urlopen',
        return_value=io.StringIO(api_stub)
    ):
        ret = what_is_year_now.what_is_year_now()
        assert ret == expected


def test_wrong_format():
    api_stub = '{"currentDateTime": "01-03-2019"}'
    with patch(
        'urllib.request.urlopen',
        return_value=io.StringIO(api_stub)
    ):
        with pytest.raises(ValueError):
            what_is_year_now.what_is_year_now()
