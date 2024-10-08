import phone_utils as pu

def test_is_valid_phone_number_valid():
    phone_number = "123-456-7891"
    expected = True
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_no_dashes():
    phone_number = "1234567891"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_letters():
    phone_number = "abc-def-ghji"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual

def test_is_valid_phone_number_too_long():
    phone_number = "123-456-78910"
    expected = False
    actual = pu.is_valid_phone_number(phone_number)
    assert expected == actual
