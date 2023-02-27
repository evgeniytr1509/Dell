"""Dict 04"""

contact_list = [{"name": "Bill", "phones": ["1324563", "6476599"]},
                {"name": "Jill", "phones": ["5745589", "6734834"]}]



def find_contact(contacts, number):
    result = []
    for contact in contacts:
        if str(number) in str(contact):
            result.append(contact)
    return result

if __name__ == "__main__":
    print(find_contact(contact_list, 6))