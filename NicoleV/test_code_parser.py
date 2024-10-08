import code_parser as c

def test_get_db_link_valid():
    building_code = "20-WBO-109642-809"
    expected = "BO-642"
    actual = c.get_db_link(building_code)
    assert expected == actual

