import sqlite3
import pandas as pd


conn = sqlite3.connect('my_dabase.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS my_dataset''')
c.execute('''CREATE TABLE my_dataset (show_id String, type String, title String, director String, cast String, country String,
date_added String, release_year Integer, rating String, duration String, listed_in String, description String)''')

#Load our file
my_dataset = pd.read_csv('netflix_titles.csv')

# write the data to a sqlite table
my_dataset.to_sql('my_dataset', conn, if_exists='append', index = False)

#print(c.execute('''SELECT * FROM my_dataset LIMIT 10''').fetchall())

#L'API va devoir prendre en argument un texte qui va etre lu et executer (le texte sera notre requête)

#On va pouvoir Lire, Creer, Updater et supprimer un utilisateur