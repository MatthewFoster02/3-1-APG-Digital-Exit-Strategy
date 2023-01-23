# 3-1-APG-Digital-Exit-Strategy:
This project was prepared in cooperation with APG as project 3-1 of the
Bachelor of Data Science and Artificial Intelligence, Maastricht University.

There are multiple notebook files in this directory, for cleaning, processing the data, 
and then also for the IUNIS model. The data is not part of this GitHub due to its size.

## Information Need Model
Predicting when a customer will drop from ABP's website without finding their information need, 
therefore alerting the website that the customer needs human intervention.



### 1) TF-IDF Model:

* **TF-IDF Model:** Convert doc into keywords with weight (based on the most relevant keywords). 
* **TF_IDF + time:** Time can also be included in the
model by adjusting the TF-IDF weight Pages on which users usually.
spend more time, might be more relevant).
* **Predict IN** (information Need): When a user visit's length past 3 , Implement a vector of keywords(word2vector).

Estimate the probability of the visit  whether the path is straying from its optimal path or not.
* **Markov Chain**:Mathematical system that experiences transitions from one state to another according to certain probabilistic rules. 
* Cluster Analysis with **PCA**:PCA used for data reduction without losing its properties. Reducing dimensions of the DB-Scan clusters by selecting
the most important features that capture maximum information about the dataset helps to calculate visit distance to each cluster.  


### 2) Information scent model:
* **Word2vec** is a neural network-based language model that is trained to predict the likelihood of a word appearing in
a certain context. It achieves this by using words that surround that
word within a sentence and then outputs a vector representation of
that word


### 3) Clustering
* **DB-Scan**:Cluster complete visits such that similar visits are in one cluster

### 4) Evaluation: 
The evaluations of predicted IN takes place under the following assumptions:
* The Goal page occurs late in the visit path
* How much a user spend time in goal page

