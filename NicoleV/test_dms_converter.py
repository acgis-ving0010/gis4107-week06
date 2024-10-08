import dms_converter as d

def test_dms2dd():
    test_input = "075 45 03 W 45 23 05 N\n"
    expected = -75.75083333, 45.38472222
    actual = d.dms2dd(test_input)
    assert expected == actual

