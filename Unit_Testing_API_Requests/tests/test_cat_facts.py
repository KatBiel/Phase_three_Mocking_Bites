from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_cat_facts():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"Ailurophile is the word cat lovers are officially called.","length":57}
    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: Ailurophile is the word cat lovers are officially called."