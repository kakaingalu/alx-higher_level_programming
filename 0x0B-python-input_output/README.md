# 0x0B. Python - Input/Output

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

## Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc 
- Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Table of contents 
Files | Description
------|------------
[0-read_file.py](./0-read_file.py) | a function that reads a text file (UTF8) and prints it to stdout.
[1-write_file.py](./1-write_file.py) | a function that writes a string to a text file (UTF8) and returns the number of characters written.
[2-append_write.py](./2-append_write.py) | a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
[3-to_json_string.py](./3-to_json_string.py) | a function that returns the JSON representation of an object (string).
[4-from_json_string.py](./4-from_json_string.py) | a function that returns an object (Python data structure) represented by a JSON string.
[5-save_to_json_file.py](./5-save_to_json_file.py) | a function that writes an Object to a text file, using a JSON representation.
[6-load_from_json_file.py](./6-load_from_json_file.py) | a function that creates an Object from a “JSON file”.
[7-add_item.py](./7-add_item.py) | a script that adds all arguments to a Python list, and then save them to a file.
[8-class_to_json.py](./8-class_to_json.py) | a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.
[9-student.py](./9-student.py) | a class Student that defines a student by.
[10-student.py](./10-student.py) | a class Student that defines a student by: (based on 9-student.py).
[11-student.py](./11-student.py) | a class Student that defines a student by: (based on 10-student.py).
[12-pascal_triangle.py](./12-pascal_triangle.py) | a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of `n`.
[100-append_after.py](./100-append_after.py) | a function that inserts a line of text to a file, after each line containing a specific string.
[101-stats.py](./101-stats.py) | a script that reads stdin line by line and computes metrics.

## Cohort
9
