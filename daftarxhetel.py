import sqlite3
import csv

daf = []

n = input("Enter the name: ")
s = int(input("Enter the number: "))
with open ("daftarche.csv" , "a") as file:
    writer = csv.DictWriter(file, fieldnames = ['name' , 'number'])
    writer.writerow({'name' : n,'number' : s})
to = (n , s)
daf.append({n:s})
tel = sqlite3.connect('daftarche.db')
cursor = tel.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, number INTEGER);")
cursor.execute("INSERT INTO users (name , number) VALUES (?,?);",to)
tel.commit()
tel.close()
print(daf)

f = input("search: ")
if f in daf[0]:
    print(daf[0][f])
ftop = (f,)
tel = sqlite3.connect('daftarche.db')
cursor = tel.cursor()
cursor.execute("SELECT number FROM users WHERE name = ?;", ftop)
rows = cursor.fetchall()
for row in rows:
    print(row)
tel.close()
