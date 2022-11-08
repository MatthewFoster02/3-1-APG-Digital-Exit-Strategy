import pandas as pd
import time
pd.set_option('display.max_columns', None)
pd.options.display.width = 0
str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
df_list = []
print("Loading data chunk")
start = time.time()

for i in range(18):
    df_list.append(pd.read_csv('C:/Users/01din/Desktop/data APG/data/xa' + str_list[i] + '.csv'))

df_urls = pd.read_excel('C:/Users/01din/Desktop/data APG/scrape_results/url-reference.xlsx')
end = time.time()
print("Loaded in " + str(end-start) + " seconds.")

for df in df_list:
    df.drop(['user_id', 'dwh_datum_vanaf', 'dwh_datum_tot', 'dwh_datum_aanmaak', 'dwh_datum_partitie', 'dwh_mog', 'dwh_scn', 'page_name'], axis=1, inplace=True)

for i in range(len(df_urls)):
    url = df_urls.iloc[i]['urls']
    print(i)
    id = i+1
    for df in df_list:
        df.loc[df['page_url'] == url, 'page_url'] = id


str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(len(df_list)):
    df = df_list[i]
    df.to_csv(r'C:/Users/01din/Desktop/data APG/data/clean_xa' + str_list[i] + '.csv', index=None, header=True)
