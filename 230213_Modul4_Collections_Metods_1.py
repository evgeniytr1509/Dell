person = {"name": "Bill", "age": "30"}

print(person.get("addres", "Not set"))

print(person.get("name", "Not set"))

address = person.get("address", -1)

name = person.get (("name", "Not set"))

if address < 0:
    print ("Addres not set")

print(person.pop("name"))
print(person)
person.update({"name": "Jim"})
print (person)
person ["weight"] = 76
print(person)

if not person.get("height"):
    person['height'] = 200

person.update({"dogs" : ["Patron"]})
person["dogs"] = ["Parton"]
person["dogs"].append("Bobik") # добавление в словарь

print(person)
