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

# Linear Regression Analysis Using Python

## In this Tutorial
In this tutorial, we will discuss how to perform a linear regression analysis using Python. Specifically, we will use the well known package ```NumPy```. This package allows you to work with multi dimensional data arrays and perform particular calculations with them. You can find more information about this package in its [official guide](https://docs.scipy.org/doc/numpy/user/index.html). Additionally, we will use the ```scikit-learn``` library to perform the actual analysis. Please make sure you have both installed!

We will not go into details regarding the theory on regression analysis and the interpretation of outcomes. Rather, we will focus on how to produce results using Python.

<div class="info">

**NOTE: How to install Numpy and scikit-learn?**
Are you not sure how to install Numpy? Please check out the [tutorial on Modules and Packages](02_01_Modules&Packages.md). If you are working with an Anaconda distribution of Python, NumPy should already be installed.

</div>
<br/>


## 1. Simple Linear Regression with scikit-learn

The sections below will guide you through the process of performing a simple linear regression using ```scikit-learn``` and ```NumPy```. That is, we will only consider one regressor variable (x). The next chapter will discuss Multiple Linear Regression (MLR) with multiple regressor variables.

### 1.1 Import Packages and Classes

First of all, we should start by importing ```NumPy``` and the classes that we need from ```scikit-learn``` at the start of our script.

Note that we can import ```numpy``` as ```np``` to reduce the amount of typing we have to do, and to make the code more readble. Further, to import the ```LinearRegression``` class from ```scikit-learn``` we can use the ```from``` keyword.

```python
import numpy as np
from sklearn.linear_model import LinearRegression
```

### 1.2 Getting the Data Ready

Next, we will need to specify the data that we want to work with. If you are familiar with regression analysis, you will know that two inputs are applicable: 1) the **regressors** (```x```) and 2) the **predictor** (```y```). 

We can capture this data in two variables, both of which are ```NumPy``` arrays (class: ```numpy.ndarray```). 

1. The **predictor** (```y```) should be provided as a one-dimensional array with one row listing the predictor values. This can be done using ```np.array()``` and providing a list of the values as argument.
2. The **regressors** (```x```) should be provided in a two-dimensional array with one colomn and one row per regressor value. As with the predictor, we use ```np.array()```. We then transpose the array using ```.reshape((-1,1))```.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

```

****
### Exercise 1: NumPy Arrays (Optional)
<div class="exercise"><strong>You might not be familiar with NumPy arrays yet. If so, you can have a look at the exercises below.</strong><br/><br/>

* Print ```x``` and ```y``` and evaluate the shape of the arrays.
* How many colomns do each of the arrays have?
* And how many rows?
* What are the dimensions of the arrays?
* Create a one-dimensional NumPy array with the values between 0 and 100 with steps of 5 in between. (Hint: You learned how to do this quickly when you were learning about list operators in [this](01_02_LanguageFeatures.md) tutorial!)
* Transpose the NumPy array you created in the previous exercise. What are the dimensions of the array now?

</div>
<br/>

****

### 1.3 Fitting a Model to the Data

Next, we will create a linear regression model and fit it to the data that we specified in the previous step. We create a model based on the ```LinearRegression()``` class that we imported at the start of our script. This means that ```model``` is an instance of the ```LinearRegression()``` class.

<div class="info">

**NOTE: How to initiate a class?**
Are you a bit shaky when it comes to classes and instances? Please check out the [tutorial on Classes, Objects and Instances](02_03_Objects.md) to refresh your mind.

</div>
<br/>

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

model = LinearRegression()

```

Please check out the page on the ```LinearRegression()``` class on the website of ```scikit-learn``` [here](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html). Here you can find the additional **parameters** that you can specify and their standard values. Also, you will find an overview of the **attributes** of the ```LinearRegression()``` class. Moreover, you can find the **methods** that apply to the class.

****
#### Exercise 2: Parameters and Attributes of ```LinearRegression()```
<div class="exercise">

**Use the page on the ```LinearRegression()``` class (mentioned above) to answer the questions below.**

* Imagine you would like to normalize your x variable. Do you need to change any of the default parameters before initializing ```LinearRegression()```?
* You would like to know how well your model fits the data. How can you find this information? Will you need to refer to an attribute of ```model``` or use a method? Which one?
* What arguments does the method ```predict()``` take? And do you know what you could use this method for?
* What does the method ```score()``` return?

</div>
<br/>

****

Although we have created the instance ```model```, we have not yet fitted the model to our data. We can do this using the ```.fit()``` method. This method takes two argumentes, ```x``` and ```y```. We call ```.fit()``` on ```model``` as shown below. This step is where the optimal weights b<sub>0</sub> and b<sub>1</sub> are determined.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

model = LinearRegression()

model.fit(x, y)

```

### 1.4 Assessing the Results

We can obtain R<sup>2</sup> using the ```.score()``` method. You will need to provide this methods again with ```x``` and ```y``` as arguments.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

model = LinearRegression()

model.fit(x, y)

rSquare = model.score(x, y)
print('The R-Square value:', rSquare)

```

