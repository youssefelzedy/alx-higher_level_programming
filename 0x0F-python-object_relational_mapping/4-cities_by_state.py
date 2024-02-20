#!/usr/bin/python3

'''
3-my_safe_filter_states.py:
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password>
<database name> <state name searched>
'''

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                FROM `cities`\
                JOIN `states` ON `cities`.`state_id` = `states`.`id`\
                ORDER BY `cities`.`id`")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
