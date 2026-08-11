text = input("Enter some text: ")
search = input("Search for: ")

text = text.lower()
search = search.lower()

if search in text:
    print("Found: True")
else:
    print("Found: False")