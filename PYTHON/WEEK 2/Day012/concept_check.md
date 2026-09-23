# What is an exception?
An exception is an error that occurs while a program is running and interrupts the normal flow of the program.

# What does try do?
The try block lets you test a block of code for errors.

# What does except do?
The except block catches and handles errors raised within the associated try block.

# What is ValueError?
A ValueError occurs when a function receives an argument of the correct data type but an inappropriate or invalid value. 

# What is ZeroDivisionError?
A ZeroDivisionError is raised when the second argument of a division or modulo operation is zero.

# Why is catching specific exceptions better than using a bare except?
Using specific exceptions (like except ValueError:) prevents your code from accidentally hiding unrelated bugs or critical system events. A bare except can catch many unrelated runtime exceptions and make genuine programming bugs harder to notice and debug.

# What does else do in exception handling?
The else block executes code only if the try block runs completely without raising any exceptions.

# What does finally do?
The finally block runs its code no matter what, regardless of whether an exception was raised, caught, or ignored.

# What happens if an exception isn't handled?
If an exception is not caught by any except block, it propagates upward through the program execution stack. 

# Why is exception handling important in real applications?
Exception handling ensures that production applications remain resilient, user-friendly, and secure:
Prevents Crashes: It keeps web servers or desktop applications running smoothly even when a single user input or temporary network request fails.
Improves User Experience: Instead of showing users a confusing, technical error log, the application can display a polite, human-readable message (e.g., "File not found. Please try again.").
Resource Management: It ensures that system assets like file locks, memory pointers, and network sockets are safely closed and released, preventing resource leaks.