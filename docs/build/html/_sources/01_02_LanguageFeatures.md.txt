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

# Language Features

This section discusses some of the fundamental features of the Python language. Before we continue with actual programming, it is important that you are aware of the different terminology that is used. Therefore, this overview is very useful to review before starting to work with operators and functions. 

## 1. Variables and datatypes

As the name implies, the values of variables can vary. They store a piece of information and allow you to refer to this by its identifier. The identifiers is nothing more than a name that you define to identify the piece of information that is stored by the respective variable. Although you are quite flexible in choosing these names, there are some rules that you should stick to so Python can interpret your code properly.

**Rules for naming identifiers:**
- The first character of the variable name must always be a letter of the alphabet or an underscore (```_```).
- Python is case-sensitive. So keep that in mind when you are using lower (a) and upper (A) case letters.
- The remainder of the name can constist of letters, underscores (```_```) and digits (0-9).

Other than these rules, variables ideally have well-defined, good, and meaningful names, so that you can understand them as a developer. 

The information that is stored to those variables that you define can be of different data types.

**A number of important datatypes in Python include:**
- ```int``` - integer: integer value (no floating point)
- ```float``` - float: floating point number
- ```str``` - string: sequence of characters
- ```bool``` - boolean: binary value (```True``` or ```False```)

These datatypes are discussed in more detail below.

### 1.1 Numbers (Integers & Floats)
Python makes a distinction between two types of numbers. 
- **Integers** are whole numbers such as ```1```, ```23``` and ```2350525```. 
- **Floats** (floating point numbers) are so called "real" numbers. They are formulated with a decimal point and can capture fractions for integers. Examples include ```1.25``` and ```2e3``` (2 times 10 to the power of 3).

```python
# Integers
myInt = 1
anotherInt = -2018

# Floats
myFloat = 3.1415
anotherFloat = 2e3
```

### 1.2 Text (Strings)

A string is a sequence of characters. That is, they capture words, sentences, etc. However, they can also contain numbers. Keep in mind that if you define a number as a string, Pyton will interpret is as a piece of text (not a numerical value)!

Strings are specified using single, double and triple quotes. 
- Single and double quotes are interpreted exactly the same in Python. You can use them to specify one-line pieces of texts. Anything that is located between these quotes is treated as part of the string, including spaces, tabs, numbers, etc. 

```python
# Strings
myStr = "This is a string..."
anotherStr = 'This is also a string!'

# This is also a string. It is intepreted as a piece of text, not as a number!
# Hence, we cannot perform computational operations with this variable.
numberStr = '4' 
```

- Triple quotes can be used to specify multi-line strings

```python
# Multi-line Strings
'''This is a multi-line string. This is the first line.
This is the second line.
'''
```

Sometimes you might want to construct a text that containts values of other variables. For example, you might want to print a line of text that describes the output of your script. To do so, you can use the ```format()``` function. As you can see below, this allows us to insert the value of other variables in our piece of text. In this case, we have a sentence in which we insert a name and age. In later sections, you will learn in more detail how functions such as ```format()``` can be applied.

```python
age = 25
name = Marjolein

Str = "My name is {0} and I am {1} years old.".format(name,age)
```

If you print this string to your console (using ```print(Str)```), you will get the following output.
- My name is Marjolein and I am 25 years old.

### 1.3 Boolean

Booleans are special in the sense that they only take two values *True* and *False*. These are basically evaluations of some related statement. For example, if we provide 10<20 as a statement, the booleans evaluation would be *True* (indeed, 10 is smaller than 20). We will use this datatype later when we write conditional statements.

```python
# boolean
myBool = True
anotherBool = 10 < 20
```

### 1.4 Find out the datatype of a variable

To find out the datatype of a variable, use the ```type()``` function. When you put the variable name between the parentheses, this function will return the datatype of the variable. 

```python
buildingName = "Vertigo"
type(buildingName)
```

****
### Exercise 1: Data Types and Printing
<div class="exercise"><strong>Try it for yourself! If you add the piece of code below to a .py file in the Spyder editor and run it, you will be able to see the variables, their types and value appear in the Variable Explorer tab. You can now use these variables later in your script.</strong><br/><br/>

1. Try running ```print(myStr)``` from the console to print the value of the ```myStr``` variable to the console window.
2. Also, run ```type(numberStr)``` to confirm that the value ```4``` is indeed a string and not an integer or float.
3. Find out the value of the variable ```anotherBool``` by printing it to the console using ```print()```. What does this value tell you?
4. Create a variable called ```university``` with the value ```TU/e``` and one called ```myName``` with your name as its value. Finally, add another variable called ```sentence``` and use the ```format()``` function to construct the following sentence: "My name is <here your name> and I study at <here your university>.". Now print this sentence to the console window using ```print()```.

