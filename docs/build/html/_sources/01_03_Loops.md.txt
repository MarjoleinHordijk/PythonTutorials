# Loops and Conditional Statements

Loops and conditional statements are very common elements of scripts. These structures allow us to specify what should happen when a particular condition is satisfied or not. 

## 1. Writing conditional statements

Python supports many of the usual logical conditions from mathematics:

- Equals: ```a == b```
- Not Equals: ```a != b```
- Less than: ```a < b```
- Less than or equal to: ```a <= b```
- Greater than: ```a > b```
- Greater than or equal to: ```a >= b```

In these examples, a and b can take different values and they can be of different datatypes. However, be aware that certain data types are not suitable for praticular logical contitions. For example, if we have a piece of text "Univeristy", which is a string, it will be impossible to evaluate if this is greater than another value. Although this may seem obvious in this example, it could be possible that you stored two numbers (e.g 2 & 4), but you stored one of them as a string instead of an integer. In this case, you will also receive an error. Please see [here](01_02_LanguageFeatures.md) for more on datatypes such as strings and integers.

## 2. If statement
If statement allow you to check whether a particular statement is true or not. Depending on the boolean evaluation (true versus false), a particular piece of code (or nothing) is executed. 

The header line of the if statement begins with the keyword ```if``` followed by a boolean expression and ends with a colon (:). The indented statements that follow are called a block. This block contains the code that should be executed when the condition is satisfied. Each statement inside the block must have the same indentation. The first unindented statement marks the end of the block. 

```python
if <conditional statement>:
	<code to be executed when conditional statement is TRUE>
```

If you would like to specify what happens when the conditional statement is not true, you can use a ```if else```. 

```python
if <conditional statement>:
	<code to be executed when conditional statement is TRUE>
else:
	<code to be executed when conditional statement is FALSE>
```

We can also chain conditional statements to be checked using a ```if elif else``` structure as shown below.

```python
if <first conditional statement>:
	<code to be executed when first conditional statement is TRUE>
elif <second conditional statement>:
	<code to be executed when second conditional statement is TRUE>
elif <third conditional statement>:
	<code to be executed when third conditional statement is TRUE>

...

else:
	<code to be executed when all conditional statements above are FALSE>
```

In the case that you do not want to execute any code in a particular situation, you can use ```pass```.

**Important things to keep in mind when writing if statements:**
* Be aware of the indentation. That is, the code that must be executed is indented by one level. Click [here](06_Help.md) to learn more about identation.
* Do not forget the colon (:), it seperates the header of the statement from its body.
* Several forms of if statements are possible, as shown below. They differ in the amount of conditions that are checked. 

Below you can find several examples of if statements.

### 2.1 One condition

The most basic form of an if statement checks one condition. If this condition is true, the code below it will be executed. If the condition is not true, it will always perform the second piece of code.

*If this is true, do that. Otherwise, do this.*

```python
a = 12
b = 5
if a > b:
	print("a is greater than b")
else:
	print("a is not greater than b")
```

![](../../images/01_03/1.png)

### 2.2 One condition, pass

As adressed above, we can use ```pass``` to specify that we do not want any code to be executed in a particular situation. In the example below, this is the case when the if statement (a > b) is not true.

*If this is true, do that. Otherwise, do nothing.*

```python
a = 12
b = 5
if a > b:
	print("a is greater than b")
else:
	pass
```
![](../../images/01_03/2.png)

### 2.3 Multiple conditions

As mentioned before, we can chain multiple statements using a ```if elif else``` structure. In this way we can capture all situations where the program should perform specific behavior.

*If this is true, do that. Else check if this is true, and do that. Else do this.*

```python
a = 3
b = 5
if a > b:
	print("a is greater than b")
elif a == b:
	print("a is equal to b")
else:
	print("b is greater than a")
```

![](../../images/01_03/3.png)

## 3. While-loop
In a While-loop, a certain script is performed as long as a particular boolean statement evaluates to True.

*While this is true, do*

```python
i = 1
while i < 10:
	print(i)
	i += 1 #i = i + 1
```

A while-loop can be interrupted or loops in a while-loop can be skipped using the ```break``` and ```continue``` statements.

```python
i = 1
while i < 10:
	print(i)
	if i == 5:
		break
	i += 1

i = 1
while i < 10:
	print(i)
	if i == 5:
		continue
	i += 1
```

## 4. For-loop
*For every element in this entire sequence, do*

```python
cars = ["Volvo", "Ford", "Mercedes"]
for carName in cars
	print(carName)
		
city = "Eindhoven"
for letter in city
	print(letter)
```








