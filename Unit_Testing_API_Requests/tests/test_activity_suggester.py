from lib.activity_suggester import ActivitySuggester
from unittest.mock import Mock

'''When we call suggest it returns a nice activity'''
def test_suggest_activity():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"activity":"Learn about the Golden Ratio","type":"education","participants":1,"price":0.1,"link":"https://en.wikipedia.org/wiki/Golden_ratio","key":"2095681","accessibility":0.2}
    suggester = ActivitySuggester(requester_mock)
    assert suggester.suggest() == "Why not: Learn about the Golden Ratio"

    #we can also simplify this:

def test_suggest_activity():
    requester_mock = Mock()
    requester_mock.get().json.return_value = {"activity":"Learn about the Golden Ratio","type":"education","participants":1,"price":0.1,"link":"https://en.wikipedia.org/wiki/Golden_ratio","key":"2095681","accessibility":0.2}
    suggester = ActivitySuggester(requester_mock)
    assert suggester.suggest() == "Why not: Learn about the Golden Ratio"