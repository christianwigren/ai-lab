"""
================================
Recognizing hand-written digits
================================

This example shows how scikit-learn can be used to recognize images of
hand-written digits, from 0-9.

"""

# Author: Gael Varoquaux <gael dot varoquaux at normalesup dot org>
# License: BSD 3 clause

# Standard scientific Python imports
from asyncore import read
import matplotlib.pyplot as plt
import csv 
import os
import pandas as pd

# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split

###############################################################################
# Digits dataset
# --------------
#
# The digits dataset consists of 8x8
# pixel images of digits. The ``images`` attribute of the dataset stores
# 8x8 arrays of grayscale values for each image. We will use these arrays to
# visualize the first 4 images. The ``target`` attribute of the dataset stores
# the digit each image represents and this is included in the title of the 4
# plots below.
#
# Note: if we were working from image files (e.g., 'png' files), we would load
# them using :func:`matplotlib.pyplot.imread`.

# for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))

current_path = os.path.dirname(os.path.abspath(__file__))

filename=os.path.join(os.getcwd(), 'Data/GS/Ringlista.csv')
data = pd.read_csv(filename, sep=',')

# print(data)

# input("\n\n\npress to continue\n\n\n")

X = []

for i in range(len(data)):
    print(data['Gender'][i], data['Age'][i])

    # X.append([data['Gender'][i], data['Age'][i], data['EmploymentStatus'][i], data['NotificationType'][i], data['Debt'][i]])

print(X)

y = []
class_names = ['Fail','Success']


for i in range(len(X)):
    print(X[i])

input("\n\n\npress to continue\n\n\n")


for i in range(len(X)):
    print(X[i], y[i])

input("\n\n\npress to continue\n\n\n")


for i in range(len(X)):
    print(X[i], class_names[y[i]])


input("\n\n\npress to continue\n\n\n")

balance = [0] * len(class_names)
print(balance)

for i in range(len(y)):
    num = balance[y[i]] + 1
    balance[y[i]] = num


for i in range(len(balance)):
    print(class_names[i], balance[i])



input("\n\n\npress to continue\n\n\n")
