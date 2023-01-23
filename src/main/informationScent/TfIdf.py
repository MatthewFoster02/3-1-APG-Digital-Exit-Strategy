import pandas as pd


class TfIdf:
    def __init__(self):
        # Loading in the tf-idf
        # Rows are documents, the first column is the document id
        # Columns are keywords, the first row is the keyword id
        self.tfidf = pd.read_csv("../data/tf_idf/tf_idf.csv")

        # Loading in the keywords
        # Two columns, column 1 is id, column 2 is keyword
        # We can access the weight in the tf-idf by first accessing the id number from the keyword file
        self.tfidf_keywords = pd.read_csv("../data/tf_idf/tf_idf_keywords.csv")
        self.tfidf_keywords.columns = ["id", "keyword"]

    def get_id_by_keyword(self, keyword):
        return self.tfidf_keywords.id.iloc[self.tfidf_keywords[self.tfidf_keywords.keyword == keyword].index].values[0]

    # Method to get the tfidf value of a keyword in a page
    def get_tf_idf_value(self, page_id, keyword):
        keyword_id = self.get_id_by_keyword(keyword)
        return self.tfidf.iloc[page_id, keyword_id + 1]
