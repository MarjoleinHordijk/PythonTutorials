# Scripts and Functions

## What is a function?

Function can perform a particular operation, usually on one or several input variables. It is a block of code which is performed when the function is called. A function can return output data as a result, which you will then see appear in the console.

We can write a function ourselfs or use a standard function from Python. We can also call functions from packages / modules from third parties if we have those installed.

### Standard Python Functions

If you followed the "Introduction to Python" tutorial (see [Here](https://pythontutorials.readthedocs.io/en/latest/01_01_GetStarted.html "Introduction")), you have already encountered several standard functions. 

For example, ```print()``` can be used to print anything to the console output.

You can find an overview of other standard functions [Here](https://docs.python.org/3/library/functions.html#open "Standard functions").

![standardfunctions](https://github.com/MarjoleinHordijk/PythonTutorials/blob/master/images/01_02/1.png?raw=true)

### Arguments

Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses.

For example, you can pass a string (a piece of text) as argument to the ```print()``` function as such: ```print("some text")```.

### Writing your Own Functions

You can define your own function aswell. In this case the function will be a piece of code that you write yourself. 

To define a function, you will need to use the ```def``` keyword, followed by the name of the function, parenthesis and a colon.
Next will need to indent one level to start writing your function. You can indent using several spaces or tab. However, make sure that you always use the same indentation method throughout your script. If you this up, Python will not be able to recognize when you indent.

To illustrate, you can define a function that will print a piece of text. In the example below the function will print "My name is " followed by the name that is provided when the function is called. The provided name is in this case an argument.




## What is a Script?

If you quit Spyder (or another editor/IDE) and enter it again, the variables or functions that you defined in the console will be lost. However, you may want to store a particular sequence of commands for several reasons.

- You want to share the sequence with someone.
- You want to reuse the sequence later on.
- You want to continue working on the same process.

Fortunately, we can use scripting to store the sequence of commands for later use. In this way we can easily run the code again in one go. To illustrate, imagine you used a set of commands to clean a dataset and you would like to do exactly the same of a different set of data. You can run the script again for the new dataset without having to perform all the commands seperately again. Or maybe you want to help a peer student out to clean his dataset. You could simply send the script with this person.







