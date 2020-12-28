import numpy as np
import pandas as pd
import warnings
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score

df_X_pca = pd.read_csv('df_X_pca.csv').drop('Unnamed: 0', axis = 1)
y = pd.read_csv('y.csv').drop('track_id', axis = 1)

model = LogisticRegression(random_state = 1)
train_X, val_X, train_y, val_y = train_test_split(df_X_pca,y,random_state = 1)
model.fit(train_X, train_y)
predicted_val = model.predict(val_X)
mean_absolute_error(val_y, predicted_val)
print(accuracy_score(val_y, predicted_val))
