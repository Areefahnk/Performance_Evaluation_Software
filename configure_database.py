import sqlite3

con = sqlite3.connect('genzeon_bootcamp_database.db')
con.execute('''create table performance(g_id int primary key,
               name text not null,
               mail_id text not null,
               day_wise_score float not null,
               python_project_score float not null,
               aiml_project_score float not null,
               interact_score float not null,
               overall_score float not null,
               grade text not null,
               qualify_for_Excellence_Certificate text not null)''')
con.commit()
con.close()

