# Machine-Learning-for-Data-Analytics

Learning algorithm induces function *f* using training data, and *f* will be evaluated on test set.

## Supervised Learning Model
The algorithm learns on a labeled dataset and evaluates its accuracy on training data.

**Regression**
* Predict a real value.

**Binary Classification**
* Predict a simple yes/no response.

**Multiclass Classification**
* Put an example into one of a number of classes. (Genre...)

**Ranking**
* Put a set of objects in order of relevance.

---

## Unsupervised Learning Model
The training dataset is a collection of examples without a specific desired outcome or correct answer.  
The algorithm discovers hidden patterns or data groupings.

**Clustering**
* Group unlabeled data based on their similarities or differences.

**Association Rules**
* Find relationships between variables in given dataset. (Market basket analysis...)

**Dimensionality Reduction**
* Reduce the number of data inputs to a manageable size while also preserving the integrity of the dataset as much as possible.

---

## Semi-Supervised Learning Model
The training dataset is both labeled and unlabeled data.

---

## Regression: Linear Regression

## Regression: Gradient Descent

## Classification: K-Nearest Neighbors

## [Classification: Decision Tree](https://github.com/ljiwoo59/DT)

## Classification: Naive Bayesian

## Classification: Logistic Regression and Perceptron

## Classification: Support Vector Machines

## Classification: Ensemble Learning

## Clustering: K-means Clustering

## Clustering: Hierarchical Clustering

## Clustering: Density-based Clustering

## Dimensionality Reduction

## Deep Learning: Backpropagation

## Deep Learning: CNN and RNN

## Deep Learning: Representation Learning

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
