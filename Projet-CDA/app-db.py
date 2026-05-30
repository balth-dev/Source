from contextlib import nullcontext

import mariadb

# connection parameters
conn_params= {
    "user" : "root",
    "password" : "",
    "host" : "localhost",
    "database" : "resa_salles"
}

connection = None
cursor: mariadb.Cursor

def select_data():
    global cursor
    _initiate_connection()
    # Populate countries table  with some data
    cursor.execute("SELECT * FROM resa_salles.users order by id_user asc")

    # print content
    rows = cursor.fetchall()
    for row in rows:
        print(*row, sep=' ')
    _close_connection()

def _initiate_connection():
    global connection, cursor
    # Establish a connection
    connection = mariadb.connect(**conn_params)
    cursor = connection.cursor()
    return cursor

def _close_connection():
    global connection, cursor
    cursor.close()
    connection.close()

if __name__ == "__main__":
    print("Voulez-vous")
    print("1 - Afficher tous les utilisateurs")

    choix =  input()
    if choix == "1":
        select_data()
    else:
        print("Choisissez 1, 2 ou 3")
        exit()
