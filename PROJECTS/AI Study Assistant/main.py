from student import Student

name = input("Name: ")
career = input("Career: ")
topic = input("Study Topic: ")
topics = input("Topics Studied: ")

tops = topics.strip().split(",")
new_top = [topic.strip() for topic in tops]

Info = Student(name, career, topic, *new_top)

print("=============================")
print("AI STUDY ASSISTANT")
print("=============================\n")
Info.introduction()
print()
Info.show_topics()
print()
Info.topics_count()
print()
Info.search_topic()
print()
Info.add_topic()
print()
Info.change_topic()