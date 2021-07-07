# Machine-Learning-for-Data-Analytics

Learning algorithm induces function *f* using training data, and *f* will be evaluated on test set. 

**Regression**
* Predict a real value.

**Binary Classification**
* Predict a simple yes/no response.

**Multiclass Classification**
* Put an example into one of a number of classes. (Genre…)

**Ranking**
* Put a set of objects in order of relevance.

## Classification: Decision Tree
* Decision tree is one of the easiest and popular classification algorithms to understand and interpret.
* A decision tree is a flowchart-like tree structure where an internal node represents feature(or attribute), the branch represents a decision rule, and each leaf node represents the outcome.
* Can be utilized for both classification and regression.
* Partitions the tree recursively.
* Handle high dimensional data with good accuracy.

### Algorithm
1. Select the best attribute using Attribute Selection Method (ASM) to split the records.
2. Make that attribute a decision node and breaks the dataset into smaller subsets.
3. Starts tree building by repeating this process recursively for each child until one of the condition will match:
    - All the tuples belong to the same attribute value.
    - There are no more remaining attributes.
    - There are no more instances

### ASM
* Provides a rank to each feature (attribute).
* Best score attribute will be selected as a splitting attribute.
* **Information Gain, Gain Ratio, Gini Index**

#### Information Gain
* The decrease in entropy (impurity in a group of examples).
* Computes the difference between entropy before split and average entropy after split of dataset based on given attribute values.
* The attribute with highest information gain is chosen as the splitting attribute.
* Biased : prefers the attribute with a large number of distinct values.
  - ex) unique identifier (customer_id) has pure partition, thus maximizing information gain and creating useless partitioning.

#### Gain Ratio
* Handles bias by normalizing the information gain.
* The attribute with highest gain ratio is chosen.

#### Gini Index
* Considers a binary split for each attribute.
* In the case of a discrete-valued attribute, the subset that gives the minimum gini index is selected as a splitting attribute.
* In the case of continuous-valued attributes, selects each pair of adjacent value as a possible split-point and point with smaller gini index is chosen as a splitting point.

## Evaluation

**Loss function** : How bad a system’s prediction is in comparison to the truth.

**Cross Validation** : Partitioning dataset into training set and independent set used to evaluate analysis.
* Able to compare the performance of different machine learning models on the same data set.
* Able to select the values for model’s parameters (parameter tuning).
* **K-fold CV**
    - Original dataset is partitioned into k equal size subsamples. (5 or 10 is preferred)
    - Repeated k times, at each time, one of the k subsets is used as test/validation set.
    - Error estimation is averaged overall k trials
    - Reduces bias and variance

### Model evaluation Metrics : Quantify model performance

#### Classification Metrics
* **Classification Accuracy** : Number of correct predictions made as a ratio of all prediction made.
* **Confusion Matrix** : Detailed breakdown of correct and incorrect classifications for each class.
    - Diagonal elements represent the number of points for which the predicted label is equal to the true label, while off-diagonal are mislabeled by the classifier.
    - [[ TP  FP]]
    - [[ FN  TN]]
    - **TPR / Sensitivity / Recall**
        - TP / (TP + FN)
        - Proportion of the positive class got correctly classified.
    - **FNR**
        - FN / (TP + FN)
        - Proportion of the positive class got incorrectly classified.
    - **TNR / Specificity**
        - TN / (TN + FP)
        - Proportion of the negative class got correctly classified.
    - **FPR**
        - FP / (TN + FP) = 1 - *Sensitivity*
        - Proportion of the negative class got incorrectly classified.
    - Higher *TPR* and lower *FNR* is desirable.
    - Higher *TNR* and lower *FPR* is desirable.
* **Logarithmic Loss** : Measures the performance of a classification model where the prediction input is a probability value between 0 and 1.
    - Increases as the predicted probability diverges from actual label.
    - 0 is perfect.
* **Area under Curve (AUC), Receiver Operator Characteristics (ROC)**
    - **AUC**
        - A summary of ROC.
        - Measures ability of a binary classifier to distinguish between classes.
        - Degree of separability.
        - Higher AUC, better performance.
    - **ROC**
        - Evaluation metric for binary classification.
        - Plots TPR against FPR at various threshold values, separates signals from noises.
        - Higher x-axis values, higher FP than TN.
        - Higher y-axis values, higher TP than FN.
        - Choice of threshold depends on the ability to balance between FP and FN.
* **F-Measure**
    - Measure of test’s accuracy that considers both precision and recall of the test to compute score.
        - Precision : Number of correct positive results divided by the total predicted positive observations.
        - Recall : Number of correct positive results divided by the number of all relevant samples (total actual positives).

#### Regression Metrics
* **Mean Absolute Error (MAE)** : Sum of the absolute differences between predictions and actual values
* **Root Mean Squared Error (RMSE)** : Average magnitude of error by taking the square root of the average of squared differences between predictions and actual observation




## References
* A Course in Machine Learning, Hal Daume III, 2017
* https://www.datacamp.com/community/tutorials/decision-tree-classification-python
