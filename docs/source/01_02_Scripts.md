# Scripts and Functions

## What is a function?

Function can perform a particular operation, usually on one or several input variables. It is a block of code which is performed when the function is called. A function can return output data as a result, which you will then see appear in the console.

We can write a function ourselfs or use a standard function from Python. We can also call functions from packages / modules from third parties if we have those installed.

### Standard Python Functions

If you followed the "Introduction to Python" tutorial (see [Here](https://pythontutorials.readthedocs.io/en/latest/01_01_GetStarted.html)), you have already encountered several standard functions. 

For example, ```print()``` can be used to print anything to the console output.

You can find an overview of other standard functions [Here](https://docs.python.org/3/library/functions.html#open).

![standardfunctions](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_02/1.png?raw=true)

### Arguments

Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses.

For example, you can pass a string (a piece of text) as argument to the ```print()``` function as such: ```print("some text")```.

### Writing your Own Functions

You can define your own function aswell. In this case the function will be a piece of code that you write yourself. 

To define a function, you will need to use the ```def``` keyword, followed by the name of the function, parenthesis and a colon.
Next will need to indent one level to start writing your function. You can indent using several spaces or tab. However, make sure that you always use the same indentation method throughout your script. If you this up, Python will not be able to recognize when you indent.

#### A Simple Function

To illustrate, you can define a function that will print a piece of text. In the example below the function will print "My name is " followed by the name that is provided when the function is called. The provided name is in this case an argument.

- Add the following piece of code to a .py file in the editor panel.

```python
def myFunction(name):
    print("My name is " + name + ".")
```

- Run the code by pressing the small play button.

- Call the function from the console panel and provide your name as argument to the function.

```python
myFunction("Marjolein")
```
- You will see the output in the console window.

Output: My name is Marjolein.

![ownprintfunction](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_02/2.png?raw=true)

#### A Function with Mutiple Arguments

You can also create a function that takes multiple arguments by seperating them with a comma when you define the function.

- Add the following piece of code to a .py file in the editor panel.

We use ```str()``` here to change the integer argument (your age) to a string so it can be printed as text.

```python
def myFunction(name, age):
    print("My name is " + name + " and I am " + str(age) + " years old.")
```

- Run the code by pressing the small play button.

- Call the function from the console panel and provide your name as the first argument, and you age as a second one.

```python
myFunction("Marjolein", 25)
```
- You will see the output in the console window.

Output: My name is Marjolein and I am 25 years old.

![ownfunctiontwoarguments](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_02/3.png?raw=true)

#### Asking for Input

You can use the ```input()``` function to ask the user of your code for input. For example you can ask for someone's name and use this input to print a sentence.

- Add the following piece of code to a .py file in the editor panel.

```python
print("What is your name?")
name = input()
print("Welcome to the course, " + name)
```
- Run the code by pressing the small play button.

- You will see the question for you name appear. Provide your name as input.

- You should see the sentence appear with your name filled in.

![ownfunctioninput](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_02/4.png?raw=true)

### Functions from Packages / Modules

As said before, you can also access functions developed by others from packages or modules. These can be downloaded and usually contain a large set of functions related to a particular goal. For example, NumPy is a package that containts function to perform scientific computations. You can install this package to use the functions that it offers. 

Installing and using packages or modules is out of the scope of this introductory tutorial.
However you will find more information on this in other tutorials available on the repository!

## What is a Script?

If you quit Spyder (or another editor/IDE) and enter it again, the variables or functions that you defined in the console will be lost. However, you may want to store a particular sequence of commands for several reasons.

- You want to share the sequence with someone.
- You want to reuse the sequence later on.
- You want to continue working on the same process.

Fortunately, we can use scripting to store the sequence of commands for later use. In this way we can easily run the code again in one go. To illustrate, imagine you used a set of commands to clean a dataset and you would like to do exactly the same of a different set of data. You can run the script again for the new dataset without having to perform all the commands seperately again. Or maybe you want to help a peer student out to clean his dataset. You could simply send the script with this person.







