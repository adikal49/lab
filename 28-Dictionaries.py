#Dictionaries are key : value pairs
#Name: john Smith
#Email: john@gmail.com
#Phone: 1232

customer = {
    "name": "john smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "jack smith"
customer["birthdate"] = 1992
print(customer["birthdate"])
#print(customer.get("birthdate", 1992))