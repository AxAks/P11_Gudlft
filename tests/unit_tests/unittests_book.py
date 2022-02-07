"""
File for Unit Tests in route book
"""
from datetime import datetime

from libs.lib_commons import check_competition_date


def test_competition_date_in_the_future_should_return_true():
    now = datetime.strptime("2022-01-02 09:00:00", "%Y-%m-%d %H:%M:%S")
    competition_date = datetime.strptime("2022-03-12 10:00:00", "%Y-%m-%d %H:%M:%S")
    assert check_competition_date(competition_date, now) is True


def test_competition_date_in_the_past_should_return_false():
    now = datetime.strptime("2022-01-02 09:00:00", "%Y-%m-%d %H:%M:%S")
    competition_date = datetime.strptime("2022-01-01 10:00:00", "%Y-%m-%d %H:%M:%S")
    assert check_competition_date(competition_date, now) is False
