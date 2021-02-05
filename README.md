# Student Behavior Analysis with Machine Learning, Deep Learing Techniques
This is my lab project on Students Behavior Analysis which had 5 lab tasks to do. Which are:

Association Rule Mining: 
This is a rule-based machine learning method to find the relationships between different itemsets in databases. 
Decision Tree:
Tree-based machine learning method to predict something using some historical data.

Kmeans Clustering:
An unsupervised machine learning method to find groups with same characteristics in the data and with the K number of groups.

Regression Analysis:
A set of machine learning methods to predict a continous dependent variable based on one or multiple independent variables using some mathematical equations.

Artificial Neural Network:
A deep learning method which works like human brain to predict a dependent variable based on some independent variables using some mathematical equations with an input layer, one or more hidden layers and an output layer.


# Note: My dataset consists of 920 instances with 20 features. The dataset is my personal dataset. So It is not sharable in public. Just showing the process. In addition, you can also open the codes in colab by clicking the link "open in colab". 


# 1. Association Rules
I have used Apriori algorithm to generate the association rules among the frequent itemsets. There are two sections: Implementation and Deep Analysis. In implementation section, I generated the association rules of all the itemsets. And in Deep Analysis section, I analyzed the unique element or item of each features which have more than one unique element or item and found the association rules with my feelings level (Very Good, Good, Normal, Bad, Very Bad) for each single item. 


# 2. Decision Tree
I have used decision tree classifier with both default crition (gini) and non-default criterion (entropy), respectively. In addition, I have also tuned hyperparameter with both grid search cv and randomized search cv, respectively to get the best parameters.


# 3. Kmeans Clustering
To find the different groups of item with same characteristics, I have used Kmeans clustering by analyzing and visualizing the same technique in many ways. Finally, I have created two models with 9 clusters and 8 clusters, respectively. 


# 4. Regression Analysis
I have used 7 types of regression models to predict my depression or happiness over some features. I used information gain method for feature selection. The 7 models gave me different train and accuracy and I have selected the best models for my problem. 

Note that: The summary to find the best models has been added in the last cell of .ipynb file.


# 5. Artificial Neural Network (ANN)
This neural network model predicts my depression or happiness(Very Good, Good, Normal, Bad, Very Bad) over some features. My model gives 94% training accuracy and 91% test accuracy with one hidden layer which have 11 neurons. 

Note that: To see the tensorboard, open .ipynb file in colab. 


