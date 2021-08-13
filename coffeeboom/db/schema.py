import sqlite3



connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()

# cursor.execute("create table section (id bigint PRIMARY KEY, name text)")
#
# cursor.execute("create table goods (id bigint PRIMARY KEY, name text, price INTEGER, section_id references section(id))")
#
# connection.commit()

cursor.execute("SELECT * FROM section")
section = cursor.fetchall()


cursor.execute("SELECT * FROM goods WHERE section_id = 1")

goods = cursor.fetchall()

for item in goods:
    print(item)