We can assess the values of weights b<sub>0</sub> and b<sub>1</sub> from the attributes ```.intercept_``` and ```.coef_``` respectively.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

model = LinearRegression()

model.fit(x, y)

print('The intercept (b0):', model.intercept_)
print('The slope (b1):', model.coef_)

```

****
#### Exercise 3: Assessing the Results
<div class="exercise">

**The exercises below focus on assessing the results of a simple linear regression.**

* Try to run the last example code. If you entered the same data as in the example above, the R<sup>2</sup> should be about 0.987.
* Change one of the values in the x variable to dramatically worsen the fit. How bad does the fit become?
* Go back to the original data. Is the slope of the regression line positive or negative?
* What is the intercept of the regression line?

</div>
<br/>

****

### 1.5 Predicting

Now that we have fit the model to the data, we can use it to predict  values. We do so using the ```.predict()``` method.

If we pass ```.predict()``` the regressor variable ```x```, we can see what values the model predicts for ```y```. If we compare these values to our actual values, we can get an indication of the quality of our model.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

model = LinearRegression()

model.fit(x, y)

y_Predicted = model.predict(x)
print('Predicted y values:', y_Predicted)

```

Furthermore, we can use our model to predict new y values. To do so, we can create a new regressor array ```x_New``` with values we like to have a prediction for. We then pass ```x_New``` to the ```.predict()``` method.

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])
x = np.array([1, 2, 3, 4, 5, 6]).reshape(-1, 1)

model = LinearRegression()

model.fit(x, y)

x_New = np.array([7, 8, 9, 10]).reshape(-1, 1)
y_Predicted_New = model.predict(x_New)
print('New predicted y values:', y_Predicted_New)

```

****
#### Exercise 4: Forecasting
<div class="exercise">

**The exercises below focus on prediction new values with a simple linear regression model.**

* Replicate the predicted y values from the first exampel above. Do they respond closely to the values in ```y```? Would you expect this given the R<sup>2</sup> value?
* Use the model to predict the value of y when x=100. Try to reason if the outcome is as expected.

</div>
<br/>

****

## 2. Multiple Linear Regression with scikit-learn

Although the process for Multiple Linear Regression (MLR) is similar to Simple Linear Regression, we will discuss some specific considerations below. Specifically, our regressors array (```x```) will now how two colomns. That is, we will consider two regressors to fit our model.

### 2.1 Importing and Getting the Data Ready

As we did with the Simple Linear Regression, we will need to import NumPy and the ```LinearRegression``` class from ```scikit-learn```. 

The specification of the **predictor** (```y```) values is analogous.However, we will now need to specify multiple **regressors**. That is, ```x``` will need to have two colomns (one for each regressor). To do this, we simply make a list of value-pairs. Each pair provides the two regressor values (x1 and x2) for one particular predictor value (y).

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

y = np.array([3, 9, 20, 24, 30, 38])

x = [[1, 10], [2, 15], [3, 20], [4, 25], [5, 30], [6, 35]]
x = np.array(x)
```

### 2.2 Fitting, Results and Forecasting

From this point onwards, the steps correspond closely to those that we took when performing the Simple Linear Regression analysis.

We create our ```model``` and fit the model to the data using ```model = LinearRegression().fit(x, y)```. (Notice how we took two steps with one line of code here. This is possible because ```.fit()``` returns ```self```, which is the model.)

```python
import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])

x = [[1, 10], [2, 15], [3, 20], [4, 25], [5, 30], [6, 35]]
x = np.array(x)

model = LinearRegression().fit(x, y)

# Getting the slope of the regression line.
print('The estimates (b1-b2):', model.coef_)

# Getting the intercept value of the regression line.
print('The intercept (b0):', model.intercept_)

# Predicting the values of y based on the model.
y_Predicted = model.predict(x)
print('Predicted y values:', y_Predicted)

# Specifying a new set of x values to forecast y for.
x_New = [[7, 40], [8, 45], [9, 50], [10, 55], [11, 60], [12, 70]]
x_New = np.array(x_New)
y_Predicted_New = model.predict(x_New)
print('New predicted y values:', y_Predicted_New)

```

****
#### Exercise 5: Multiple Linear Regression
<div class="exercise">

**Run the example code for performing a MLR analysis.**

* Is the intercept of the regression line positive or negative?
* Of what datatype is ```.coef_```? How many elements does it contain? Why is this the case?
* Confirm that for the regressor values x1=15 and x2=100, the value of the predictor (y) is approximately 127.
* Add a third regressor to the analysis with the following values for y=1 till y=6: -19, -13, 0, 10, 14, 20. 
    * Confirm that the intercept changes to about -0.656.
    * Predict the value of y when x1-12, x2=70, and x3=23. Compare the result to the input data. Do you think the prediction you made is reliable?

</div>
<br/>