</div>
<br/>


Are you having trouble using Spyder? Please refer back to section 3 of [this](01_01_GetReady.md) tutorial.

```python
# Integers
myInt = 1
anotherInt = -2018

# Floats
myFloat = 3.1415
anotherFloat = 2e3

# Strings
myStr = "This is a string..."
anotherStr = 'This is also a string!'

# This is also a string. It is intepreted as a piece of text, not as a number!
# Hence, we cannot perform computational operations with this variable.
numberStr = '4' 

# Multi-line Strings
'''This is a multi-line string. This is the first line.
This is the second line.
'''

# boolean
myBool = True
anotherBool = 10 < 20
```

![](../../images/01_02/1.png)

****

## 2. Special Data Structures

In addition to the datatypes discussed above, Python uses several special data structures that can hold multiple pieces of information. That is, they store a collection of data. 

**There are four built-in data structures in Python:**
- ```list``` - List: A sequence of items. Ordered & editable.
- ```tuple``` - Tuble: A sequence of items. Ordered & not editable.
- ```dict``` - Dictionary: A collection of key-value pairs.
- ```set``` - Set: A collection of items. *Not* ordered.

### 2.1 Lists

A list refers to a sequence of multiple items, which can be of different datatypes. Important to remember is that the order of these items is fixed and the content of the list is editable. You define a list using square brackets (```[]```) and seperate items using commas (```[item1, item2, etc]```)

```python
# Lists
myList = [2, 4, 42, 3.1415, 5000]
anotherList = ["Alpha", "Bravo", "Charlie"]

item1 = 1
item2 = 2

itemsList = [item1, item2]
```

### 2.2 Tuples

Tuples are very similar to lists. However, they allow for far less operations to be performed on them. They are not editable. Something which may seem impracticle at first, but this can sometimes actually be very useful. You can use them for sequences that should at all times remain intact. You define a tuple using round brackets (```()```).

```python
# Tuples
myTuple = (2, 4, 42, 3.1415, 5000)
anotherTuple = ("Alpha", "Bravo", "Charlie")
```

### 2.3 Sets

Sets differ from lists or tuples, because they are not ordered. That is, they do not contain a sequence of items, but simply an unordered collection of them. A set is defined using ```set([item1, item2, etc])```. As you might notice, this is a function!

```python
# Set
mySet = set([item1, item2, item3])
```

### 2.4 Dictionaries

Dictionaries in Python can be compared to physical dictionaries. If you want to know the meaning of a particular word, you start searching for the word (key) and at some point you will be able to find the corresponding meaning (value). The *values* in a dictionary variable are "bookmarked" using *keys*. Therefore we talk about key-value pairs. The combination of a word in the physical dictionary and its meaning would be a key-value pair. The values in a dicationary (as opposed to the keys!) can change over time.

You define a dictionary ```d``` with two items as ```d = {key1 : value1, key2 : value2 }```. The key-value pairs are separated by commas, much like the items in a list. The key and values themselves are seperated by a colon. You could now use ```key1``` to look up ```value1```. 

Take as an example this dictionary that stores the ages of a group of people.

```python
# Dictionary
myDic = {Marjolein : 25, Anne : 36, Caroline: 50}
```

How to work with these special data structures is discussed in a later section. That is, how can we retrieve or edit the data from these structures?

****
### Exercise 2: Special Data Structures
<div class="exercise"><strong>We will discuss how to actually use these special data structures in a later section on operations. However, it is important for now that you understand the differences and know how to define variables of these types.</strong><br/><br/>
    <ol>
        <li>Someone is keeping a record of the names of all students that took a Python course. New people get added whenever they complete the course, which can be at different moments in time. Which of the above datatypes are suitable to store this data? Why are the others not suitable?</li>
		<li>Create a variable that stores a hypothetical list of students that took the python course.</li>
		<li>You would like to store series of temperature measurements. The measurements are taken every minute. What datatype would you chose? Are there other options? In what situation would you have a specific preference? What are your considerations?</li>
		<li>Create a variable that stores a series of ten time measurements.</li>
		<li>Reflect on the variable you just created. Can Python tell which measurement was taken before another? (Is the order specified?)</li>
		<li>Are you able to tell at what time each measurement was taken, without knowing when you started measuring? If not, can you respecify the variable so that this is actually possible?</li>
	</ol> 
</div>
<br/>

****

## 3. Literal Constants

