import doc_scanner as ds

def test_has_x_code_True():
    input_text  = "Tx6op3"  
    expected = True
    actual = ds.has_x_code(input_text)
    assert expected == actual

def test_has_x_code_False():
    input_text = "asldfkj"
    expected = False
    actual = ds.has_x_code(input_text)
    assert expected == actual

def test_get_x_code_position_input_index_0():
    input_text = "Tx6op3"
    expected = 1
    actual = ds.get_x_code_position(input_text)
    assert expected == actual

def test_get_x_code_position_invalid():
    input_text = "asdlfkasdf"
    expected = -1
    actual = ds.get_x_code_position(input_text)
    assert expected == actual

def test_get_x_code_position_input_index_3():
    input_text = "abcTx6op3"
    expected = 4
    actual = ds.get_x_code_position(input_text)
    assert expected == actual
