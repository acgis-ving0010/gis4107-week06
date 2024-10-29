import dms_converter as d

def test_dms2dd_valid_input_WN():
    test_input = "075 45 03 W 45 23 05 N\n"
    expected = -(75+(45/60)+(3/3600)), 45+(23/60)+(5/3600)
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_valid_input_WS():
    test_input = "075 45 03 W 45 23 05 S\n"
    expected = -(75+(45/60)+(3/3600)), -(45+(23/60)+(5/3600))
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_valid_input_ES():
    test_input = "075 45 03 E 45 23 05 S\n"
    expected = (75+(45/60)+(3/3600)), -(45+(23/60)+(5/3600))
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_valid_input_EN():
    test_input = "075 45 03 E 45 23 05 N\n"
    expected = (75+(45/60)+(3/3600)), (45+(23/60)+(5/3600))
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_valid_input_lowercase():
    test_input = "075 45 03 w 45 23 05 n\n"
    expected = -(75+(45/60)+(3/3600)), 45+(23/60)+(5/3600)
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_long_deg_out_of_range():
    test_input = "181 45 03 W 45 23 05 N\n"
    expected = None,None
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_long_min_out_of_range():
    test_input = "075 60 03 W 45 23 05 N\n"
    expected = None,None
    actual = d.dms2dd(test_input)
    assert expected == actual

def test_dms2dd_weird_letter():
    test_input = "075 45 03 j 45 23 05 N\n"
    expected = None,None
    actual = d.dms2dd(test_input)
    assert expected == actual    

def test_dms2dd_no_long_sec():
    test_input = "075 45 W 45 23 05 N\n"
    expected = -(75+(45/60)), 45+(23/60)+(5/3600)
    actual = d.dms2dd(test_input)
    assert expected == actual   

def test_dms2dd_no_long_sec_min():
    test_input = "075 W 45 23 05 N\n"
    expected = -(75), 45+(23/60)+(5/3600)
    actual = d.dms2dd(test_input)
    assert expected == actual  

def test_dms2dd_no_lat_sec():
    test_input = "075 45 03 W 45 23 N\n"
    expected = -(75+(45/60)+(3/3600)), 45+(23/60)
    actual = d.dms2dd(test_input)
    assert expected == actual   

def test_dms2dd_no_lat_sec_min():
    test_input = "075 45 03 W 45 N\n"
    expected = -(75+(45/60)+(3/3600)), 45
    actual = d.dms2dd(test_input)
    assert expected == actual  

def test_dms2dd_no_long():
    test_input = "45 N\n"
    expected = None,None
    actual = d.dms2dd(test_input)
    assert expected == actual  