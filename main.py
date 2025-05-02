
import sqlite3
import csv
import io
import minidb.data
import minidb.schema


# ###########################################    GLOBAL INITIALIZATION    ##############################################
# TODO: Maybe add a CONFIGURATION section before this one, maybe even in addition to a config module.
#   Such a section here is in addition to a separate minidb.config module.


# Major resource initialization might go here. Currently the below DB conn/cursor init has been moved in to main()
#
# conn = sqlite3.connect('minidb.db')
# cursor = conn.cursor()


# ########################################    GLOBAL FUNCTION DEFINITIONS    ###########################################
# TODO: If we go OOP in this program, and we might, then the CLASS DEFINITIONS section would go after this one.
#   That is for any 'global' classes (living in main.py). Class can also live inside sub-module files we import.
#   OOP may not be right for this program. We will see. This program is really more about SQL and SQLLite than about
#   Python coding strategies, but a lot of my programs, if they grow much, do often end up getting classes.

def load_initial_data_csv(cursor, csv_data, table_name):
    print(f"Loading initial data into table [{table_name}] ...")
    reader = csv.DictReader(io.StringIO(csv_data.strip()))
    columns = reader.fieldnames
    placeholders = ','.join(['?'] * len(columns))
    insert_sql = f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({placeholders})"
    for row in reader:
        values = [row[col] for col in columns]
        cursor.execute(insert_sql, values)


# ##########################################    GLOBAL CLASS DEFINITIONS    ############################################

# Global classes (Those in the root main.py) will be defined in this section if any are needed.


# ##########################################    DATABASE INITIALIZATION    #############################################

# This is currently inside main(). Another good program structure might use a section here like this.


# ###############################################    MAIN EXECUTION    #################################################


def main():
    conn = sqlite3.connect('minidb.db')
    cursor = conn.cursor()

    print("Creating the database tables fresh from scratch. DB will be created, if necessary.")
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS orders")
    cursor.execute(minidb.schema.USERS_CREATE)
    cursor.execute(minidb.schema.ORDERS_CREATE)
    print("Tables created fresh.")
    load_initial_data_csv(cursor, csv_data=minidb.data.USERS_CSV, table_name="users")
    load_initial_data_csv(cursor, csv_data=minidb.data.ORDERS_CSV, table_name="orders")
    print("Initial data loaded.")

    # TODO: In many cases, we will want to commit after certain steps, not at the end like this.
    #  This program is of course still in its infancy.
    conn.commit()
    print("Database initialized and loaded. Committed.")

    print("Closing database connection.")
    conn.close()


# ######################################################################################################################

if __name__ == "__main__":
    main()


##
#


# ###################################################    NOTES    ######################################################






# ######################################################################################################################

##
#

