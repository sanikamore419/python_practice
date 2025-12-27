"""
ml_basics_intro.py

This file contains a basic introduction to Machine Learning.
It explains what machine learning is, its types and a simple example.

Author: Sanika
Branch: AI & Data Science
"""

"""
Machine Learning is a part of Artificial Intelligence.
It allows computers to learn from data and make predictions
without being explicitly programmed.
"""

"""
There are mainly three types of Machine Learning.
Supervised Learning uses labeled data.
Unsupervised Learning works with unlabeled data.
Reinforcement Learning learns using rewards and penalties.
"""

"""
Basic steps involved in Machine Learning:
Collect data
Clean the data
Split data into training and testing
Train the model
Test the model
Improve performance
"""

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([35, 42, 50, 55, 60])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted marks:", y_pred)
print("Actual marks:", y_test)

error = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", error)

"""
Overfitting happens when the model performs well on training data
but gives poor results on new data.

Underfitting happens when the model is too simple
and does not learn properly from data.
"""

"""
Important terms:
Feature: input value
Label: output value
Model: program that learns from data
Training: teaching the model
Testing: checking model performance
"""

"""
Machine Learning is used in many applications such as
spam detection, recommendation systems, medical diagnosis
and face recognition.
"""

"""
End of ml_basics_intro.py
"""
