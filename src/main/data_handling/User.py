class User:

    def __init__(self, user_data):
        self.landed_in_mijnomgeving = user_data.iloc[0]['landed_in_mijnomgeving']
        self.visitor_id = user_data.iloc[0]['visitor_id']
        self.df_page_names = user_data['page_name']
        self.df_page_url = user_data['page_url']
        self.unique_visits = user_data['visit_number'].unique()
        self.user_data = user_data
