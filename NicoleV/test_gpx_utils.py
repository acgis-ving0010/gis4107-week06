import gpx_utils as gu

def test_get_coords_from_gpx_valid():
    test_input = '<trkpt lat="45.3888995" lon="-75.7472631">'
    expected = -75.7472631,45.3888995
    actual = gu.get_coords_from_gpx(test_input)
    assert expected == actual
