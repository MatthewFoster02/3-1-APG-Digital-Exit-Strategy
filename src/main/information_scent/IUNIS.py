import pandas as pd

# Loading in the tf-idf
# Rows are documents, the first column is the document id
# Columns are keywords, the first row is the keyword id
tfidf = pd.read_csv("../data/tf_idf/tf_idf.csv")


# Loading in the keywords
# Two columns, column 1 is id, column 2 is keyword
# We can access the weight in the tf-idf by first accessing the id number from the keyword file
tfidf_keywords = pd.read_csv("../data/tf_idf/tf_idf_keywords.csv")
tfidf_keywords.columns = ["id", "keyword"]

# Loading in the adjacency matrix
# First column and row are data immediately, so access directly by page id
# If row(page_id_1) leads to column(page_id_2) = 1 else = 0
adjacency_matrix = pd.read_csv("../data/matrices/adjacency_matrix.csv", header = None)


def get_id_by_keyword(keyword):
    return tfidf_keywords.id.iloc[tfidf_keywords[tfidf_keywords.keyword == keyword].index].values[0]


# Method to get the tfidf value of a keyword in a page
def get_tf_idf_value(page_id, keyword):
    keyword_id = get_id_by_keyword(keyword)
    return tfidf.iloc[page_id,keyword_id+1]


# Method to get the adjacency value from two page ids
def get_adjacency_value(page_id_1, page_id_2):
    return adjacency_matrix.iloc[page_id_1,page_id_2]==1


print(get_adjacency_value(7,3))