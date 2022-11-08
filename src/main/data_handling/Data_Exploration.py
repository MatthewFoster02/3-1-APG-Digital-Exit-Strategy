import pandas
import pandas as pd
import time
import numpy as np
from Visit import Visit
from User import User
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.options.display.width = 0

print("Loading data chunk")
start = time.time()
df = pd.read_csv('C:/Users/01din/Desktop/data APG/data/data_clean/clean_xaa.csv')
end = time.time()
print("Loaded in " + str(end-start) + " seconds.")





start = time.time()
user_ids = df['visitor_id'].unique()
user_ids = user_ids[:2000]

users = []

for user_id in user_ids:
    user = User(df.loc[df['visitor_id'] == str(user_id)])
    users.append(user)

visits = []
visit_length = []
for user in users:
    visit_index_list = user.unique_visits
    for visit_index in visit_index_list:
        visit = Visit(user.user_data.loc[user.user_data['visit_number'] == float(visit_index)])
        visit_length.append(visit.max_visit_number_in_session)
        visits.append(visit)

end = time.time()
print("Loaded in " + str(end-start) + " seconds.")

plt.hist(visit_length, bins=range(int(min(visit_length)), int(max(visit_length)) + 10, 10))
plt.show()
# Outliers more than 1000 page visits
# print(users)
# user = df.loc[df['visitor_id'] == '00000164040540958943749471359763654058']
# print(user)
# visit = Visit(user)
# print(visit.df_page_names)
