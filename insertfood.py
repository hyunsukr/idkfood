import sqlite3
import sys

conn = sqlite3.connect('allFoods.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Food (name text PRIMARY KEY NOT NULL, type TEXT  NOT NULL, flavor text NOT NULL, country text not null, time int NOT NULL, link text not null)''')
index = 0
c.execute('''SELECT * FROM ALLFOOD''')
for row in c:
    index = index + 1

#Section for the Everyday items
NULL= "NULL"
c.execute('''SELECT * FROM ALLFOOD WHERE name = "Hamburger" AND calories = 354''')
counter = 0
for row in c:
  counter = counter + 1
if counter == 0:
  index = index + 1
  c.execute('''INSERT OR IGNORE INTO ALLFOOD(id, name, calories, ingredients, price, image, date) VALUES (?,?,?,?,?,?,?)''',(index, "Hamburger", 354, "meat, bun", 2.20, "hamburger.jpg", NULL))

conn.commit()


#c.execute('''SELECT * FROM ALLFOOD WHERE date = "2018-07-16"''')
c.execute('''SELECT * FROM ALLFOOD''')
for row in c:
  print(row)
  print('****')
conn.close()

