########### below only needed if pyw not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#####################################################################
import pyw
import pandas as pd

df = pd.read_csv('https://projects.fivethirtyeight.com/soccer-api/international/2018/wc_matches.csv')

def func(df, key, value):
    dd = {key : value}
    dd['opponent_count'] = [len(df.team2)]

    return pd.DataFrame(dd)

new_df = pyw.p_groupby_apply(func, df, 'team1')
