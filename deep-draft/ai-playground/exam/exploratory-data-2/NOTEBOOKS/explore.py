import pandas as pd

nov18f = "data/france/tsv/clickstream-frwiki-2018-11.tsv"
dec18f = "data/france/tsv/clickstream-frwiki-2018-12.tsv"
jan19f = "data/france/tsv/clickstream-frwiki-2019-01.tsv"
feb19f = "data/france/tsv/clickstream-frwiki-2019-02.tsv"
mar19f = "data/france/tsv/clickstream-frwiki-2019-03.tsv"

months = ["Nov '18", "Dec '18", "Jan '19", "Feb '19", "Mar '19"]
paths = [nov18f, dec18f, jan19f, feb19f, mar19f]

def explore_tsv(file):
    df = pd.read_csv(file, sep='\t', header=0)
    df.columns = ['prev', 'curr', 'type', 'n']
    return df

def top_articles(df):
    return df.groupby('curr').sum().sort_values(['n'], ascending=False)
    
def top_from_search(df):
    df_search = df[df['prev'] == 'other-search']
    return df_search.groupby('curr').sum().sort_values(['n'], ascending=False)

