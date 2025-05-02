
import sqlite3


conn = sqlite3.connect('minidb.db')
cursor = conn.cursor()


cursor.executescript("""
SELECT * FROM users;
""")

cursor.executescript("""
SELECT * FROM orders;
""")


conn.commit()
conn.close()


##
#


# ###################################################    NOTES    ######################################################






# ######################################################################################################################

##
#