In addition to variables, we can also use so called "Literal Constants". Examples include numbers or pieces of text (strings). It is called a **literal** because it is literal - you use its value literally. That is, ```4``` is not a variable storing some value. It is the actual value four itself. Likewise, ```"This is a string."``` is a string, a piece of text, and not a variable that stores it. They are **constant** in the sense that the value does not change. For example, ```4``` will always have the value of four. It will never change its value to five, or a string for that matter.

## 4. Comments

Comments are used to document your code inline.
This can be very helpful for others (or yourself) to understand your script and keep overview.
As you might have noticed, we actually already used comments in our previous example codes.

- ```”””``` comments multiple lines until ”””
- ```#``` comments out a single line

****
### Exercise 3: Comments
<div class="exercise"><strong>Comments are very useful to help others understand your code. In Exercise 1, you developed a code for printing a sentence. Add comments to this code to make it as readable as possible to someone who is also a beginner in programmig.</strong>
</div>
<br/>

****

## 5. Operators

Operators allow to perform operations on variables of particular data types. Although this might sound a bit abstract, hopefully the examples below will clear things up for you.

A number of operators are available. There are plenty of cheat sheets online that provide an overview of commonly used ones. An example of such an sheet is shown below.

![](../../images/01_02/2.jpg)

### 5.1 Number and boolean operators

Operators that can be used on numbers and boolean variables are likely familiar to you. They are often used in math.

<div class="info">

X and y are examples of variables on which the operators are performed.

**Arithmetic operators:**
- x plus y: ```x + y```
- x less y: ```x - y```
- product of x and y: ```x * y```
- x over y: ```x / y```
- x to the power of y: ```x ** y```

**Assignment operators:**
- x equals y: ```x = y``` (assigning the value of y to x)
- x equals x + y: ```x += y``` (adding y to the current value of x)

**Comparison operators:**
- Is x equal to y?: ```x == y``` 
- Is x equal to y? (When x & y are boolean) ```x is y```
- Is x not equal to y? (When x & y are boolean) ```x is not y```
- Is x greater than y?: ```x > y```
- Is x smaller than y?: ```x < y```
- Is x greater or equal to y?: ```x >= y```
- Is x smaller or equal to y?: ```x <= y```

**Logical operators:**
(When x & y are boolean)
- Are both x and y True?: ```x and y```
- Is x or y True?: ```x or y```

</div>
<br/>
<br/>

### 5.2 Indexes

Indexes in Python refer to the order of elements. These elements can for example be characters within a string or items in a list.

Two things are important to remember:
- Python starts counting from 0. That is, the first character in a string has index value 0 and the second character value 1 and so on.
- When you define a range, the first value that you provide is included, but the last one is not.

So if we take for example the variable ```CityName = "Eindhoven"```, the index of the ```E``` in Eindhoven is 0 (because it is the first characters). The index of the final character ```n``` is 8 (not 9!). 

![](../../images/01_02/2.png)

We can define a range of indexes using square brackets ```[FirstIndex:LastIndex]```. When we put this behind the name of a string variable, Python will return the section of the string defined by this range. Likewise, if we put this behind a list variable, we will get the specific items that the range covers.

To illustrate, this ```StringVariable[1:5]``` excludes the first character of ```StringVariable``` (because 0 is not included in the range), but also the sixth one (which has index value 5!).
Likewise, ```ListVariable[0:3]``` returns the first, second and third item from ```ListVariable```, but not the fourth (although the index if the fourth item is 3!). 

More specific examples will folow in the next sections.

****

### Exercise 4: Indexes in Python
<div class="exercise"><strong>Indexes in Python can be somewhat counterintuitive at the beginning. Below are some exercises to practice with.</strong><br/><br/>

1. Create a string variable that stores your name.
2. What is the second character of your name?
3. Now retrieve the second character based on the index and print it to the console window.
4. Also, print the first two characters of your name to the console windows.

</div>
<br/>

****

### 5.3 String operators
A number of operators allow us to operate with strings. 

First of all, we can combine strings into one using ```+```. This is also called *string concatenation*. 
- ```"CME" + " Master!"``` => "CME Master!"

Moreover, we can take out certain parts of a string. To do so, we have to provide a range of index values. These index values refer to the characters in the string. We can extract a part of a string by typing the string name, followed by the range of index values between square brackets.

Some examples for the variable	```CityName = "Eindhoven"```:
- ```CityName[0]``` => 'E'
- ```CityName[1:5]``` => 'indh'
- ```CityName[:3]``` => 'Ein' #Everything until 3 (exclusive)
- ```CityName[3:]``` => 'dhoven' #Everything from 3 (inclusive)

Finally, we can use the ```len()``` function to determine the length of a string, which corresponds to the number of characters. So for ```CityName = "Eindhoven"```:
- ```len(CityName)``` => '9'

