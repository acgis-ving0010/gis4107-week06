def get_db_link(building_code):
    """ A building code has the form NN-LLL-NNNNNN-NNN, where N is a number and
    L is a letter. Given a building code, return the link.
    """

    ##### NEED TO VERIFY BUILDING CODE FORMAT LIKE WITH TELEPHONE NUMBER? 

    code_list = building_code.split("-")
    link_list = []
    # get the last 2 letters of the LL part of the building code
    lll = code_list[1]
    link_list.append(lll[len(lll)-2:])
    # get the last 3 numbers of the second numbered part of the building code
    nnnnnn = code_list[2]
    link_list.append(nnnnnn[len(nnnnnn)-3:])
    # add these parts together and return the link
    link = "-".join(link_list)
    return link