def get_coords_from_gpx(gpx):
    """ A GPX contains coordinates in a string. 
    For example, '<trkpt lat="45.3888995" lon="-75.7472631">'
    Extract the longitude and latitude and return as values. 
    """
    # check that input string contains "trkpt"
    trkpt = gpx.find("trkpt")
    if trkpt >= 0:
        # find the substring that contains longitude information
        long_within = gpx[gpx.find("lon"):gpx.rfind(">")]
        # extract number in double quotes
        long_str = long_within[long_within.find("\"")+1: long_within.rfind("\"")]
        # check if long is a number by trying to convert it
        long = float(long_str)
        # find the substring that contains latitude information
        lat_within = gpx[gpx.find("lat"):gpx.find("lon")]
        # extract number in double quotes
        lat_str = lat_within[lat_within.find("\"")+1:lat_within.rfind("\"")]
        #check if lat is a number by trying to convert it
        lat = float(lat_str)
        return long, lat
    
    elif trkpt == -1:
        return None, None
    
    else:
        return "Something has gone wrong"

