import pytest
from challenges.challenge_encrypt_message import encrypt_message

INVALID_KEY = "tipo inválido para key"
INVALID_MESSAGE = "tipo inválido para message"
MESSAGE = "Alohomora"
ASSERTION_ONE = "aromoholA"
ASSERION_TWO = "olA_aromoh"
ASSERTION_THREE = "aromoho_lA"


def test_encrypt_message():
    with pytest.raises(TypeError, match=INVALID_KEY):
        encrypt_message(MESSAGE, "1")
    with pytest.raises(TypeError, match=INVALID_MESSAGE):
        encrypt_message(777, 3)

    assert encrypt_message(MESSAGE, 15) == ASSERTION_ONE
    assert encrypt_message(MESSAGE, 3) == ASSERION_TWO
    assert encrypt_message(MESSAGE, 2) == ASSERTION_THREE
