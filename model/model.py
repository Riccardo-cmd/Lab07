from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo_id_str:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        # Converte l'ID del museo da stringa a intero.
        # Se il valore è "Nessun filtro" o None, imposta l'ID a None.
        museo_id = None
        if museo_id_str and museo_id_str != "Nessun filtro":
            try:
                museo_id = int(museo_id_str)
            except ValueError:
                print(f"Errore: ID museo non valido: {museo_id_str}")
                museo_id = None

        # Imposta l'epoca a None se il valore è "Nessun filtro"
        epoca_filtro = epoca
        if epoca == "Nessun filtro":
            epoca_filtro = None

        # Chiama il DAO con i parametri puliti (int|None, str|None)
        return self._artefatto_dao.get_artefatti_filtrati(museo_id, epoca_filtro)

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        return self._artefatto_dao.get_epoche()

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        return self._museo_dao.get_all_musei()
