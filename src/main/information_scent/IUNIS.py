from src.main.information_scent.AdjacencyMatrix import AdjacencyMatrix
from src.main.information_scent.TfIdf import TfIdf
from src.main.information_scent.ProximalCues import ProximalCues
import pandas as pd

# I dislike classes in python but I think it makes sense to make these classes.
# I would put the adj matrix in the tfidf but that would just create confusion
tfidf = TfIdf()
adjacency_matrix = AdjacencyMatrix()
proximal_cues = ProximalCues()

# The input to the model should be a list of documents and the order in which they were visited.