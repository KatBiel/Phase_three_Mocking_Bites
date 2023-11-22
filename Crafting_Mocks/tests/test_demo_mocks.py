from unittest.mock import Mock

'''A plain old object'''

def test_plain_object():
    fake_object_1 = FakeClass()

    fake_object_2 = Mock()
    fake_object_2.hello()

class FakeClass():
    pass

'''An object with methods'''

def test_object_witb_methods():
    fake_object = FakeClassWithMethods()
    assert fake_object.greet() == 'Hello world!'

    fake_object_2 = Mock()
    fake_object_2.greet.return_value = 'Hello world!'
    assert fake_object_2.greet() == 'Hello world!'

class FakeClassWithMethods():
    def greet(self):
        return 'Hello world!'
    

'''An object with methods that can be verified have been called'''

def test_object_with_verified_methods():
    fake_object = FakeClassWithVerifiedMethods()
    assert fake_object.greet('Kat') == 'Hello Kat!'
    assert fake_object.greet_has_been_called == True

class FakeClassWithVerifiedMethods():
    def __init__(self):
        self.greet_has_been_called = False

    def greet(self, name):
        self.greet_has_been_called = True
        assert name == 'Kat'
        return 'Hello Kat!'
    
def test_mock_with_verifies_method():
    fake_object = Mock()
    fake_object.greet.return_value = 'Hello Kat!'
    assert fake_object.greet('Kat') == 'Hello Kat!'

    assert fake_object.greet('Kat') == 'Hello Kat!'
    fake_object.greet.assert_called()
    fake_object.greet.assert_called_with('Kat')