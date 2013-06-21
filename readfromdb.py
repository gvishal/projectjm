import sqlite3
conn = sqlite3.connect('afterh2t.db')
c = conn.cursor()
c.execute('Select * FROM data')
for r in c.fetchall():
	for member in r:
		print member
