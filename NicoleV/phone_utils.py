def is_valid_phone_number(phone_number):
    if (phone_number[0:3].isdigit() and 
        phone_number[3] == '-' and
        phone_number[4:7].isdigit() and
        phone_number[7] == '-' and
        phone_number[8:12].isdigit() and 
        len(phone_number) == 12):
        return True
    else:
          return False