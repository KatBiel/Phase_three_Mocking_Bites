from lib.diary import *
from lib.secret_diary import *
import pytest

'''test when diary is locked, you cannot read it'''
def test_read_locked_diary():
    diary = Diary('My Contents')
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"

'''Unlock a secret diary and read the message'''
def test_unlock_secret_diary():
    diary = Diary('My contents')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == 'My contents'

def test_lock_secret_diary():
    diary = Diary('My contents')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as e:
        secret_diary.read()
    error_message = str(e.value)
    assert error_message == "Go away!"