import pandas as pd
from os import path

'''
3.0.1 Load the 2018 aggregated pitching data into a DataFrame
'''

DATA_DIR = '/Users/jorgecontreras/Desktop/web-projects/data-projects/data'

dfp = pd.read_csv(
    path.join(DATA_DIR, '2018-season', 'pitches.csv')
)
dfp.head()

'''
3.0.2 Using the dfp DataFrame create another DataFrame dfp50 that is the
top 50 pitchers by lowest ERA
'''
dfp50 = dfp.sort_values('ERA')
dfp50[['nameFirst', 'nameLast', 'ERA']].head(50)

'''
Sort dfp by Name so Zack Greinke appears first.
'''
dfp.sort_values('nameFirst', ascending=False)
dfp.head()

'''
What is the type of dfp.sort_values('W') = DataFrame
'''
type(dfp.sort_values('W'))

'''
3.0.5
a) Make a new DataFrame, dfp_simple, with just the columns nameFirst, nameLast, 'W, L, ERA
'''

dfp_simple = dfp[['nameFirst', 'nameLast', 'W', 'L', 'ERA']]
dfp_simple.head(5)

dfp_simple = dfp_simple[['nameLast', 'nameFirst', 'ERA', 'W', 'L']]
dfp_simple.head(5)

dfp_simple['team'] = dfp['teamID']
dfp_simple.head(5)

dfp.to_csv(
    path.join(DATA_DIR, 'problems', 'fdp_simple.txt'), sep='|'
)
