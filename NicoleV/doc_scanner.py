def has_x_code(in_text):
    """ Look for the code 'Tx6op3' in text and return True if found, and
    False if it is not present. 
    """
    search = in_text.find("Tx6op3")
    if search >= 0:
        return True
    elif search == -1:
        return False

def get_x_code_position(in_text):
    """ Look for the code 'Tx6op3' in text and return 1-based position for 
    start, if found. Otherwise return -1.  
    """
    search = in_text.find("Tx6op3")
    if search >= 0:
        search +=1
    return search