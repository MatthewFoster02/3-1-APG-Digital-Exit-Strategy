# 3-1-APG-Digital-Exit-Strategy:
This project was prepared in cooperation with APG as project 3-1 of the
Bachelor of Data Science and Artificial Intelligence, Maastricht University.

There are multiple notebook files in this directory, for cleaning, processing the data, 
and then also for the IUNIS model. The data is not part of this GitHub due to its size.


Predicting when a customer will drop from ABP's website without finding their information need, 
therefore alerting the website that the customer needs human intervention.



### 1) Information Need Model:

* **TF-IDF Model:** Convert doc into keywords with weight (based on the most relevant keywords). 
* **TF-IDF + time:** Time can also be included in the
model by adjusting the TF-IDF weight based on how much time users in the dataset spend on these pages. (Poor performance, different implementation could likely still offer better results)
* **Predict IN** (information Need): On a subset of a complete path, compute the information need for that subset. This information need is a prediction for the users information need over the whole visit.
* Variables such as Decay Factor, the inclusion of time, and prediction page have been experimented with. Results can be found in the report.

### 2) Word2vec:
* **Word2vec** is a neural network-based language model that is trained to predict the likelihood of a word appearing in
a certain context. It achieves this by using words that surround that
word within a sentence and then outputs a vector representation of
that word.
* For this use case, the set of keywords in the TF-IDF must be a subset of the set of keywords in the Word2vec. 
* A pre-trained Word2vec model does not work, as there are words in the TF-IDF which are not in the pre-trained Word2vec model.
* A self-trained Word2vec model was used, which was trained on the same set of documents as the TF-IDF.
* The 10 highest weighted keywords in a visit are passed to Word2vec. These words' vectors are computed and averaged out, and the word with the most similar vector to said vector is used to label the visit.
* 


### 3) Clustering
* **DB-Scan**: Complete visits can be transformed into meaning, and thus into a Word2vec vector. These visits are then clustered using DBScan, such that visits with similar meaning are close to each other.
* The idea is that, when a new visitor comes, we can predict their information need, and attempt to place it into a cluster.
* Then, we can compare the path the user is taking, to paths that other users with similar information need have taken.

### 4) Evaluation: 
The evaluations of predicted IN takes place under the following assumptions:
* The Goal page occurs late in the visit path
* The user usually spends much time on the goal page.
* With these assumptions, the similarity between the keywords on the goal page and the keywords of the predicted information need is computed.
* No formal evaluations of the 

### 4) Measuring User Stray: 
* **Markov Chain**:Mathematical system that experiences transitions from one state to another according to certain probabilistic rules. 
* For each cluster created, thus, for each group of similar visits, a Markov Chain is created. For all visits in the cluster, the transition probabilities are computed: the probabilities that from each page, you go to each other page.
* In each state, the probability to reach a final state can be calculated. When this probability gets too low, a Digital Exit Strategy can be called.
* 
* Cluster Analysis with **PCA**:PCA used for data reduction without losing its properties. Reducing dimensions of the DB-Scan clusters by selecting
the most important features that capture maximum information about the dataset helps to calculate visit distance to each cluster.  