# Database management system

# Python includes SQLite
"""
The python Database API provides a standard mechanism for programming a wide variery of database management systems,
including SQLite.
	1. Connect
	2. Create
	3. Interact
	4. Commit & Rollback
	5. Close
"""

# Database API as Python code
"""
import sqlite3
connection = sqlite3.connect('test.sqlite')
cursor = connection.cursor()
cursor.execute("""SELECT DATE('NOW')""")
connection.commit()
connection.close()
"""

# Define your database schema
"""
create table athletes(
	id integer primary key autoincrement unique not null,
	name text not null,
	dob date not null)

create table timing_data(
	athlete_id integer not null,
	value text not null,
	foreign key (athlete_id) references athletes)
"""


