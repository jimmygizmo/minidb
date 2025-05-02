

USERS_CREATE="""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
"""

ORDERS_CREATE="""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
"""


##
#


# ###################################################    NOTES    ######################################################






# ######################################################################################################################

##
#
