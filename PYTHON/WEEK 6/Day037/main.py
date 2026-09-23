from dataclasses import dataclass

# Basic Dataclass
@dataclass
class Student:

        name: str
        age: int
        course: str

student = Student("Evelyn", 20, "Engineering")

print(student.name)

# Topic Dataclass
@dataclass
class Topic:

    name: str
    completed: bool
    score: int

topic = Topic("Evelyn", True, 90)

print(topic.name)
print(topic.completed)
print(topic.score)

# Default Values
@dataclass
class User:

    name: str
    age: int
    level: str = "Beginner"

user = User("Evelyn", 21)

print(user.name)
print(user.age)
print(user.level)

# Dataclass Method
@dataclass
class Student:

    name: str
    score: int

    def passed (self):
        return self.score >= 50

student = Student("Evelyn", 90)

print(student.name)
print(student.score)
print(student.passed())

#  AI Document Dataclass
@dataclass
class Document:

    title: str
    content: str
    source: str

document = Document(
    title="Python Iterators",
    content="Iterators produce values one at a time.",
    source="Python Notes"
)

print(document)

# AI Study Record
@dataclass
class StudyRecord:

    topic: str
    completed: bool
    score: int
    notes: str = ""

    def summary(self):
        return f"Topic: {self.topic} | Completed: {self.completed} | Score: {self.score}"

study = StudyRecord(
    "Loops",
    True,
    80,
    notes="I learned how loops work."
)

print(study.summary())