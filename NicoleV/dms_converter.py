def dms2dd(record):
    record_list = record.split()
    record_strip = record.strip()

    possible_long_directions = ["W", "w", "E", "e"]

    find_long_sign = [record_strip[i].isalpha() for i in record_strip]
    #long_substr = record_strip[:record_strip.find(possible_long_directions)]

    # find where the w or e character is in the string
    for i in len(record_strip):
        if record_strip[i].isalpha():
            break
        else:
            continue
    return i

    long_sign = record_strip[i]

    # long_deg
    # long_min
    # long_sec
    # long_sign

    # lat_deg
    # lat_min
    # lat_sec
    # lat_sign

    long, lat = "", ""



    return long, lat

# running pytest in the terminal is helpful if there are 
# problems getting the TDD framework set up