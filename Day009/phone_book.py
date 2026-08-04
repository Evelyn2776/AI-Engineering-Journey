phone_book = {
    "Alice": "08012345678",
    "John": "08087654321",
    "Grace": "08099998888"
}

name = input("Contact name: ")

if name in phone_book:
    print("Phone number: ", phone_book[name])
else:
    print("Contact not found.")