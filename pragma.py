#steps
'''
1. importing module
2. create a database
3. connecting to a database
4. create a table in DB - write a query
5. execute the query
'''

#step 1
import sqlite3

#step 2 & 3
"Genzeon_Bootcamp_2023.db"
conn=sqlite3.connect("genzeon_bootcamp_database.db")
print(conn)

'''
Query -> describe table_name - MySQL
Query -> pragma table_info(table_name) - sqlite3
'''


details=conn.execute("pragma table_info('performance')")
print(details)
for i in details:
    print(i)


