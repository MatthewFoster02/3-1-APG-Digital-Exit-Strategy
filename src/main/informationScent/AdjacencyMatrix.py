import pandas as pd


class AdjacencyMatrix:
    def __init__(self):
        # Loading in the adjacency matrix
        # First column and row are data immediately, so access directly by page id
        # If row(page_id_1) leads to column(page_id_2) = 1 else = 0
        self.adjacency_matrix = pd.read_csv("../data/matrices/adjacency_matrix.csv", header=None)

    # Method to get the adjacency value from two page ids
    def get_adjacency_value(self, page_id_1, page_id_2):
        return self.adjacency_matrix.iloc[page_id_1, page_id_2] == 1