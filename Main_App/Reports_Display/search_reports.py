import sqlite3

conn = sqlite3.connect('genzeon_bootcamp_database.db')


def search(id):
    print(id)
    record = conn.execute("select *from performance where G_id='" +str(id)+ "'")
    #c.execute("select quantity from addb where bookname='" + title + "'")

    for i in record:
        print(i)

