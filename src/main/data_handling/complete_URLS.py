import pandas as pd
import time
pd.set_option('display.max_columns', None)
pd.options.display.width = 0
str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
df_list = []
print("Loading data chunk")
start = time.time()

for i in range(1):
    df_list.append(pd.read_csv('C:/Users/01din/Desktop/data APG/data/xa' + str_list[i] + '.csv'))
    for df in df_list:
        df.drop(['user_id', 'dwh_datum_vanaf', 'dwh_datum_tot', 'dwh_datum_aanmaak', 'dwh_datum_partitie', 'dwh_mog',
                 'dwh_scn', 'page_name'], axis=1, inplace=True)
df_urls = pd.read_excel('C:/Users/01din/Desktop/data APG/scrape_results/url-reference.xlsx')
end = time.time()

print("Loaded in " + str(end-start) + " seconds.")


def save_new_urls(url, df_urls):
    if url not in df_urls['urls']:
        df = pd.DataFrame([df_urls.iloc[-1]['id'], url])
        return pd.concat([df_urls, df])

for df in df_list:
    df_urls = df['page_url'].apply(save_new_urls, args=[df_urls])

df_urls.to_csv(r'C:/Users/01din/Desktop/data APG/scrape_results/url-reference_new.xlsx', index=None, header=True)
for i in range(len(df_list)):
    df = df_list[i]
    df.to_csv(r'C:/Users/01din/Desktop/data APG/data/clean_xa' + str_list[i] + '.csv', index=None, header=True)
