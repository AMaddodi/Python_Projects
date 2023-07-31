import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

iris = pd.read_csv("iris.csv")

sns.scatterplot(x='Sepal.Length', 
                y='Petal.Length', 
                data= iris, 
                hue = 'Species')

plt.show()

y = iris[['Sepal.Length']]
x = iris[['Sepal.Width']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

lr = LinearRegression()

lr.fit(x_train, y_train)

y_predict = lr.predict(x_test)

mean_squared_error(y_test, y_predict)

# Multi Linear Regression
y = iris[['Sepal.Length']]
x = iris[['Sepal.Width', 'Petal.Length', 'Petal.Width']]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

mlr = LinearRegression()

mlr.fit(x_train, y_train)
y_predict = mlr.predict(x_test)

mean_squared_error(y_test, y_predict)
