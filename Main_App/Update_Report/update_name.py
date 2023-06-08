import sqlite3

conn = sqlite3.connect('genzeon_bootcamp_database.db')


def update(id,name_new):
    conn.execute("update Performance set name='"+name_new+" 'where g_id='"+str(id)+"'")
    conn.commit()
    print("Successully updated")