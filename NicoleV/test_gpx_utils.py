import gpx_utils as gu

def test_get_coords_from_gpx_valid():
    test_input = '<trkpt lat="45.3888995" lon="-75.7472631">'
    expected_long, expected_lat = -75.7472631,45.3888995
    actual_long, actual_lat = gu.get_coords_from_gpx(test_input)
    assert [expected_long, expected_lat] == [actual_long, actual_lat]

def test_get_coords_from_gpx_invalid():
    test_input = '<lat="45.3888995" lon="-75.7472631">'
    expected_long, expected_lat = None,None
    actual_long, actual_lat = gu.get_coords_from_gpx(test_input)
    assert [expected_long, expected_lat] == [actual_long, actual_lat]

