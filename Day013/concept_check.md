# What is a Python module?
A python module is a python file containing codes that can be used by another python file.

# What does import do?
The import keyword allows you to be able to call a function of module into a python file to be used by that file.

# What is the difference between import math and from math import sqrt?
'import math' imports the entire file called maths and you can call any function in the file maths, while 'from math import sqrt' import the sqrt function from the math module.

# What is the Python Standard Library?
It's a collection of modules and packages distributed with Python that provide commonly needed functionality.

# What does the random module do?
random is a module in Python's standard library.

# What does the datetime module do?
datetime is a module, not simply a function.

# Why is modular programming useful?
Modular in programming is important because it is reusable, you don't have to write everything from the beginning you can call it and reuse it anytime.

# What is the advantage of putting functions in a separate module?
It is advantagous becanuse it makes it useable outside that file and allows you to call it into another file.

# What happens when you import your own .py file?
When you import your own .py file, Python treats it as a module and performs three distinct actions under the hood.
1. Executes the CodePython runs every line of code inside the imported file from top to bottom. If that file contains print statements, loops, or active function calls outside of a class or function definition, they will execute immediately in your current terminal.
2. Creates a NamespacePython loads all functions, classes, and global variables defined in that file into a separate namespace. This isolates the imported code so it does not accidentally overwrite variables in your main file. You access them using the module name (e.g., mymodule.my_function()).
3. Generates a __pycache__ FolderPython compiles your source code into bytecode to speed up future loading times. It stores this compiled code inside a new directory called __pycache__ as a .pyc file.
   
# Why is code reuse important in software engineering?
Reusing a code in programming is important because it reduces bulkiness, makes the work neat and readable, an dmakes it easy for you to use a particular function multiply times.
