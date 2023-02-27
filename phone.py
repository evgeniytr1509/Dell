import random
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    print (new_phone)

    list_phones = []
    for i in range(10):
        list_phones.append(new_phone)
    
    print (list_phones)

sanitize_phone_number("+45645 64-64")



#def get_phone_numbers_for_countries(list_phones):


#get_phone_numbers_for_countries():