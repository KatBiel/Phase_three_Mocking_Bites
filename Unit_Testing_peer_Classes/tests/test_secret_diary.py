from lib.secret_diary import *
from unittest.mock import Mock
import pytest

'''test initially is locked, you cannot read it'''
def test_read_locked_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"
    diary.read.assert_not_called()

'''Unlock a secret diary and read the message'''
def test_unlock_secret_diary():
    diary = Mock()
    diary.read.return_value = 'Cool Contents'
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'Cool Contents'
    diary.read.assert_called()

def test_lock_secret_diary():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"
    diary.read.assert_not_called()