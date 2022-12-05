import pandas as pd
from ast import literal_eval


class ProximalCues:
    def __init__(self):
        generic = lambda x: literal_eval(x)

        conv = {'pc': generic}

        self.urls = pd.read_csv("../data/urls/url-reference_new.csv", converters=conv)

    # Get the proximal cues by page id
    def get_proximal_cues_by_id(self, id):
        return self.urls.loc[self.urls.id == id].pc[0]
