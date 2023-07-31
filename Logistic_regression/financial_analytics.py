import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
color = sns.color_palette()
import sklearn.metrics as metrics
import warnings
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
warnings.filterwarnings('ignore')

default = pd.read_csv('default.csv')

print(default.shape)
print(default.describe())
plt.figure(figsize = (15,5))
plt.subplot(1,2,1)
sns.boxplot(y = default['balance'])

plt.subplot(1,2,2)
sns.boxplot(y = default['income'])
plt.show()

default = pd.get_dummies(default, drop_first = True)
default.columns = ['balance', 'income', 'default', 'student']

x = default.drop('default', axis =1)
y = default['default']

x_train, x_test, y_train, y_test = train_test_split(x,y,
                                                   test_size=0.3,
                                                   random_state = 21,
                                                   stratify = y)

sm = SMOTE(random_state=33, sampling_strategy = 0.75)
x_res, y_res = sm.fit_sample(x_train, y_train)

lr = LogisticRegression()
lr.fit(x_res, y_res)
y_pred = lr.predict(x_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_true, y_pred))
