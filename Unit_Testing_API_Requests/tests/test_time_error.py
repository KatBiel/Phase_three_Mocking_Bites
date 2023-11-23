from lib.time_error import TimeError
from unittest.mock import Mock

def test_time_difference():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1700751327}
    timer_mock = Mock()
    timer_mock.time.return_value = 1700753687.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -2360.5