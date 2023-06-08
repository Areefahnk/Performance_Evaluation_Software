import sqlite3

conn = sqlite3.connect('D:\Bootcamp_Evaluation_Software\genzeon_bootcamp_database.db')


def display():
    records = conn.execute("select * from performance")
    for i in records:
        print(i)
