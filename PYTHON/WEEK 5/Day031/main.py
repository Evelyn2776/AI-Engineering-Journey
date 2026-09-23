import re

text = "I have 3 apples, 12 oranges, and 25 bananas."

numbers = re.findall(r"\d+", text)
print(numbers)

clean_text = re.sub(r"\d+","NUMBER", text)
print(clean_text)

eve_text = "My age is 23, birthday 24 and i like the numbern 2."
number = re.findall(r"\d+", eve_text)
print(number)

texts = "I am learning Python and building AI projects."

result = re.search(r"Python", texts)

if result:
    print("Python found!")

texted = "Python"
results = re.findall(r"^Python$", texted)
print(results)

words = "I like 2 Animals and i ate 12 eggs and i have 3 balls."
numbered = re.findall(r"\d+", words)
chara = re.findall(r"[A-Z]+", words)
print(numbered)
print(chara)

text = "Student: David, Score: 95"
pattern = r"Student: (\w+), Score: (\d+)"
resul = re.search(pattern, text)

if resul:
    name = resul.group(1)
    score = resul.group(2)

    print(name)
    print(score)

test = "Name: John, Age: 18"
world = re.search(r"Name: (\w+), Age: (\d+)", test)

if world:
    print(world.group(1))
    print(world.group(2))

tests = "User ID: 48291"
id_match = re.search(r"User ID: (\d+)", tests)

if id_match:
    print(id_match.group(1))

fext = "Name: Sarah, Age: 19, Score:95"
wordy = re.search(r"Name: (\w+), Age: (\d+), Score: (\d+)", fext)

if wordy:
    age = int(wordy.group(2))
    score = int(wordy.group(3))

    print(wordy.group(1))
    print(age)
    print(score)

