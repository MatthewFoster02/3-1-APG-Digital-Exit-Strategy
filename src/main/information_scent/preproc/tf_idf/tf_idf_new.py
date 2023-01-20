import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt
import nltk
from collections import Counter

nltk.download('stopwords')

# Change this variable and the path in the else statement below.
laurence = False
path = None
if laurence:
    path = "C:/Users/laure/OneDrive/Documenten/Project 3.1 APG Files/"
else:
    path = "C:/Users/01din/Desktop/Data APG/scrape_results/"


corpus = pd.read_csv(path + "public_and_private_sentences_none_filtered.csv")

df = pd.DataFrame({'text':corpus.sentences.tolist()})
c = Counter(df.text.str.split().explode())
df = df.text.apply(lambda x: ' '.join(w for w in x.split() if c[w] >= 5).strip())

final_corpus = []
for i in range(len(df)):
    sentence = df.iloc[i]
    final_corpus[corpus.document.iloc[i]-1] = final_corpus[corpus.document.iloc[i]-1] + " " + sentence

vectorizer = TfidfVectorizer(max_df=1.0)
vec_trained = vectorizer.fit_transform(df)

keywords_tf_idf = pd.DataFrame(vectorizer.get_feature_names_out()).values.tolist()
