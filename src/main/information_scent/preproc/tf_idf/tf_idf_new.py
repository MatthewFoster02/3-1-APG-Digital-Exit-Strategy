import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt
from collections import Counter

# Change this variable and the path in the else statement below.
laurence = False
path = None
if laurence:
    path = "C:/Users/laure/OneDrive/Documenten/Project 3.1 APG Files/"
else:
    path = "C:/Users/01din/Desktop/Data APG/scrape_results/"


corpus = pd.read_csv(path + "final.csv")
# "public_and_private_paragraphs_none_filtered.csv"
df = pd.DataFrame({'text':corpus.paragraphs.tolist()})
c = Counter(df.text.str.split().explode())
df = df.text.apply(lambda x: ' '.join(w for w in x.split() if c[w] >= 5).strip())


vectorizer = TfidfVectorizer(max_df=1.0)
vec_trained = vectorizer.fit_transform(df)


pd.DataFrame(vec_trained.todense()).to_csv('C:/Users/01din/Desktop/data APG/tfidf/tf_idf_new.csv')
pd.DataFrame(vectorizer.get_feature_names_out()).to_csv('C:/Users/01din/Desktop/data APG/tfidf/tf_idf_keywords_new.csv')

print(len(vectorizer.get_feature_names_out()))
