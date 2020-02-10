# Language Features

## 1. Variables and datatypes
A python script works with data. This data can be stored in variables with certain datatypes.

A number of datatypes are available in python:
- ```int``` - integer: integer value (no floating point)
- ```float``` - float: floating point number
- ```str``` - string: sequence of characters
- ```list``` - list: list of datatypes
- ```bool``` - boolean: binary value (```True``` or ```False```)

Values in any of these datatypes can be stored in variables. 
These variables ideally have well-defined, good, and meaningful names, so that you can understand them as a developer. 

Examples:

```python
# integers
myInt = 1
anotherInt = -2018

# float
myFloat = 3.1415
anotherFloat = 2e3

# string
myStr = "Eindhoven University of Technology ... !?"
anotherStr = "what a #great university"

# list
myList = [2, 4, 42, 3.1415, 5000]
anotherList = ["Alpha", "Bravo", "Charlie"]

# boolean
myBool = True
anotherBool = 10 < 20
```

Try it for yourself! If you add the piece of code above to a .py file in the Spyder editor and run it, you will be able to see the variables, their types and value appear in the Variable Explorer tab.
You can now use these variables later in your script. For example, you can run ```print(myStr)```.

![](../../images/01_02/1.png)

There are some rules to defining variable names. Variable names may not contain spaces. Python will then not be able to recognize multiple words as one name. Further, variable names can not start with a number.

```python
# bad / not allowed
my name = "John Doe" #variable names can not include spaces
1like = 1prayer #variable names can not start with a number
```

To find out the datatype of a variable, run:
```python
buildingName = "VRT9"
print(buildingName)
print(type(buildingName))
```

## 2. Comments
Comments are used to document your code inline.
This can be very helpful for others (or yourself) to understand your script and keep overview.
As you might have noticed, we actually already used comments in our previous example codes.

- ```”””``` comments multiple lines until ”””
- ```#``` comments out a single line

## 3. Operators
Operators allow to perform operations on variables of particular data types. A number of operators are available. There are plenty of cheat sheets online that list the different available operators. If you don't know what to use to do something, Google it first; or search for a solution in the cheat sheets.

![](../../images/01_02/2.jpg)

### Number and boolean operators

(X and y are examples of variables on which the operators are performed.)

- Arithmetic
	- ```x + y```
	- ```x - y```
	- ```x * y```
	- ```x / y```
	- ```x ** y``` (notation for x^y)
- Assignment
	- ```x = y```
	- ```x += y``` (same as x = x + y)
- Comparison:
	- ```x == y``` (equal) => use ```x is y``` when x or y is a ```boolean```
	- ```x != y``` (not equal) => use ```x is not y``` when x or y is a ```boolean```
	- ```x > y``` (greater than)
	- ```x < y``` (smaller than)
	- ```x >= y``` (greater or equal than)
- Logical
	- ```x and y``` (True if both are True)
	- ```x or y``` (True if one is True)
	
### String operators
A number of operators allows to operate with strings. Note that Python starts counting from 0. The first character in a string is thus character number 0.

- String concatenation:
	- ```"CME" + " Master!"``` => "CME Master!"
- Selecting parts of strings and handling string length
	- ```CityName = "Eindhoven"```
	- ```CityName[0]``` => 'E'
	- ```CityName[1:5]``` => 'indh'
	- ```CityName[:3]``` => 'Ein' #Everything until 3 (exclusive)
	- ```CityName[3:]``` => 'dhoven' #Everything from 3 (inclusive)
	- ```len(CityName)``` => '9'

### List operators
Lists can contain everything:

- ```list_of_numbers = [1, 2.5, 3, 52]```
- ```list_of_strings = ["abc", "xyz", "12345"]```

Indexing is the same as for single strings: Python starts to count from 0.
- ```list_of_numbers[1]``` => 2.5
- ```list_of_numbers[-1]``` => 52
- ```list_of_strings[1]``` => "xyz"
- ```list_of_strings[1:]``` => ["xyz", "12345"]
- ```list_of_strings[2][3:]``` => "45"
	
List of numbers can be generated in multiple ways:
- ```numList = [0, 1, 2, 3]``` => [0, 1, 2, 3]
- ```numList = list(range(4))``` => [0, 1, 2, 3]
- ```numList = list(range(3,10,2))``` => [3, 5, 7, 9] #start,stop,step

Indexing can happen in steps as well
- ```myList (list(range( 10))``` => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
- ```myList [::2]``` => [0, 2, 4, 6, 8] #[start:stop:step]
- ```myList [2:9:3]``` => [2, 5, 8]
- ```myList [::-1]``` => [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
