"""
================
Confusion matrix
================

Example of confusion matrix usage to evaluate the quality
of the output of a classifier on the iris data set. The
diagonal elements represent the number of points for which
the predicted label is equal to the true label, while
off-diagonal elements are those that are mislabeled by the
classifier. The higher the diagonal values of the confusion
matrix the better, indicating many correct predictions.

The figures show the confusion matrix with and without
normalization by class support size (number of elements
in each class). This kind of normalization can be
interesting in case of class imbalance to have a more
visual interpretation of which class is being misclassified.

Here the results are not as good as they could be as our
choice for the regularization parameter C was not the best.
In real life applications this parameter is usually chosen
using :ref:`grid_search`.

"""

import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from xgboost import XGBClassifier
from sklearn.metrics import classification_report


# import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names


for i in range(len(X)):
    print(X[i])

input("\n\n\npress to continue\n\n\n")


for i in range(len(X)):
    print(X[i], y[i])

input("\n\n\npress to continue\n\n\n")


for i in range(len(X)):
    print(X[i], iris.target_names[y[i]])


input("\n\n\npress to continue\n\n\n")

balance = [0] * len(iris.target_names)
print(balance)

for i in range(len(y)):
    num = balance[y[i]] + 1
    balance[y[i]] = num


for i in range(len(balance)):
    print(iris.target_names[i], balance[i])



input("\n\n\npress to continue\n\n\n")

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Run classifier, using a model that is too regularized (C too low) to see
# the impact on the results
# classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
classifier = XGBClassifier(use_label_encoder=False, eval_metric='logloss').fit(X_train, y_train)

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
    f"{classification_report(y_test, predictions, target_names=iris.target_names)}\n"
)