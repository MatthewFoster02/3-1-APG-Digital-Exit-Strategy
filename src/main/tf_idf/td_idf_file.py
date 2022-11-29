import string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt
import nltk
nltk.download('stopwords')

#Change paths
private_scrape = pd.read_excel("C:/Users/laure/OneDrive/Documenten/Project 3.1 APG Files/private_scrape_results.xlsx")
public_scrape = pd.read_excel("C:/Users/laure/OneDrive/Documenten/Project 3.1 APG Files/public_scrape_results.xlsx")

from nltk.corpus import stopwords

# Storing all of the records of 'public_scrape' in English in a separate dataframe. 'private_scrape' does not contain any records in
# English so this is not needed there.
public_scrape_english = public_scrape.loc[public_scrape['full_url'].str.contains("english", case=False)]

# Storing all of the records of 'public_scrape' in Dutch in a separate dataframe.
public_scrape_dutch = public_scrape.loc[~public_scrape['full_url'].str.contains("english", case=False)]

# Obtaining the paragraphs of these scrape results and converting them to lists, making them easier to iterare over.
private_corpus = private_scrape.paragraph.tolist()
public_corpus = public_scrape_dutch.paragraph.tolist()
public_corpus_english = public_scrape_english.paragraph.tolist()

# Adding the 'private_corpus' and 'public_corpus' as they are both in Dutch.
corpus_dutch = private_corpus + public_corpus
corpus_english = public_corpus_english

# Defining which words in Dutch we want to remove before starting computing the tf-idf matrix.
dutch_stopwords = stopwords.words('dutch')
dutch_months = ['Januari', "Februari", "Maart", "April", "Mei", "Juni", "Juli", "Augustus", "September", "Oktober", "November", "December", 'januari', "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
words_to_remove_dutch = dutch_stopwords + dutch_months

# Defining which words in English we want to remove before starting computing the tf-idf matrix.
english_stopwords = stopwords.words('english')
english_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
words_to_remove_english = english_stopwords + english_months


# This function reduces the number of words in the passed on 'corpus' by removing the words in the 'words_to_remove',
# replacing words on which emphasis is placed, stemming, and removing some unexpected characters.
def clean_documents(corpus, words_to_remove, dutch):
    for i in range(len(corpus)):
        # In order to work with the corpus, we first need to convert it to a string.
        document = str(corpus[i])

        # Replacing characters on which emphasis was placed. This helps avoiding the word 'maar' to appear both as
        # 'maar' and as 'máár' in the final cleaned corpus.
        document = document.replace("á", "a").replace("é", "e").replace("è", "e").replace("ó", "o").replace("ò",
                                                                                                            "o").replace(
            "í", "i")

        # Splitting our 'document' into a list of words, meaning we can now look at each word individually and
        # initializing a new variable 'clean_document' to which we can store all the words we want to retain.
        words = document.split()
        cleaned_document = []

        # First, we start by removing every word in the list that appears in the 'words_to_remove' list and each word
        # that either contains or entirely consists of some unexpected characters (such as 'xD' here which is inserted
        # by Python when a tab is read from the original scrape results. This removal is done by simply not adding them
        # to the 'cleaned_document' variable.
        for word in words:
            word = word.lower()
            if word[-2:] == "xD":
                word = word[:-2]
            cleaned_document.append(word)

        # Now we can join all these words into a list and remove punctuation, numbers and double spaces.
        cleaned_document = " ".join(cleaned_document)
        cleaned_document = cleaned_document.translate(str.maketrans("", "", (string.punctuation + "’")))
        cleaned_document = "".join([i for i in cleaned_document if not i.isdigit()])
        while "  " in cleaned_document:
            cleaned_document = cleaned_document.replace("  ", " ")

        # Splitting our 'cleaned_document' into a list of words, meaning we can now look at each word individually and
        # initializing a new variable 'stemmed_document' to which we can store all the words we want to retain.
        words = cleaned_document.split()
        stemmed_document = []

        # First, we check whether the current word does not appear in the 'words_to_remove' list and then we check whether we
        # can stem it.
        for word in words:
            if word not in words_to_remove:
                if dutch:
                    if "ing" in word and word.replace('ing', '') in words:
                        stemmed_document.append(word.replace('ing', ''))
                    elif "s" in word and word.replace('s', '') in words:
                        stemmed_document.append(word.replace('s', ''))
                    elif "ig" in word and word.replace('ig', '') in words:
                        stemmed_document.append(word.replace('ig', ''))
                    elif "isme" in word and word.replace('isme', '') in words:
                        stemmed_document.append(word.replace('isme', ''))
                    elif "lijk" in word and word.replace('lijk', '') in words:
                        stemmed_document.append(word.replace('lijk', ''))
                    else:
                        stemmed_document.append(word)
                elif not dutch:
                    if "s" in word and word.replace('s', '') in words:
                        stemmed_document.append(word.replace('s', ''))
                    elif "ism" in word and word.replace('ism', '') in words:
                        stemmed_document.append(word.replace('ism', ''))
                    elif "ed" in word and word.replace('ed', '') in words:
                        stemmed_document.append(word.replace('ed', ''))
                    elif "al" in word and word.replace('al', '') in words:
                        stemmed_document.append(word.replace('al', ''))
                    elif "ist" in word and word.replace('ist', '') in words:
                        stemmed_document.append(word.replace('ist', ''))
                    elif "ity" in word and word.replace('ity', '') in words:
                        stemmed_document.append(word.replace('ity', ''))
                    elif "ness" in word and word.replace('ness', '') in words:
                        stemmed_document.append(word.replace('ness', ''))
                    else:
                        stemmed_document.append(word)

        stemmed_document = " ".join(stemmed_document)
        corpus[i] = stemmed_document
    return corpus


# Cleaning the records in Dutch and the ones in English and later combining them to create a single corpus.
clean_corpus_dutch = clean_documents(corpus_dutch, words_to_remove_dutch, True)
clean_corpus_english = clean_documents(corpus_english, words_to_remove_english, False)
clean_corpus = clean_corpus_dutch + clean_corpus_english
print(clean_corpus)