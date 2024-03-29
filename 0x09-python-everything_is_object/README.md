## 0x09. Python - Everything is object

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg">

## Background Context
-Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

- BTW, have you ever modified a variable without knowing it or wanting to? I mean:
```
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```
- OK. But what about this?
```
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

<img src="https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif" alt="" loading="lazy" style="">

- This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

- Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

- It’s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types.

- Note that during interviews for Python positions, you will most likely have to answer to these type of questions.

- All your answers should be only one line in a file. No space before or after the answer.

## Learning Objectives
- At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

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

## .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a new line

## Table of contents
Files | Description | code
------|-------------|-----
[0-answer.txt](./0-answer.txt) | What function would you use to print the type of an object? Write the name of the function in the file, without ().
[1-answer.txt](./1-answer.txt) | How do you get the variable identifier (which is the memory address in the CPython implementation)? Write the name of the function in the file, without ().
[2-answer.txt](./2-answer.txt) | In the following code, do a and b point to the same object? Answer with Yes or No. | ``` >>> a = 89 ```<br>``` >>> b = 100 ```
[3-answer.txt](./3-answer.txt) | In the following code, do a and b point to the same object? Answer with Yes or No. | ``` >>> a = 89 ```<br>``` >>> b = 89 ```
[4-answer.txt](./4-answer.txt) | In the following code, do a and b point to the same object? Answer with Yes or No. | ``` >>> a = 89 ```<br>``` >>> b = a ```
[5-answer.txt](./5-answer.txt) | In the following code, do a and b point to the same object? Answer with Yes or No. | ``` >>> a = 89 ```<br>``` >>> b = a + 1 ```
[6-answer.txt](./6-answer.txt) | What do these 3 lines print? | ``` >>> s1 = "Best School" ```<br>``` >>> s2 = s1 ```<br>``` >>> print(s1 == s2) ```
[7-answer.txt](./7-answer.txt) | What do these 3 lines print? | ``` >>> s1 = "Best" ```<br>``` >>> s2 = s1 ```<br>``` >>> print(s1 is s2) ```
[8-answer.txt](./8-answer.txt) | What do these 3 lines print? | ``` >>> s1 = "Best School" ```<br>``` >>> s2 = "Best School" ```<br>``` >>> print(s1 == s2) ```
[9-answer.txt](./9-answer.txt) | What do these 3 lines print? | ``` >>> s1 = "Best School" ```<br>``` >>> s2 = "Best School" ```<br>``` >>> print(s1 is s2) ```
[10-answer.txt](./10-answer.txt) | What do these 3 lines print? | ``` >>> l1 = [1, 2, 3] ```<br>``` >>> l2 = [1, 2, 3] ```<br>``` >>> print(l1 == l2) ```
[11-answer.txt](./11-answer.txt) | What do these 3 lines print? | ``` >>> l1 = [1, 2, 3] ```<br>``` >>> l2 = [1, 2, 3] ```<br>``` >>> print(l1 is l2) ```
[12-answer.txt](./12-answer.txt) | What do these 3 lines print? | ``` >>> l1 = [1, 2, 3] ```<br>``` >>> l2 = l1 ```<br>``` >>> print(l1 == l2) ```
[13-answer.txt](./13-answer.txt) | What do these 3 lines print? | ``` >>> l1 = [1, 2, 3] ```<br>``` >>> l2 = l1 ```<br>``` >>> print(l1 is l2) ```
[14-answer.txt](./14-answer.txt) | What does this script print? | ``` l1 = [1, 2, 3] ```<br>``` l2 = l1 ```<br>``` l1.append(4) ```<br>``` print(l2) ```
[15-answer.txt](./15-answer.txt) | What does this script print? | ``` l1 = [1, 2, 3] ```<br>``` l2 = l1 ```<br>``` l1 = l1 + [4] ```<br>``` print(l2) ```
[16-answer.txt](./16-answer.txt) | What does this script print? | ``` def increment(n): ```<br>```    n += 1 ```<br> <br> ``` a = 1 ```<br>``` increment(a) ```<br>``` print(a) ```
[17-answer.txt](./17-answer.txt) | What does this script print? | ``` def increment(n): ```<br>```    n.append(4) ```<br> <br> ``` l = [1, 2, 3] ```<br>``` increment(l) ```<br>``` print(l) ```
[18-answer.txt](./18-answer.txt) | What does this script print? | ``` def assign_value(n, v): ```<br>```    n = v ``` <br> <br> ``` l1 = [1, 2, 3] ```<br>``` l2 = [4, 5, 6] ```<br>``` assign_value(l1, l2)```<br>``` print(l1) ```
[19-copy_list.py](./19-copy_list.py) |  a function def copy_list(l): that returns a copy of a list.
[20-answer.txt](./20-answer.txt) | Is a a tuple? Answer with Yes or No. | ``` a = () ```
[21-answer.txt](./21-answer.txt) | Is a a tuple? Answer with Yes or No. | ``` a = (1, 2) ```
[22-answer.txt](./22-answer.txt) | Is a a tuple? Answer with Yes or No. | ``` a = (1) ```
[23-answer.txt](./23-answer.txt) | Is a a tuple? Answer with Yes or No. | ``` a = (1, ) ```
[24-answer.txt](./24-answer.txt) | What does this script print? | ``` a = (1) ```<br>``` b = (1) ```<br>``` a is b ```
[25-answer.txt](./25-answer.txt) | What does this script print? | ``` a = (1, 2) ```<br>``` b = (1, 2) ```<br>``` a is b ```
[26-answer.txt](./26-answer.txt) | What does this script print? | ``` a = () ```<br>``` b = () ```<br>``` a is b ```
[27-answer.txt](./27-answer.txt) | Will the last line of this script print 139926795932424? Answer with Yes or No. | ``` >>> id(a) ```<br>``` 139926795932424 ```<br>``` >>> a ```<br>``` [1, 2, 3, 4] ```<br>``` >>> a = a + [5] ```<br>``` >>> id(a) ```
[28-answer.txt](./28-answer.txt) | Will the last line of this script print 139926795932424? Answer with Yes or No. | ``` >>> a ```<br>``` [1, 2, 3] ```<br>``` >>> id (a) ```<br>``` 139926795932424 ```<br>``` >>> a += [4] ```<br>``` >>> id(a) ```
[100-magic_string.py](./100-magic_string.py) | a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code).
[101-locked_class.py](./101-locked_class.py) | a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
[103-line1.txt](./103-line1.txt) [103-line2.txt](./103-line2.txt) | How many int objects are created by the execution of the first line of the script?  (103-line1.txt) <br> <br> How many int objects are created by the execution of the second line of the script (103-line2.txt) | ``` julien@ubuntu:/python3$ cat int.py ```<br>``` a = 1 ```<br>``` b = 1 ```<br>``` julien@ubuntu:/python3$ ```
[104-line1.txt](./104-line1.txt) [104-line2.txt](./104-line2.txt) [104-line3.txt](./104-line3.txt) [104-line4.txt](./104-line4.txt) [104-line5.txt](./104-line5.txt) | How many int objects are created by the execution of the first line of the script? (104-line1.txt) <br> <br> How many int objects are created by the execution of the second line of the script (104-line2.txt) <br> <br> After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt) <br> <br>  After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt) <br> <br> How many int objects are created by the execution of the last line of the script (104-line5.txt)
[105-line1.txt](./105-line1.txt) | Assuming we are using a CPython implementation of Python3 with default options/configuration: <br> <br> Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt) <br> <br> Why? (optional blog post :)) <br> Hint: NSMALLPOSINTS, NSMALLNEGINTS | ``` julien@twix:/tmp/so$ cat int.py ```<br>``` print("I") ```<br>``` print("Love") ```<br>``` print("Python") ```<br> julien@ubuntu:/tmp/so$ 
[106-line1.txt](./106-line1.txt) [106-line2.txt](./106-line2.txt) [106-line3.txt](./106-line3.txt) [106-line4.txt](./106-line4.txt) [106-line5.txt](./106-line5.txt) | Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):<br> <br> How many string objects are created by the execution of the first line of the script? (106-line1.txt)<br> <br> How many string objects are created by the execution of the second line of the script (106-line2.txt)<br> <br> After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)<br> <br> After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)<br> <br> How many string objects are created by the execution of the last line of the script (106-line5.txt) | ``` guillaume@ubuntu:/python3$ cat string.py ```<br>``` a = "SCHL" ```<br>``` b = "SCHL" ```<br>``` del a ```<br>``` del b ```<br>``` c = "SCHL" ```<br>``` guillaume@ubuntu:/python3$ ``` 
