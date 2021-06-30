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

## References
* A Course in Machine Learning, Hal Daume III, 2017
* https://www.datacamp.com/community/tutorials/decision-tree-classification-python
