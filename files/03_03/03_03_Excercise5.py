import numpy as np
from sklearn.linear_model import LinearRegression

y = np.array([3, 9, 20, 24, 30, 38])

x = [[1, 10, -19], [2, 15, -13], [3, 20, 0], [4, 25, 10], [5, 30, 14], [6, 35, 20]]
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
x_New = [[7, 40, -21], [8, 45, -11], [9, 50, 2], [10, 55, 12], [11, 60, 13], [7, 34, 22]]
x_New = np.array(x_New)
y_Predicted_New = model.predict(x_New)
print('New predicted y values:', y_Predicted_New)