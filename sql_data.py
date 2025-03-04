import pandas as pd
import sqlite3

#Step2: Uploading CSV to pandas
csv_file_path=r"\Users\sushe\OneDrive\Desktop\NL_SQL\bollywood_movie.csv"
df=pd.read_csv(csv_file_path)
#print(df.head())

#Step1: Uploading CSV to SQLite
#making a connection between sqlite and the csv
conn=sqlite3.connect('bollywood_movie.db')

#Cursor will help in uploading the data to SQLite
cursor=conn.cursor()

# cursor.execute("DROP TABLE IF EXISTS Movies")
# conn.commit()

#Create a new table in SQLite to hold the movie data
cursor.execute('''
CREATE TABLE IF NOT EXISTS Movies (
    Title TEXT,
    Type TEXT,
    Release_Year INTEGER,
    Genre TEXT,
    Director TEXT,
    Production_House TEXT,
    Lead_Actors TEXT,
    Language TEXT,
    Budget_Millions REAL,
    Box_Office_Millions REAL,
    OTT_Platform TEXT,
    Runtime_Minutes INTEGER,
    No_of_Episodes INTEGER,
    IMDb_Rating REAL,
    Audience_Score INTEGER,
    Critics_Score INTEGER,
    Awards_Nominations INTEGER,
    Awards_Won INTEGER,
    Social_Media_Mentions INTEGER,
    User_Reviews_Count INTEGER,
    Viewership_Hours_Million REAL
)
''')
#to move data from python to sqlite
df.to_sql('Movies',conn,if_exists='replace',index=False)
#movies=name of the db | if_ex=if movies db is there, replace it. index=fales=> use the index given by me.
conn.commit()