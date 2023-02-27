def is_valid_pin_codes(pin_codes):
    if not pin_codes:
        return False
    pin_codes_set = set(pin_codes)
    if len (pin_codes) != len(pin_codes_set):
        return False
    for arr in pin_codes:
        if len(arr) !=4:
            return False
        if not arr.isdigit():
            return False
    print (True)
    return True


is_valid_pin_codes(['11011', '9034', '0011'])