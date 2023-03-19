## 0x0A. Python - Inheritance

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

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
## Documentation
- Do not use the words import or from inside your comments, the checker will think you try to import some modules.

## Total of contents
Files | Description
------|------------
[0-lookup.py](./0-lookup.py) | a function that returns the list of available attributes and methods of an object.
[1-my_list.py](./1-my_list.py) |  a class MyList that inherits from list.
[ tests/1-my_list.txt](./ tests/1-my_list.txt) | text file.
[2-is_same_class.py](./2-is_same_class.py) | a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
[3-is_kind_of_class.py](./3-is_kind_of_class.py) |  a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.
[4-inherits_from.py](./4-inherits_from.py) | a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
[5-base_geometry.py](./5-base_geometry.py) | an empty class BaseGeometry.
[6-base_geometry.py](./6-base_geometry.py) | a class BaseGeometry (based on 5-base_geometry.py).
[7-base_geometry.py](./7-base_geometry.py) | a class BaseGeometry (based on 6-base_geometry.py).
[tests/7-base_geometry.txt](./tests/7-base_geometry.txt) | a text file.
[8-rectangle.py](./8-rectangle.py) | a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
[9-rectangle.py](./9-rectangle.py) | a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py).
[10-square.py](./10-square.py) |  a class Square that inherits from Rectangle (9-rectangle.py).
[11-square.py](./11-square.py) | a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).
[100-my_int.py](./100-my_int.py) |  a class MyInt that inherits from int.
[101-add_attribute.py](./101-add_attribute.py) | a function that adds a new attribute to an object if it’s possible.

## Cohort
9
