from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO

    def get_epoche(self) -> list[str]:
        """
        Restituisce un elenco di tutte le epoche uniche presenti nella tabella degli artefatti.
        """
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore di connessione al database.")
            return []

        cursor = cnx.cursor()
        query = """
            SELECT DISTINCT epoca
            FROM artefatto
            WHERE epoca IS NOT NULL AND epoca != ''
            ORDER BY epoca
        """
        cursor.execute(query)

        # Uso una list comprehension per estrarre il primo (e unico) elemento da ogni riga
        result = [row[0] for row in cursor]

        cursor.close()
        cnx.close()
        return result

    def get_artefatti_filtrati(self, museo_id: int | None, epoca: str | None) -> list[Artefatto]:
        """
        Restituisce un elenco di artefatti filtrati in base all'ID del museo e/o all'epoca.
        I filtri sono opzionali.

        :param museo_id: L'ID del museo per cui filtrare (None per nessun filtro)
        :param epoca: La stringa dell'epoca per cui filtrare (None per nessun filtro)
        :return: Una lista di oggetti Artefatto.
        """
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("Errore di connessione al database.")
            return []

        cursor = cnx.cursor()
        query = """
            SELECT *
            FROM artefatto a
            WHERE a.id_museo = COALESCE(%s, a.id_museo)
              AND a.epoca = COALESCE(%s, a.epoca)
            ORDER BY a.nome
        """
        # COALESCE(%s, colonna) usa il parametro %s se non è NULL,
        # altrimenti usa il valore della colonna stessa (annullando il filtro).
        params = (museo_id, epoca)

        cursor.execute(query, params)

        result = []
        for row in cursor:
            # Mappiamo i risultati della riga nel DTO Artefatto
            # (id, nome, tipologia, epoca, id_museo)
            artefatto = Artefatto(row[0], row[1], row[2], row[3], row[4])
            result.append(artefatto)

        cursor.close()
        cnx.close()
        return result
