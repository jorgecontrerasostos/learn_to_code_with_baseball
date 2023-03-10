import pandas as pd
from os import path

DATA_DIR = '/Users/jorgecontreras/Desktop/web-projects/data-projects/data'

# Reading csv file joining the folder path with the actual csv.
players = pd.read_csv(
    path.join(DATA_DIR, '2018-season', 'players.csv')
)

# Returns the first n rows.
players.head(10)

players.columns

# Returns dimension rxt of the data
players.shape

players['name'].head()

# A sigle column is a Serie not a Data Frame
type(players['name'])

# Changing a the data type from Series to DataFrame
players['name'].to_frame().head()
type(players['name'].to_frame())

# Referencing multiple columns. Note that this is a DataFrame
players[['name', 'height', 'weight','debut']].head()

'''
Indexing
The first row of the DataFrame is the index, which always starts at
0. They do not have to be numbers, can be strings or dates.
'''
# Making the column 'playerID' the id of our DataFrame
players.set_index('playerID').head()

# Make our specified ID to be always the ID of the Dataframe
players.set_index('playerID', inplace=True)
players.head()

# Reset original index
players.reset_index().head()

# Creates a subset of the original DataFrame
players_cuba = players.loc[
    players['birthCountry'] == 'Cuba',
    ['name', 'height', 'weight', 'birthCountry']
]
players_cuba.head()

# Sort players by weight
players_cuba.sort_values('weight', inplace=True)
players_cuba.head()

# Add new column to our subset of cuban players
players_cuba['bats'] = players['bats']
print(players_cuba.head())

'''
Outputing data with to_csv() method
'''

players_cuba.to_csv(
    path.join(DATA_DIR,' 2018-season', 'players_cuba.csv')
)
players_cuba.to_csv(
    path.join(DATA_DIR,' 2018-season', 'players_cuba.csv'),
    index=False
)

# Creating new columns

DATA_DIR = '/Users/jorgecontreras/desktop/web-projects/data-projects/data'

# load data
pp = pd.read_csv(path.join(DATA_DIR, '100-game-sample', 'pitches.csv'))

pp['mph_max'] = 104.3
pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'pitch_type', 'mph', 'mph_max']].head()

pp['mph_max'] = 105.1
pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'pitch_type', 'mph', 'mph_max']].head()

# Math and number columns
pp['sz_height'] = pp['sz_top'] - pp['sz_bot']
pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'sz_top', 'sz_bot', 'sz_height']].head()

# Using the sample() method we can print data frame columns randomly

pp['season'] = 2018
pp[['pitcher', 'batter', 'i', 'o', 'b', 's', 'pitch_type', 'mph', 'season']].sample(5)