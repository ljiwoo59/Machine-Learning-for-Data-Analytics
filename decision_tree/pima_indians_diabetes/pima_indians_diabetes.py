import pandas as pd
from sklearn.tree import DecisionTreeClassifier # import Decision Tree Classifier
from sklearn.model_selection import train_test_split # import train_test_split function
from sklearn import metrics # import metrics module for accuracy calculation
# visualizing tree
from sklearn import tree
import graphviz

# import dataset
col_names = ["pregnant", "glucose", "bp", "skin", "insulin", "bmi", "pedigree", "age", "label"]
df = pd.read_csv("diabetes.csv", header=0, names=col_names)

# split dataset in feature and target variable
feature_cols = col_names[:-1]
X = df[feature_cols] # features
y = df.label # target variable

# 70% training, 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# create Decision Tree classifier object
clf = DecisionTreeClassifier() #default: gini
# train Decision Tree classifier
clf = clf.fit(X_train, y_train)
# predict the outcome for test dataset
y_pred = clf.predict(X_test)

# Decision Tree classifier using Information Gain
clf2 = DecisionTreeClassifier(criterion="entropy", max_depth=4)
clf2 = clf2.fit(X_train, y_train)
y_pred2 = clf2.predict(X_test)

# evaluation
print("Accuracy for gini index: ", metrics.accuracy_score(y_test, y_pred))
print("Classification report: ", metrics.classification_report(y_test, y_pred))
print("Confusion matrix: ", metrics.confusion_matrix(y_test, y_pred))
print("Log loss: ", metrics.log_loss(y_test, y_pred))

print("Accuracy for information gain with max depth 4: ", metrics.accuracy_score(y_test, y_pred2))
print("Classification report: ", metrics.classification_report(y_test, y_pred2))
print("Confusion matrix: ", metrics.confusion_matrix(y_test, y_pred2))
print("Log loss: ", metrics.log_loss(y_test, y_pred2))

# visualizing tree
dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=feature_cols,
                                class_names=['0', '1'],
                                filled=True)
graph = graphviz.Source(dot_data, format="png")
graph.render("pima_indians_diabetes_clf")

dot_data2 = tree.export_graphviz(clf2, out_file=None,
                                feature_names=feature_cols,
                                class_names=['0', '1'],
                                filled=True)
graph2 = graphviz.Source(dot_data2, format="png")
graph2.render("pima_indians_diabetes_clf2")