****

### Exercise 5: Operating on Strings
<div class="exercise"><strong>The exercises below help you practice with the different string operators.</strong><br/><br/>

1. Again, create a string variable that stores your name.
2. Print the final two characters of your name to the console window.
3. Determine the length of your name using ```len()```.
4. Create another string variable that stores your lastname. Use string concatenation (```+```) to create a new variable which containts both your first- and lastname. Print this variable to the console.

</div>
<br/>

****

### 5.4 List operators

Similar to strings, we can use the indexing to extract particular parts of a list. Note that is this case the indexes do not refer to characters, but to items in the list.

Take for example these two lists:
- ```list_of_numbers = [1, 2.5, 3, 52]```
- ```list_of_strings = ["abc", "xyz", "12345"]```

We can extract particular items from these lists as shown below:
- ```list_of_numbers[1]``` => 2.5
- ```list_of_numbers[-1]``` => 52
- ```list_of_strings[1]``` => "xyz"
- ```list_of_strings[1:]``` => ["xyz", "12345"]
- ```list_of_strings[2][3:]``` => "45"

We can also use operators to generate lists. We saw before that we can define a list by putting the values between square brackets and seperating them by commas. However we acn also use ```list()``` and ```range()``` to construct lists automatically. The function ```range()``` generates a range of values between a starting point and an end point. For example, if we type ```list(range(3,10,2))```, we create a list of the values 3 till 9 with a step of 2. That is, 3, 3+2=5, 5+2=7, 7+2=9. In this case, the endpoint 10 is not included, because the next value after 9 would be 11, given the time step of 2 (and 11 being out of range). 

List of numbers can be generated in multiple ways:
- ```numList = [0, 1, 2, 3]``` => [0, 1, 2, 3]
- ```numList = list(range(4))``` => [0, 1, 2, 3]
- ```numList = list(range(3,10,2))``` => [3, 5, 7, 9] #start,stop,step

Indexing can happen in steps as well
- ```myList (list(range( 10))``` => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
- ```myList [::2]``` => [0, 2, 4, 6, 8] #[start:stop:step]
- ```myList [2:9:3]``` => [2, 5, 8]
- ```myList [::-1]``` => [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

****

### Exercise 6: Operating on Lists
<div class="exercise"><strong>The exercises below help you practice with the different list operators.</strong><br/><br/>

1. Create three lists of the numbers 5, 6, 7, and 8. Do so using the different methods discussed above. Print the lists to the console to confirm that they are indeed the same.
2. What is the quickst way of generating a list ranging from 0 upto and including 100 with steps of 5 in between. (So: 0, 5, 10, 15, ... , 95, 100) Specify a the list and print it to the console window to confirm.
3. Use indexing on the variable created in the previous question to print the values between 30 and 80 (excluding 30 and 80) which can be devided by 10. (So: 40, 50, 60, 70)

</div>
<br/>

****

## 6. An Introduction to Functions

Throughout the previous section, we have already encountered a couple of functions such as ```print()``` and ```format()```. A later section on [functions](01_04_Functions.md) goes into detail about how functions work, how we can find and call them and even how we can develop our own. For now, it is important to be aware of a couple of things.

- You can call a function within a script or from a console (e.g. when we ran ```print(myStr)``` from the Spyder console).
- When you call a function, you usually have to provide one or several arguments. Arguments are specified after the function name, inside the parentheses. For example, in ```print(myStr)```, ```myStr``` is the argument that we pass to the ```print()``` function. You could see it as input that we provide the function with. (We want to ```print()``` the value of ```myStr```.)
- If a function takes multiple arguments, you can seperate them by a comma. The arguments should be provided in the order in which the function will use them. We will use this later [here](01_04_Functions.md).

****

### Exercise 7: Introduction to Functions
<div class="exercise"><strong>To give you a heads start on the tutorial on functions, you can try the exercise below.</strong><br/><br/>

1. Copy the following code to a script in Spyder.

```python
def myFunction(Name, Age):
	print ("My name is " + Name + " and I am " + Age + " years old.")
```

2. This code specifies a function called ```myFunction``` which prints a sentence. What are ```Name``` and ```Age``` for this function?
3. If you look closely to the function definition, you will see that we add pieces of string and Name and Age together. What is it called when we add strings together?
4. Specify two string variables; one which stores your name and another one storing your age. Please be aware that you cannot combine a string and number. To solve this, make sure that your age is stored as a string.
5. In the console, run ```myFunction(Name, Age)```. What happens? Why does this happen?
6. Run the code. In the console, run ```myFunction(Name, Age)``` again. What happens now?

</div>
<br/>

