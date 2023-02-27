"""Dict 04"""

contact_list = [{"name": "Bill", "phones": ["4456456456", "6476599"]},
                {"name": "Jill", "phones": ["4564456456", "674534834"]},
                {"name": "John", "phones": ["78917978978978", "6745634834"]},
                {"name": "Mike", "phones": ["789179789789", "6734834"]},
                {"name": "Frenk", "phones": ["78546456464", "6734834"]},
                {"name": "Alelx", "phones": ["78546456456", "6734456834"]}]



def find_contact(contacts, number):
    result = []
    for contact in contacts:
        if str(number) in str(contact):
            result.append(contact)
    return result

if __name__ == "__main__":
    print(find_contact(contact_list, 179))
