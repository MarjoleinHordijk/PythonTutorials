<html>
<head>
<style>
.info {
  background-color: #e6e6e6;
  border-left: 6px solid #666666;
  padding: 10px;
}
.exercise {
  background-color: #e7f3fe;
  border-left: 6px solid #2196F3;
  padding: 10px;
}
</style>
</head>
<body>

# Functions

## 1. What is a function?

Function can perform a particular operation, usually on one or several input variables. It is a block of code that is performed when the function is called. A function can return output data as a result, which you will then see appear in the console. When we chain a sequence of functions, the output of one function can become the input for another.

For now, we will focus on writing our own functions and using those that are shipped with Python. We can also call functions from packages/modules from third parties if we have those installed. In "Beyond the Basics" you will discuss the latter in greater detail.

### 1.1 Arguments

Information can be passed to functions through arguments. They can include input data that must be processed or parameters that specify how the function should be applied. To illustrate, a parameter could be used to indicate what the datatype of the output should be or whether or not to perform a specific operation that is included in the function. You will get more familiar with this when you gain more experience in coding.

Arguments are specified after the function name, inside the parentheses.

For example, you can pass a string (a piece of text) as an argument to the ```print()``` function as such: ```print("some text")```.

****
#### Exercise 1: What are arguments?
<div class="exercise"><strong>We have used arguments before in earlier segments, although you might not have been completely aware of it. Below are some exercises regarding the functions that we have already used. These will help you to gain a better understanding of what arguments are.</strong><br/><br/>

1. Specify four variables storing:
    * A sentence
    * A number
    * A word
    * A boolean
2. Run ```type()``` to check the datatypes of the variables you just created.
3. What were the arguments that you passed to the ```type()```?
4. Use ```len()``` to determine the amount of characters in your sentence.
5. Of what datatypes can the arguments that you pass to ```len()``` be?
6. Create one argument to pass to ```print()``` that contains both the word and the number separated by a space character. Test if your solution works. (Hint: use ```str()```!)
</div>
<br/>

****

## 2. Standard Python Functions

If you followed the preceding tutorials, you have already encountered several standard functions. For example, ```print()``` can be used to print something to the console output. Also, we used ```str()``` to convert numbers into strings. 

You can find an overview of other standard functions [Here](https://docs.python.org/3/library/functions.html).

![](../../images/01_04/1.png)

### 2.1 Functions for dataype conversions

Python supports various data-types, such as text (string) or numbers (integers, floats). However, in some cases you are able to capture a particular piece of information with multiple data-types. For example, you can store your age in full years as an integer or float, but also as a small piece of text (string). 

In some cases, a particular data-type might be more applicable or straightforward than another. It could also be that a function requires the input to be of a specific datatype. If the data you have does not correspond to the desired data-type, you can convert it using some build-in functions of Python.

- ```str()```: Converts the data provided as argument into a string (text).
- ```int()```: Converts the data provided as argument into an integer (whole number).
- ```float()```: Converts the data provided as argument into a real number (decimal number).
- ```list()```: Converts the data provided as argument into a list.
- ```dict()```: Converts the data provided as argument into a dictionary.

****
#### Exercise 2: Conversions
<div class="exercise"><strong>Try it out for yourself by following the steps below!</strong><br/><br/>

* Add the following piece of code to a .py file in the editor panel of Spyder.

```python
myString="25"
myInteger=25
myFloat=25.2
```

* Run the code (by pressing the small play button).
* Try running the following commands. You will see that not all of them work. This happens because the ```print()``` function can only take strings as an argument when you provide them in this manner.

```python
print ("I am " + myString + " years old.")
print ("I am " + myInteger + " years old.")
print ("I am " + myFloat + " years old.")
```
![](../../images/01_04/5.png)

* To solve this issue, we can convert the integer and float data to string data as follows. Try if this indeed works.

```python
print ("I am " + str(myInteger) + " years old.")
print ("I am " + str(myFloat) + " years old.")
```

![](../../images/01_04/6.png)

* Alternatively, you might want to convert the decimal numbers in your dataset to whole numbers (integers). You can do this by converting the float data to integer data as shown below. When you run this, you will see that the variable "converted" of data-type "int" is added to your Variable Explorer panel in Spyder.

```python
converted = int(myFloat)
```

![](../../images/01_04/7.png)

</div>
<br/>

****

## 3. Writing your Own Functions

You can define your own function as well. In this case the function will be a piece of code that you write yourself. 

### 3.1 Functions with One Argument

To define a function, you will need to use the ```def``` keyword, followed by the name of the function, parenthesis and a colon.
Next, you must indent one level to start writing your function. You can indent using several spaces or tab. However, make sure that you always use the same indentation method throughout your script. If you this up, Python will not be able to recognize when you indent.

<div class="info">

Are you not sure what **indentation** is and why it is so important in Python?
Please check out the section on "Indentation" on the [help page](06_Help.md). You will find everything you need to know about indentation there!

</div>
<br/>

****
#### Exercise 3: Writing a Function with One Argument
<div class="exercise"><strong>To illustrate, we will define a function that will print a piece of text. In the example below the function will print "My name is " followed by the name that is provided when the function is called. The provided name is in this case an argument.</strong><br/><br/>

- Add the following piece of code to a .py file in the editor panel in Spyder.

```python
def myFunction(name):
    print("My name is " + name + ".")
```

- Run the code by pressing the small play button.

- Call the function from the console panel and provide your name as an argument to the function.

```python
myFunction("Marjolein")
```
- You will see the output in the console window.

![](../../images/01_04/2.png)

</div>
<br/>

****

### 3.1 Functions with Mutiple Arguments

You can also create a function that takes multiple arguments by separating them with a comma when you define the function.

****
#### Exercise 4: Writing a Function with Multiple Arguments
<div class="exercise"><strong>As an illustration, we will extent the function we developed in the previous exercise. We will not only inclde a name in the sentence we want to print, but also the age.</strong><br/><br/>

- Add the following piece of code to a .py file in the editor panel. We use ```str()``` here to change the integer argument (your age) to a string so it can be printed as text.

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

![](../../images/01_04/3.png)

- Specify four variables (```var1``` - ```var4```) of different data-types at the start of a new script.

- Define a function that prints four sentences, each of which describes the data-type of each of the four variables.

- Test if the function works properly.

</div>
<br/>

****

### 3.3 Asking for Input

You can use the ```input()``` function to ask the user of your code for input. For example you can ask for someone's name and use this input to print a sentence.

****
#### Exercise 5: Writing a Function that Asks for Input
<div class="exercise"><strong>We will again go back to our earlier function, which prints a sentence containing a name and age.</strong><br/><br/>

- Add the following piece of code to a .py file in the editor panel.

```python
print("What is your name?")
name = input()
print("Welcome to the course, " + name)
```
- Run the code by pressing the small play button.

- You will see the question for your name appear. Provide your name as input.

- You should see the sentence appear with your name filled in.

![](../../images/01_04/4.png)

- Now, use this code to develop a function and call the function from the console.

- Does the function you developed in the previous step take any arguments?

- Extent the function so that it also asked for the person's age and it prints a sentence which contains the inputted age. That is, formulate a function which asked for two inputs.

</div>
<br/>

****

## 4. Functions from Packages / Modules

As said before, you can also access functions developed by others from packages or modules. These can be downloaded and usually contain a large set of functions related to a particular goal. For example, NumPy is a package that contains function to perform scientific computations. You can install this package to use the functions that it offers. 

Installing and using packages or modules is out of the scope of this introduction. Do you want to learn how to install packages or modules? Please refer to [this](02_01_Modules&Packages.md) tutorial.






