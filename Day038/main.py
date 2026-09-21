from enum import Enum

# Basic Enum

class Status(Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"

print(Status.PENDING)
print(Status.PENDING.value)

# Task Status

class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

task_status = TaskStatus.IN_PROGRESS
print(task_status.value)

# Loop Through an Enum

for task in TaskStatus:
    print(task, task.value)

# Priority

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH.value)

# Function With Enum

def check_status(status):

    if status == TaskStatus.DONE:
        print("Task completed!")
    else:
        print("Task not completed.")

check_status(TaskStatus.DONE)

check_status(TaskStatus.IN_PROGRESS)

# AI Agent Status

class AgentStatus(Enum):
    IDLE = "idle"
    THINKING = "thinking"
    USING_TOOL = "using_tool"
    RESPONDING = "responding"
    ERROR = "error"

class AIAgent:

    def __init__(self, name, status):

        self.name = name
        self.status = status

    def show_status (self):
        print(f"{self.name} is {self.status.value}.")

    def set_status(self, status):
        self.status = status
    

agent = AIAgent("StudyBot", AgentStatus.THINKING)  

agent.show_status()

agent.set_status(AgentStatus.USING_TOOL)

agent.show_status()