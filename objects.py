import sqlite3 as lite
import sys


object = (
    (1, 'Cat', 22000),
    (2, 'Dog', 25000),
    (3, 'Car', 28000),
    (4, 'Human', 20000),
    (5, 'Building', 29000),
)


con = lite.connect('objects.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS obj")
    cur.execute("CREATE TABLE obj(id INT, label VARCHAR(50),features INT)")
    cur.executemany("INSERT INTO obj VALUES(?,?,?)", object)