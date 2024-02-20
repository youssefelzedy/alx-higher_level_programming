#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s", (name, ))

    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
