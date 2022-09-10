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
import numpy as np


# Import datasets, classifiers and performance metrics
from sklearn import svm, metrics
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report

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
y = []
failed = 0

print(data['HasPaid'][1])

for i in range(len(data)):
    if data['HasPaid'][i] == 0:
        failed = failed + 1
        if failed <= 247:
            X.append([data['Gender'][i], data['Age'][i], data['EmploymentStatus'][i], data['NotificationType'][i], data['Debt'][i]])
            y.append(data['HasPaid'][i])
    else:
        X.append([data['Gender'][i], data['Age'][i], data['EmploymentStatus'][i], data['NotificationType'][i], data['Debt'][i]])
        y.append(data['HasPaid'][i])

print(failed)

# print(X)

class_names = ['Fail','Success']


# for i in range(len(X)):
#     print(y[i])

# input("\n\n\npress to continue\n\n\n")


# for i in range(len(X)):
#     print(X[i], y[i])

# input("\n\n\npress to continue\n\n\n")


balance = [0] * len(class_names)
print(balance)

# for i in range(len(y)):
#     num = balance[y[i]] + 1
#     balance[y[i]] = num


# for i in range(len(balance)):
#     print(class_names[i], balance[i])



input("\n\n\npress to continue\n\n\n")


# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Run classifier, using a model that is too regularized (C too low) to see
# the impact on the results
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
# classifier = XGBClassifier(use_label_encoder=False, eval_metric='logloss').fit(X_train, y_train)

np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
titles_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        X_test,
        y_test,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        normalize=normalize,
    )
    disp.ax_.set_title(title)

    print('\n\n', title)
    print(disp.confusion_matrix)

# plt.show()

predictions = classifier.predict(X_test)

print('\n\n')

print(
    f"Classification report for classifier {type(classifier).__name__}:\n"
    f"{classification_report(y_test, predictions, target_names=class_names)}\n"
)
