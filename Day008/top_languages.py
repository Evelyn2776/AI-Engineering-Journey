languages = ["English", "French", "Spanish", "Korean", "Dutch"]

for lang in languages:
    print(lang)

languages.remove("Dutch")
languages.append("Japanese")

print(languages)