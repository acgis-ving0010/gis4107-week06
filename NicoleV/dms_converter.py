def dms2dd(record):
    record_strip = record.strip()
    # find the first alphabetic character in the string
    for i in range(len(record_strip)):
        if record_strip[i].isalpha():
            break
    long_dir = record_strip[i].upper()
    long_substr = record_strip[:i].strip()

    try: 
        long_deg = int(long_substr.split()[0])
    except IndexError:
        long_deg = 0
    try: 
        long_min = int(long_substr.split()[1])
    except IndexError:
        long_min = 0
    try: 
        long_sec = int(long_substr.split()[2])
    except IndexError:
        long_sec = 0   

    # find the second alphabetic character in the string
    for j in range(i+1, len(record_strip)):
        if record_strip[j].isalpha():
            break
    lat_dir = record_strip[j].upper()
    lat_substr = record_strip[i+1:j].strip()
    
    try:
        lat_deg = int(lat_substr.split()[0])
    except IndexError:
        lat_deg =0
    try:
        lat_min = int(lat_substr.split()[1])
    except IndexError:
        lat_min = 0
    try:
        lat_sec = int(lat_substr.split()[2])
    except IndexError:
        lat_sec = 0

    if all([0<=long_deg<=180, 0<=long_min<=59,  0<=long_sec<=59,
            long_dir in ('W', 'E'), lat_dir in ('N', 'S'),
            0<= lat_deg <= 90, 0<=lat_min<=59, 0<=lat_sec<=59]):
        #then calculate long degree
        long_dd = long_deg + (long_min/60) + (long_sec/3600)
        lat_dd = lat_deg + (lat_min/60) + (lat_sec/3600)
        if long_dir == 'W': long_dd *= -1
        if lat_dir == 'S': lat_dd *= -1
    else:
        long_dd, lat_dd = None, None

    return long_dd, lat_dd

# running pytest in the terminal is helpful if there are 
# problems getting the TDD framework set up