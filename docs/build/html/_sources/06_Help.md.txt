# Help

This page provides you with an overview of all kinds of concepts, definitions and issues that relate to multiple tutorials.

## Indentation

Python uses identation to define blocks of code. An indent is nothing more than a piece of whitespace at the start of your line. This piece of whitespace can be a certain amount of spaces (e.g. 4) or tabs. However, you have to be consitent throughout your piece of code! Otherwise Python will not recognize the structure of your coding. Incorrect indentation will result in an ```IndentationError```.

The enforcement of indentation in Python makes the code look neat and clean.

Consider the example of a simple if statement below.

```python
a=2
b=4

if a<b:
    print("The value of b is larger than a.")
    difference = b-a
    print("The value of b is " + difference + " units larger than a.")
```

As you can see, we indent by one level after the conditional statement ("if a<b:"). In this example, tabs were used to indent. 

It is possible to write this same piece of code without indentation, however it will be far less readable.
As you can see below, this is done by seperating the different actions to be executed by a semicolon (;).

```python
a=2
b=4

if a<b: print("The value of b is larger than a."); difference = b-a; print("The value of b is " + difference + " units larger than a.")
```

Using different indent types in one piece of code, as shown below, will lead to a ```IndentationError```. Although the indents may seem to have the same lenght, the line that reads "```difference = b-a```" actually has four spaces as indent instead of a tab.

```python
a=2
b=4

if a<b:
    print("The value of b is larger than a.")
    difference = b-a
    print("The value of b is " + difference + " units larger than a.")
```