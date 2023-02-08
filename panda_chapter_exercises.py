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
3.0.2 Using the dfp DataFrame create another DataFrame dfp50
'''