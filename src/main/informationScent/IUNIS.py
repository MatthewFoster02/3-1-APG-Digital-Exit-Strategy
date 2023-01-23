import pandas as pd
from ast import literal_eval

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

#%%
class AdjacencyMatrix:
    def __init__(self):
        # Loading in the adjacency matrix
        # First column and row are data immediately, so access directly by page id
        # If row(page_id_1) leads to column(page_id_2) = 1 else = 0
        self.adjacency_matrix = pd.read_csv("../data/matrices/adjacency_matrix.csv", header=None)

    # Method to get the adjacency value from two page ids
    def get_adjacency_value(self, page_id_1, page_id_2):
        return self.adjacency_matrix.iloc[page_id_1, page_id_2] == 1

tfidf = TfIdf()
adjacency_matrix = AdjacencyMatrix()

generic = lambda x: literal_eval(x)

conv = {'url_id_path': generic,
        'seconds_spent_path': generic}
df = pd.read_csv('../data/clickdata/testGrouped.csv', converters=conv)

paths = df.url_id_path
path = paths[0]

print(path)