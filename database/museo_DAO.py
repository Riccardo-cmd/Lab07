import mysql

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO

    def get_all_musei(self):
        cnx = ConnessioneDB().get_connection()

        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM museo")

        result = []

        for row in cursor:
            museo = Museo(row[0], row[1], row[2])
            result.append(museo)

        cursor.close()
        cnx.close()

        return result