
# This file defines docstrings

USERS_CSV = """
id,name,email
1,Alice,alice@example.com
2,Bob,bob@example.com
3,Charlie,charlie@example.com
"""

ORDERS_CSV = """
id,user_id,product,amount
1,1,Book,2
2,1,Pen,10
3,2,Notebook,5
"""

# Old way:
# cursor.executescript("""
# INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
# INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com');
# INSERT INTO users (name, email) VALUES ('Charlie', 'charlie@example.com');
# """)
# cursor.executescript("""
# INSERT INTO orders (user_id, product, amount) VALUES (1, 'Book', 2);
# INSERT INTO orders (user_id, product, amount) VALUES (1, 'Pen', 10);
# INSERT INTO orders (user_id, product, amount) VALUES (2, 'Notebook', 5);
# """)


##
#


# ###################################################    NOTES    ######################################################






# ######################################################################################################################

##
#

