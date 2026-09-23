text = input("Enter text: ")
search = input("Search for: ")

cleaned_text = text.strip().lower()
words = cleaned_text.split()
word_count = len(words)

cleaned_search = search.strip().lower()

print(f"\nOriginal:\n{text}")
print(f"\nCleaned:\n{cleaned_text}")
print(f"\nWords:\n{words}")
print(f"\nWord count:\n{word_count}")

if cleaned_search in words:
    print("\nFound: True")
else:
    print("\nFound: False")