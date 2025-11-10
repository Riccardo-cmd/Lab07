import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def _load_dropdowns(self):
        """
        Metodo "privato" chiamato dalla View (in load_interface)
        per caricare i dati iniziali nei menu a tendina.
        """
        try:
            # 1. Carica Musei
            musei = self._model.get_musei()
            # Passa i dati alla View perché popoli il suo controllo
            self._view.populate_dd_museo(musei)

            # 2. Carica Epoche
            epoche = self._model.get_epoche()
            # Passa i dati alla View perché popoli il suo controllo
            self._view.populate_dd_epoca(epoche)

            # Aggiorna la pagina per mostrare i dati caricati
            self._view.update()

        except Exception as e:
            # Gestisce eventuali errori durante il caricamento
            self._view.show_alert(f"Errore nel caricamento dei dati iniziali: {e}")

    # CALLBACKS DROPDOWN
    # TODO


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def handle_mostra_artefatti(self, e):
        """
        Gestisce l'evento click sul pulsante "Mostra Artefatti".
        Recupera i filtri selezionati dalla vista, interroga il modello
        e aggiorna la ListView con i risultati.
        """

        # 1. Recupera i valori (le 'key') selezionati dai Dropdown nella View
        try:
            museo_id_str = self._view._dd_museo.value
            epoca = self._view._dd_epoca.value
        except AttributeError:
            self._view.show_alert("Errore: Controlli della vista non inizializzati correttamente.")
            return

        try:
            # 2. Chiama il Modello
            # Passa i filtri (come stringhe) al modello.
            artefatti_filtrati = self._model.get_artefatti_filtrati(museo_id_str, epoca)

            # 3. Aggiorna la Vista
            # Passa la lista di oggetti Artefatto alla View per la visualizzazione
            self._view.update_listview_artefatti(artefatti_filtrati)

        except Exception as e:
            self._view.show_alert(f"Errore durante la ricerca degli artefatti: {e}")